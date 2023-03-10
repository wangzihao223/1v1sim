"""
生成分布模块
"""

# 随机生成高斯分布
from scipy import stats
import numpy as np


def make_gaussian(miu, sigma, size):
    """
        生成高斯分布
    """
    return stats.norm.rvs(miu, sigma, size)


def make_binomial(n, p, size):
    """
        生成二项分布
        p：[0, 1]
    """
    return np.random.binomial(n, p, size=size)


def make_uniform(start, width, size):
    """
        生成均匀分布
        Parameters:
        size - 生成的数量
        start - 起始数
        width - 数据宽度（两值之差）
        Returns:
        list
    """
    return  stats.uniform.rvs(size=size, loc=start, scale=width)
