"""
sim manager module
"""


import heapq


from greenlet import greenlet, getcurrent

def register(init_process:list, queue:list):
    """
    init process
        Args:
    """
    self_process = getcurrent()
    for process_tuple in init_process:
        process = process_tuple[0] 
        args = process_tuple[1]

        new_args = [self_process, queue]
        new_args.extend(args)
        process.switch(*new_args)
    return None


def start_manager(queue:list, max_step:int, init_process:list, start_time=0) -> greenlet:
    """
    start a manager process
    """
    args = [queue, start_time, max_step, init_process]
    process = greenlet(manager_loop)
    process.switch(*args)
    return process


def manager_loop(queue:list, now:int, max_step:int, init_process:list) -> None:
    """
    manager main loop
    """
    register(init_process, queue)
    while now < max_step and queue != []:
        now = handle_event(queue, now)
    
    return None


def handle_event(queue:list, now:int) -> int:
    """
        handle event , switch greenlet
        queue [
            (step, process, (callback, args))
        ]
    """
    res = now 
    while queue:
        step, _, _, _ = heapq.nsmallest(1, queue)[0]            
        if step == now:
            _, _, event, callback = heapq.heappop(queue)
            event.switch(callback)
        else:
            return step
    return res
     
    