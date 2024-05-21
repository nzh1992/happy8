# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/7/8
Last Modified: 2023/7/8
Description: 
"""
import os
import random

import pandas as pd

from core.data import HistoryData
from core.funcs import AreaStatistic, HeatStatistic, LessStatistic, RamdomSet


def get_statistic_result_dir():
    """获取统计输出目录"""
    main_fp = os.path.dirname(__file__)
    result_dir = os.path.join(main_fp, "result_files")

    return result_dir


def start_statistic(data_list):
    """
    开始统计历史数据

    :param data_list: list. 历史数据列表
    :return:
    """
    # 1. 分区数量统计
    # 预设分区数量：2(大小区)，4（4分区），8，10，20，40
    area_count_list = [2, 4, 8, 10, 20, 40]
    for area_count in area_count_list:
        file_name = f"{area_count}分区统计.xlsx"
        print(f"正在生成'{file_name}'")

        stat_result = []    # 所有统计结果
        period_list = []    # 所有期数
        red_list = []       # 所有中奖号码

        for d in data_list:
            # 计算每期统计结果
            data = d.get("red")
            area_count_result = AreaStatistic.count_statistic(data, area_count)
            stat_result.append(area_count_result)

            # 每期元信息
            period_list.append(d.get("code"))
            red_list.append(data)

        # 统计df
        df = pd.DataFrame(stat_result)

        # 元信息df
        mate_dict = {'period': period_list, 'red': red_list}
        mate_df = pd.DataFrame(mate_dict)

        # 拼接统计和元信息，组成新df
        result_df = pd.concat([mate_df, df], axis=1)

        # 生成excel
        file_dir = os.path.join(get_statistic_result_dir(), "area")
        os.makedirs(file_dir, exist_ok=True)
        fp = os.path.join(file_dir, file_name)
        result_df.to_excel(fp, index=False)
        print(f"'{file_name}'生成成功.")
        print("-" * 50)

    # 2. 热力图
    # 预设历史数据期数：20，30，50，100，200，300，500，全部
    period_count_list = [20, 30, 50, 100, 200, 300, 500, 'all']
    heat_result_list = []
    for period_count in period_count_list:
        heat_result = HeatStatistic.heat_statistic(data_list, period_count)
        heat_result_list.append(heat_result)

    df = pd.DataFrame(heat_result_list, index=period_count_list)

    heat_file_name = "haet_map.xlsx"
    haet_file_dir = os.path.join(get_statistic_result_dir(), "heat_map")
    os.makedirs(haet_file_dir, exist_ok=True)
    heat_fp = os.path.join(haet_file_dir, heat_file_name)
    df.to_excel(heat_fp)
    print(f"{heat_file_name}生成成功")
    print("-" * 50)

    # 热力图分析

    # 近20期热号列表（出现大于等于6次表示热号）
    period20_dict = heat_result_list[0]
    period20_list = list(period20_dict.items())
    period20_list.sort(key=lambda x: x[1], reverse=True)
    hot20_top20 = period20_list[:20]
    # 从20个热号中，随机取5个
    random_hot_5_1 = random.sample(hot20_top20, 5)
    print(f"从20个热号中，随机取5个: {random_hot_5_1}")
    random_hot_5_2 = random.sample(hot20_top20, 5)
    print(f"从20个热号中，随机取5个: {random_hot_5_2}")

    # 3. 历史开奖表
    period_list = []
    number_list = []
    history_dict_list = []
    red_list = []  # 每期红色号码出现的数量
    blue_list = []  # 每期蓝色号码出现的数量
    for d in data_list:
        period_list.append(d.get("code"))
        number_list.append(d.get("red"))

        number_str_list = d.get("red").split(",")
        result_dict = dict(zip(
            list(range(1, 81)),
            [''] * 80
        ))

        red_count = 0
        blue_count = 0

        for number_str in number_str_list:
            number_int = int(number_str)
            result_dict[number_int] = number_str

            if number_int in [20, 22, 25, 26, 55, 58, 72, 74]:
                red_count += 1

            if number_int in [31, 33, 38, 46, 76]:
                blue_count += 1

        history_dict_list.append(result_dict)
        red_list.append(red_count)
        blue_list.append(blue_count)

    history_df = pd.DataFrame(history_dict_list)

    # 元信息df
    mate_dict = {'period': period_list, 'numbers': number_list}
    mate_df = pd.DataFrame(mate_dict)

    # 红色号码、蓝色号码、红蓝相加号码出现的次数
    blue_and_red_count = list(map(lambda x: x[0] + x[1], zip(red_list, blue_list)))
    blue_red_dict = {'red': red_list, 'blue': blue_list, 'red_and_blue': blue_and_red_count}
    color_df = pd.DataFrame(blue_red_dict)

    # 拼接统计和元信息，组成新df
    history_main_df = pd.concat([mate_df, history_df, color_df], axis=1)

    history_file_name = "history.xlsx"
    history_file_dir = os.path.join(get_statistic_result_dir(), "history")
    os.makedirs(history_file_dir, exist_ok=True)
    history_fp = os.path.join(history_file_dir, history_file_name)
    history_main_df.to_excel(history_fp)
    print(f"{history_file_name}生成成功")
    print("-" * 50)



if __name__ == '__main__':
    # 获取历史数据
    # data = HistoryData().get_data(history_count=995)

    # 历史数据列表
    # data_list = data.get("result")

    # start_statistic(data_list)

    # 获取历史数据，df格式
    df = HistoryData().get_df(history_count=2000)
    less_40 = LessStatistic().less_statistic(df, period_count=2000, top=40)

    # 计算热号40个
    hot_40 = set(range(1, 81)) - set(less_40)

    # 剔除我认为的低概率号
    # 1. 1~10号
    out_1 = set(range(1, 11))
    # 2. 10~20号
    out_2 = set(range(11, 21))

    # 选号集合
    random_set = hot_40 - out_1
    print(f"选号集合,共计{len(random_set)}个，如下：")
    print(f"{random_set}")

    # 随机5注
    # 规则：从热号集合中机选10个。
    print("开始随机生成5注，快乐8选10玩法：")
    for i in range(5):
        hot_10 = RamdomSet(random_set).get(10)
        print(f"第{i+1}注: {hot_10}")