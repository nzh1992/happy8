# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/7/8
Last Modified: 2023/7/8
Description: 获取快乐8历史数据
"""
import json

import pandas as pd
import requests


class HistoryData:
    def __init__(self):
        self.base_url = "http://www.cwl.gov.cn"
        self.history_url = "http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice"

    def _make_history_params(self, page_size=100):
        params = {
            "name": "kl8",
            "issueCount": "",
            "issueStart": "",
            "issueEnd": "",
            "dayStart": "",
            "dayEnd": "",
            "pageNo": "1",
            "pageSize": str(page_size),
            "week": "",
            "systemType": "PC"
        }

        return params

    def _make_history_headers(self):
        headers = {
            "Cookie": "HMF_CI=50c2774011b9f462867e5abaadff1245ca4ae4f3fad5563b356191d4088a1a399695cd9f192b80170f76f012e5e7f90e1952f76e7dd3f0c723d2412527c6ee6677; 21_vq=5",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }

        return headers

    def get_data(self, history_count=100):
        query_params = self._make_history_params(history_count)
        headers = self._make_history_headers()

        resp = requests.get(self.history_url, params=query_params, headers=headers, verify=False)

        return json.loads(resp.content)

    def get_df(self, history_count=100):
        """
        将统计结果以pd.DataFrame的形式返回，以方便后续统计

        :param history_count: int. 数据的期数，默认最近100期
        :return: pd.DataFrame
        """
        content = self.get_data(history_count)
        results = content.get("result")

        index_list = []     # 索引列表
        data_list = []      # 数据列表

        for result in results:
            # 保存索引
            index_list.append(result.get("code"))

            # 保存数据，出现中奖号码为True，未出现为False
            reds = [int(red) for red in result.get("red").split(",")]
            data = [False] * 80
            for red in reds:
                data[red-1] = True

            data_list.append(data)

        # 创建DF
        df = pd.DataFrame(data=data_list, index=index_list, columns=[str(i) for i in range(1, 81)])

        return df