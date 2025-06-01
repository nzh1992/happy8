import random


l = [
    6, 8, 17, 23, 25,
    39, 47, 48, 52, 61,
]

for i in range(5):
    r = random.sample(l, 5)
    r.sort()
    print(f"第{i+1}注：{r}")