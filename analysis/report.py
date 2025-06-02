"""
推荐报告
"""
from datetime import datetime

from utils.logger import logger
from core.data import HistoryData


class Report:
    def __init__(self):
        # 报告开始时间
        self.start_time = datetime.now()
        # 获取历史信息
        self._get_history_data()

    def __print_line(self):
        logger.info('-' * 100)

    def _welcome(self):
        """
        欢迎信息
        """
        logger.info("尊敬的快乐8怨总，您好！")

        today = self.start_time.strftime('%Y-%m-%d')
        dt_time = self.start_time.strftime('%Y-%m-%d %H:%M:%S')
        weekday = self.start_time.weekday()
        logger.info(f"今天是{today}, 星期{weekday + 1}")
        self.__print_line()

    def _get_history_data(self):
        """获取历史数据"""
        data = HistoryData().get_data(history_count=1)
        # 历史总共期数
        self.history_total_periods = data.get("total")
        # 上期开奖数据
        last_period_data = data.get("result")[0]
        # 上期开奖期号
        self.last_period_code = last_period_data["code"]
        # 上期开奖信息网址
        self.last_period_detail_link = last_period_data["detailsLink"]
        # 上期开奖号码
        self.last_period_reds = [int(numb) for numb in last_period_data["red"].strip().split(",")]
        # 上期销售额
        self.last_period_sales = last_period_data.get("sales", 0)
        # 当前奖池资金
        self.pool_money = last_period_data["poolmoney"]


        return data

    def _current_info(self):
        """
        最近一期信息
        """
        pass


    def start(self):
        """
        开始生成报告
        :return:
        """
        self._welcome()


if __name__ == '__main__':
    Report().start()
