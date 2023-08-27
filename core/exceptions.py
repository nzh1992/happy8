# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/8/27
Last Modified: 2023/8/27
Description: 自定义异常类
"""


class AreaCountError(Exception):
    def __init__(self):
        self.msg = "分区个数异常，不是80的公约数，导致无法均匀分区"

    def __str__(self):
        return f"异常：{self.msg}"
