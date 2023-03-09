"""
    base greenlet sim framework
"""

import sim_manager


def start_sim(queue:list, max_step:int, init_process:list, start_time=0):
    """
        start sim
    """
    sim_manager.start_manager(queue, max_step, init_process, start_time)