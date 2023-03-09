"""
sim manager module
"""


import heapq


import greenlet


def manager_loop(queue:list, now:int, max_step:int):
    """
    manager main loop
    """

    while now < max_step:
        handle_event(queue, now)
    
    return None



def handle_event(queue:list, now:int) -> None:
    """
        handle event , switch greenlet
    """
    while True:
        step, V = heapq.nsmallest(1, queue)[0]            
        if step == now:
            _, event = heapq.heappop(queue),
            event.switch()
        else:
            break
    
    return None
