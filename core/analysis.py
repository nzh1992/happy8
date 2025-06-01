# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2024/1/20
Last Modified: 2024/1/20
Description: 
"""
from copy import deepcopy

from core.data import HistoryData


class Happy8:
    def __init__(self):
        pass

    def run(self):
        numbers_list = HistoryData().get_numbers_list()
        self.algorithm2(numbers_list)

    def algorithm1(self, numbers_list):
        """
        算法1

        统计连续3期中奖的号码

        :return:
        """
        for idx, reds in enumerate(numbers_list):
            if idx == len(numbers_list) - 2:
                break

            s1 = set(reds)
            s2 = set(numbers_list[idx + 1])
            s3 = set(numbers_list[idx + 2])

            result = s1.intersection(s2).intersection(s3)
            print(f"第{idx}期. 重复数量：{len(result)}. 重复号码: {result}")

    def generate(self, numbers_list):
        """
        算法2

        按照8个数字一组分区计算，计算每期数字出现在各个分区的数量

        :param numbers_list:
        :return:
        """
        # 划分区间
        area_dict = {}
        area = []
        for idx in range(1, 81):
            area.append(idx)
            if idx % 8 == 0:
                area_cp = deepcopy(area)
                area_dict.update({str(int(idx/8)): area_cp})
                area.clear()

        for idx, reds in enumerate(numbers_list):
            # 区间计数器
            area_count = {k: 0 for k in area_dict.keys()}

            for red in reds:
                for area_name, area in area_dict.items():
                    if red in area:
                        area_count[area_name] += 1

            print(f"第{idx}期。分区统计数量：")
            print(area_count)


if __name__ == '__main__':
    Happy8().run()