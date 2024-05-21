# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/8/27
Last Modified: 2023/8/27
Description: 统计方法
"""
import random
import copy

from core.exceptions import AreaCountError


class AreaStatistic:
    """分区统计"""
    @classmethod
    def get_range_list(cls, area_count):
        """获取分区范围列表"""
        # 分区号码个数必须是80的公约数，避免无法整除
        if 80 % area_count != 0:
            raise AreaCountError()

        area_range_list = []
        area_size = int(80 / area_count)  # 每个区域大小
        for i in range(area_count):
            range_start = i * area_size + 1  # 每个区起始数值
            range_end = (i + 1) * area_size  # 每个区结束数值
            area_range_list.append((range_start, range_end))

        return area_range_list

    @classmethod
    def count_statistic(cls, data, area_count):
        """
        统计每期中奖号码所属分区的中号号码数量

        :param data: str. 每期中奖号码，格式例如"1,2,3,...,19,20"
        :param area_count: int. 每个区包含的号码个数。例如：8，表示分8个区，每个区包含10个号码。
        :return: dict. key: 分区范围，value: 每个区的中奖号码个数。
        """
        # 分区范围列表
        area_range_list = cls.get_range_list(area_count)

        # 分区结果默认值，有多少个区就有多少个默认值
        default_values = [0] * area_count

        # 分区结果字典
        area_range_dict = dict(zip(area_range_list, default_values))

        # 中奖号码，字符串转列表
        datas = data.split(',')

        # 统计分区结果
        for d in datas:
            d_num = int(d)  # 字符串转数值

            # 判断所属区
            for area_range in area_range_list:
                if area_range[0] <= d_num <= area_range[1]:
                    area_range_dict[area_range] += 1

        return area_range_dict


class HeatStatistic:
    @classmethod
    def heat_statistic(cls, data_list, period_count):
        """
        统计给定期数内(从当前期开始计算)的中奖号码累计出现次数

        :param data_list: list. 全部历史数据
        :param period_count: int. 给定期数
        :return:
        """
        # 获取指定期数内的历史数据
        if period_count == 'all':
            # 全部期数，不做处理
            pass
        else:
            data_list = data_list[:period_count]

        # 统计各个号码出现的次数
        numbs = list(range(1, 81))
        init_values = [0] * 80
        heat_result = dict(zip(numbs, init_values))

        for d in data_list:
            red_numbers = d.get("red")
            red_number_list = [int(red_number) for red_number in red_numbers.split(",")]

            for red_number in red_number_list:
                heat_result[int(red_number)] += 1

        return heat_result


class LessStatistic:
    """出现次数最少的top10统计"""
    @staticmethod
    def less_statistic(df, period_count, top=10):
        """
        统计给定期数内(从当前期开始计算)的中奖号码累计出现次数最少的前十名

        :param df: pd.DataFrame. 历史数据
        :param period_count: int. 统计期数.
        :param top: int. 前N名，默认是前10名
        :return:
        """
        target_df = df[:period_count]

        # 中奖号码计数
        numbers = [i for i in range(1, 81)]
        init_number = [0] * 80
        total_dict = dict(zip(numbers, init_number))

        # 遍历DF
        for row in target_df.iterrows():
            for num, is_red in row[1].items():
                if is_red:
                    total_dict[int(num)] += 1

        # 按升序排序
        sorted_list = sorted(total_dict.items(), key=lambda x: x[1], reverse=False)

        # 输出
        print(f"最近{period_count}期，中奖次数最少的号码如下：")
        for number, count in sorted_list[:top]:
            print(f"数字：{number}，出现次数: {count}")

        # 冷号排序
        sorted_numbers = [l[0] for l in sorted_list[:top]]
        sorted_numbers.sort(reverse=False)
        print(f"冷号排序: {sorted_numbers}")

        return sorted_numbers


class RamdomSet:
    def __init__(self, data):
        """用一个数据集合初始化data"""
        self.data = list(data)

    def get(self, length):
        """从数据集合中随机获取length个元素，并按升序排列后返回"""
        data_copy = copy.deepcopy(self.data)
        random.shuffle(data_copy)
        result = data_copy[:length]
        result.sort(reverse=False)
        return result


if __name__ == '__main__':
    data = '02,07,10,13,28,29,34,36,37,38,44,48,49,50,52,57,59,63,65,72'
    area_count = 8
    area_range_dict = AreaStatistic.count_statistic(data, area_count)
    print(area_range_dict)
