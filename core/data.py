# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/7/8
Last Modified: 2023/7/8
Description: 获取快乐8历史数据
"""
import json

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

        resp = requests.get(self.history_url, params=query_params, headers=headers)

        return json.loads(resp.content)
