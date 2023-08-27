# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/7/8
Last Modified: 2023/7/8
Description: 
"""
import os

import pandas as pd

from core.data import HistoryData
from core.funcs import AreaStatistic


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

    # 2.
    pass


if __name__ == '__main__':
    # 获取历史数据
    data = HistoryData().get_data(history_count=995)

    # 历史数据列表
    data_list = data.get("result")

    start_statistic(data_list)
