"""
关键指标
t~(正态和均匀分布)
R~(正态和均匀分布)
P~(二项分布)
X~(均匀分布)
"""


from make_distribution import *

# red Task release 1
def troop_assembly(target):
    """
    部队集合事件，返回集合时间(t)
    Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)

def networking_building(target):
    """
    组网建链，返回完成时间(t)
    Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)


# red Early warning detection 2
def detection_range(target):
    """
    探测距离(R)
    Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)


def detection_probability(target):
    """
    探测概率(P)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)


def Target_integrity(target):
    """
    目标完整度(p)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)


def reaction_time(target):
    """
    反应时间(t)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)


#red Command and control 3
# (target recognition 1)

def control_range(target):
    """
    控制距离(R)
    Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)


def accuracy_of_control(target):
    """
    控制正确率(P)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)


def control_time(target):
     """
    控制时间(T)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
     return distribute_selector(target)


# red Command and control 3
# （Battlefield situation 2）
def control_integrity(target):
     """
    控制完整度(P)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
     return distribute_selector(target)

def control_formation_time(target):
    """
    控制形成时间(T)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)

# red Command and control 3
# （Target indication 3）
def control_accuracy(target):
    """
    控制精度(sigema(t))
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)

# +控制时间control_time


# red Fire Strike 4
def strike_time(target):
    """
    打击时间(t)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)

def capture_probability(target):
    """
    捕捉概率(P)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)

def hit_probability(target):
    """
    命中概率(P)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)

def damage_degree(target):
    """
    毁伤程度(X)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)


# red Enemy confrontation 5
def electronic_warfare(target):
    """
   软对抗成功率(P)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)

def kill_probability(target):
    """
    硬武器杀伤概率(P)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)


# red Effect evaluation 6
def evaluation_accuracy(target):
    """
    评估正确率(P)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)

def evaluation_time(target):
    """
    评估时间(t)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)




# blue Task release 1 = red Task release 1

#blue Early warning detection 2
#(1)距离(2)探测概率(3)目标完整度
def recognition_accuracy(target):
    """
    识别正确率(p)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)
#(5)探测时间


#blue Command and control 3
#(1)目标完整度(2)反应时间


def identification_and_distribution(target):
    """
    目标识别与分配时间(t)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)


#blue Fire Strike 4
#目标指示（1）
#（1）正确率（2）指示距离（3）指示精度（4）反应时间

#编队导弹反导（2）
def interception_distance(target):
    """
    拦截距离(R)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)

def interception_accuracy(target):
    """
    拦截正确率(P)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)
#（3）命中概率

#舰炮反导（3）
#命中概率

#电子战
def means_of_confrontation(target):
    """
    对抗手段(n)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)
#（2）成功率《电子战》


#效果评估 Effect evaluation 5
#（1）评估正确率（2）评估时间
def re_reaction_time(target):
    """
    二次打击反应时间(t)
     Args:
        target: list ["gaussian",[miu, sigma]]
    """
    return distribute_selector(target)



def distribute_selector(target):
    """
        分布选择
    """
    args = target[1]
    args.append(1)
    if target[0] == "gaussian":
        res = make_gaussian(*args)
    elif target[0] == "binomial":
        res = make_binomial(*args)
    else:
        res = make_uniform(*args)
    return res[0]