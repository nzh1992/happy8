# -*- coding: utf-8 -*-
"""
Author: niziheng
Created Date: 2023/8/27
Last Modified: 2023/8/27
Description: 
"""
import random

numbs = list(range(1, 81))

# 1. 低频号
low_freq_numbs = [20, 22, 25, 26, 31, 33, 38, 46, 55, 58, 72, 74, 76]

# 2. 近20期超高频
high_freq_20_numbs = [9, 13, 22, 30, 36, 54, 63, 71]

# 3. 近50期最多前十
most_50_numbs = [71, 21, 11, 35, 41, 12, 61, 29, 30]

# 4. 近50期最少前十
less_50_numbs = [19, 46, 2, 38, 52, 72, 6, 17, 48, 74]

# 3. 上期开奖号码
last_period_numbs = [2, 3, 4, 9, 14, 16, 22, 26, 30, 35, 36, 47, 56, 58, 60, 62, 63, 66, 76, 80]

# 输出剩余号码
unexpect_numbs_list = [
    low_freq_numbs,
    high_freq_20_numbs,
    last_period_numbs,
    most_50_numbs,
    less_50_numbs
]
for l in unexpect_numbs_list:
    for n in l:
        if n in numbs:
            numbs.remove(n)

print(f"排除后，剩余{len(numbs)}个号码")
print(numbs)
print("-" * 50)

# 随机取两个值
random_two = random.sample(numbs, 2)
print("随机取出两个号码")
print(random_two)
