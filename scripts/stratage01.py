# 2025-01-02 测试
# 筛选阶段
# 1.上一期出现的不要
# 2.不要热号
# 3. 不要近50期热号
# 4. 不要近50期冷号

# 选号阶段
# 1.避免连号
# 2.选最近2期连续空缺超过6个中间的号码
import random

from loguru import logger

reds = set(range(1, 81))


# 1. 排除上期号码
last_period = set([
    2, 15, 20, 22, 32,
    34, 35, 42, 44, 46,
    50, 54, 55, 64, 68,
    71, 74, 75, 77, 79
])
# left_reds = reds - last_period
left_reds = reds
logger.info(f'去掉上期开奖号码，还剩{len(left_reds)}, left_reds: {left_reds}')

# 2. 最近20期热号集合，排除
hot_reds = {2, 7, 12, 15, 32, 42, 44, 59, 71, 72, 76, 77}
left_reds = left_reds - hot_reds
logger.info(f'去掉近20期热号，还剩{len(left_reds)}, left_reds: {left_reds}')

# 3.近50期热号，排除
hot_top_10 = {72, 2, 8, 46, 69, 22, 71, 12, 15, 20}
left_reds = left_reds - hot_top_10
logger.info(f'去掉近50期热号，还剩{len(left_reds)}, left_reds: {left_reds}')

# 4.近50期冷号，排除
cold_top_10 = {45, 1, 10, 47, 62, 21, 24, 51, 19, 27}
left_reds = left_reds - cold_top_10
logger.info(f'去掉近50期热号，还剩{len(left_reds)}, left_reds: {left_reds}')


# 随机10注
for i in range(10):
    random_reds = random.sample(left_reds, 5)
    reds_sorted = sorted(random_reds)
    print(f"第{i+1}注：{reds_sorted}")