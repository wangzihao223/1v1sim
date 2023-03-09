"""
多目标同时临空方式一
"""
#设某作战平台Ai，与攻击目标距离为Ri，导弹速度为Vi。
#若为变速导弹：弹道变速点与目标距离为RI，速度为VI，临空时间为T，导弹发射反应时间为Δt。
#ti:发射时刻


#常规导弹
def routine(T, Ri, Vi, Δt):
    return  T - (Ri / Vi + Δt)
    

#变速导弹
def change_speed(T, Ri, Vi, RI, VI, Δt):
    return T - ((Ri - RI) / Vi + RI / VI + Δt)

#同型或不同型的导弹速度均可能存在差异采取随机抽样获取Vi~U(Vmax, Vmin).


"""
多目标同时临空方式二
"""
# 为多目标、多方向攻击导弹同时到达攻击目标的防御边界。设被打击目标的防御边界为Rk，则：

#常规发射时刻
def routine_fire(T, Ri, Vi, Rk, Δt):
    return T - ((Ri - Rk )/ Vi + Δt)

#变速发射时刻(一般RI<Rk)
def change_speed_fire(T, Ri, Vi, Rk, Δt):
    return T - ((Ri - Rk )/ Vi + Δt)


#高低混合（一般RI>Rk）
def high_and_low_mixing(T, Ri, Vi, RI, VI, Rk, Δt):
    return T - ((Ri - RI) / Vi + (RI - Rk) / VI + Δt)

"""
目标威胁判断排序
"""
#主要目的是决定拦截目标先后的问题，按威胁程度，首先是来袭导弹到达的时间，其次是来袭导弹到达的路径。
#来袭目标i，相对于某作战平台j，其到达时间为Tij（过j平台捷径点），且航路捷径为Pji，则该目标相对于某作战平台j的威胁系数为：
def threat_coefficient(a1, Tij, a2, Pji):
    """
    alpha为威胁系数,威胁系数越小,目标威胁越大
    a1,a2为权系数且a1+a2=1,a1>a2
    """
    alpha = a1 * Tij + a2 * Pji
    return alpha

"""
反导防御目标拦截可能性计算
"""
#某型防空导弹杀伤区远界Ry, 近界Rj,拦截目标最大航路捷径Pmax，水平杀伤区最大航路角θmax,拦截距离段导弹平均速度V，导弹发射反应时间为Δt
#目标参数 ：距离（Rm） 高度（Hm） 航捷（Pm） 速度（Vm）
#远界拦截可能性计算（Ryf）
def far_intercept(Ry, Pm, Hm, V, Vm, Δt):
    Xyf = (Ry**2 - Pm**2 - Hm**2)**0.5 + (Ry / V + Δt) * Vm
    Ryf = (Xyf**2 + Pm**2 + Hm**2)**0.5
    return Ryf

#近界拦截可能性计算（Rjf）
#近拦截Rj值判定
def judge_Rj(Pm , sinθmax, Rj):
    if (Pm / sinθmax) > Rj:
        Rj = (Pm / sinθmax)
    else:
        Rj = Rj
    

def near_intercept(Rj, Pm, Hm, V, Vm, Δt):
    Xyf = (Rj**2 - Pm**2 - Hm**2)**0.5 + (Rj / V + Δt) * Vm
    Rjf = (Xyf**2 + Pm**2 + Hm**2)**0.5
    return Rjf


#判断模块

# def judge_far(Ryf, Rm, Pm, Pmax):
#     if Ryf >= Rm and Pm <= Pmax:
#      """
#      远拦截
#      """
#      print("可拦截")
#     else:
#         print("不可拦截")

# def judge_near(Rjf, Rm, Pm, Pmax):
#     if Rjf >= Rm and Pm <= Pmax:
#      """
#      近拦截
#      """
#      print("可拦截")
#     else:
#         print("不可拦截")