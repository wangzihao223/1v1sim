
from mokuai import*
import time



def operation_task_release(start, width, size):
    t = troop_assembly(start, width, size)
    print("兵力集结用时", t)
    time.sleep(t)
    i = networking_building(start, width, size)
    print("组网建链用时", i)
    time.sleep(i)


def early_warning_detection(start, width, size, n, p):#p < 1
    print("预警探测")
    ti = reaction_time(start, width, size)
    time.sleep(ti)
    di = detection_range(start, width, size)
    print("探测距离为", di)
    pr = target_integrity(n, p, size)
    print("目标完整度为", pr)
    print("反应时间为", ti)



def command_and_control(miu, sigma, size, n, p):
   print("目标识别")
   ta = target_recognition(miu, sigma, size, n, p)
   ti = reaction_time(miu, sigma, size)
   print(ta)
   print("识别时间为", ti)
   time.sleep(ti)
   print("战场态势")
   ba = battlefield_situation(miu, sigma,n, p, size)
   print(ba)




operation_task_release(5, 5, 1)
early_warning_detection(5, 5, 1, 2, 0.9)
command_and_control(2, 2, 1, 2, 0.9)



