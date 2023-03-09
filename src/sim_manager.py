"""
sim manager module
"""


import heapq


from greenlet import greenlet


def start_manager(queue:list, max_step:int, start_time=0) -> greenlet:
    """
    start a manager process
    """
    args = [queue, start_time, max_step]
    process = greenlet(manager_loop, *args)
    return process


def manager_loop(queue:list, now:int, max_step:int) -> None:
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
