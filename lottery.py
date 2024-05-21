"""
模拟体彩随机选号
"""
import random


class Lottery:
    def __init__(self):
        self.reds = list(range(1, 36))      # 红球 1~35
        self.blues = list(range(1, 13))     # 篮球 1~12

    def get_red(self):
        """从1-35随机选5个数，作为红球"""
        reds = random.sample(self.reds, 5)
        reds.sort()
        return reds

    def get_blue(self):
        """从1~14随机选2个数，作为蓝球"""
        blues = random.sample(self.blues, 2)
        blues.sort()
        return blues

    def get_random(self, number=1):
        """随机一注"""
        results = []

        for numb in range(1, number+1):
            print(f"第{numb}注：")
            reds = ", ".join([str(i) for i in self.get_red()])
            blues = ", ".join([str(i) for i in self.get_blue()])
            result = f"{reds} + {blues}"
            print(result)
            results.append(result)

        return results


if __name__ == '__main__':
    lottery = Lottery()
    result = lottery.get_random(10)
