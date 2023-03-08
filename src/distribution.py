# 正态分布/高斯分布
# miu = 0，sigma = 1时为标准正态分布
# miu是平均值sigma是方差
#y是概率密度x是生成的符合正态分布的随机变量（x数量可以设置）

import math
from scipy import stats


def gaussian(miu, sigma, size):
    x = stats.norm.rvs(miu, sigma, size)
    e = math.e
    pal = math.pi
    y = 1 / (sigma * ((2 * pal) ** 0.5)) * e ** ((0-0.5)*(((x-miu)/sigma) ** 2))
    return y
# end = gaussian( 2, 3, 1)
# print(end)


# 二项分布
# 二项分布是指在只有两个结果的n次独立的伯努利试验中，所期望的结果出现次数的概率。


from scipy.special import comb


def binomial(n, k, p):


# 输入：n(抽取的试验次数)、k(命中次数/未命中次数)、p(既定的总 命中/未命中 概率).
# 输出：二项分布值

    C = comb(n, k)
    B = C * p**k * (1-p)**(n-k)

    return B


# 例：o = binomial(10, 1, 0.005)
# print(o)


# 均匀分布

def uniform(a, b):  #注意在均匀分布计算时a<b
    x = 1 / a - b
    return x

# 例：er = uniform(100, 101)
# print(er)