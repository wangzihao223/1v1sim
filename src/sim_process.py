"""
sim process module
"""

import heapq 
import time


from greenlet import greenlet, getcurrent


def current_process() -> greenlet:
    """
        get current process
    """
    return getcurrent()


def commit_event(queue:list, step:int, manager:greenlet, self:greenlet, \
                callback:list) -> list:
    """
        向manager提交事件
    """
    id = time.perf_counter()
    element = (step, id, self, callback)
    # print(element)
    heapq.heappush(queue, element)
    # switch manager
    callback = manager.switch()
    
    return callback 


def init_process(queue:list, init_callback:list, self:greenlet, step:int) \
                -> None:
    """
        init process 
    """
    element = (step, self, init_callback)
    heapq.heappush(queue, element)
    return None

def make_process(func):
    return greenlet(func)

def green_process(func):
    def fun(manager, queue, *args):
        res = func(manager, queue, *args)
        manager.switch()
        return res 
    return fun