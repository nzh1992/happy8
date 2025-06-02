"""
目标数据集
"""
import math

import pandas as pd

from core.data import HistoryData


class DataSet:
    def __init__(self, code_from, code_to):
        """

        :param code_from: str. 起始期号
        :param code_to: str. 截止期号
        :return:
        """
        self.code_from = code_from
        self.code_to = code_to
        self.df = self._make_dataset()

    def _make_dataset(self):
        """
        构造数据集
        :return:
        """
        df = HistoryData().get_number_df(self.code_from, self.code_to)
        return df

    def get_number_count(self, reverse=None, top_n=None):
        """
        获取计数器
        :param reverse: bool or None. 默认值为None，按红球数字排序。若值为True，按出现次数降序排列，若值为False，按出现次数升序排列
        :param top_n: int. 取前top_n个结果，默认值为None，取全部结果。
        :return:
        """
        count_dict = {int(i): 0 for i in range(1, 81)}

        for index, row in self.df.iterrows():
            for numb in row:
                count_dict[numb] += 1

        if reverse is None:
            # 按红球数字排序
            if top_n is None:
                return count_dict
            else:
                l = list(count_dict.items())
                return dict(l[:top_n])
        elif reverse is True:
            sorted_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
            if top_n is None:
                return dict(sorted_list)
            else:
                return dict(sorted_list[:top_n])
        elif reverse is False:
            sorted_list = sorted(count_dict.items(), key=lambda x: x[1], reverse=False)
            if top_n is None:
                return dict(sorted_list)
            else:
                return dict(sorted_list[:top_n])

    def get_tail_number_df(self):
        """
        计算每期尾号出现的次数
        :return:
        """
        tail_columns = [f"tail_{i}" for i in range(10)]
        data_list = []

        for index, row in self.df.iterrows():
            count_dict = {f"tail_{i}": 0 for i in range(10)}
            for numb in row:
                tail_numb = numb % 10
                count_dict[f"tail_{tail_numb}"] += 1

            data_list.append(count_dict)

        # 生成df
        tail_number_df = pd.DataFrame(data=data_list, columns=tail_columns, index=self.df.index)

        return tail_number_df

    def get_area_df(self):
        """
        计算每期8分区分布情况
        :return:
        """
        # 定义分区数为8
        AREAS = 8
        # 每个分区的数量
        AREAS_COUNT = 80 / AREAS

        # 定义列名
        area_columns = [f"area_{i}" for i in range(1, AREAS + 1)]
        # 数据列表
        data_list = []

        for index, row in self.df.iterrows():
            count_dict = {f"area_{i}": 0 for i in range(1, AREAS + 1)}
            for numb in row:
                area_numb = math.ceil(numb / AREAS_COUNT)
                count_dict[f"area_{area_numb}"] += 1

            data_list.append(count_dict)

        # 生成df
        area_df = pd.DataFrame(data=data_list, columns=area_columns, index=self.df.index)

        return area_df




if __name__ == '__main__':
    ds = DataSet(code_from="2025131", code_to="2025141")
    # number_count = ds.get_number_count(reverse=None, top_n=5)

    ds.get_area_df()