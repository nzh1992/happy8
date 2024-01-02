# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/8/27
Last Modified: 2023/8/27
Description: 统计方法
"""
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


if __name__ == '__main__':
    data = '02,07,10,13,28,29,34,36,37,38,44,48,49,50,52,57,59,63,65,72'
    area_count = 8
    area_range_dict = AreaStatistic.count_statistic(data, area_count)
    print(area_range_dict)
