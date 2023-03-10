"""
test sim frame
"""
import green_sim
import sim_process
import sim_manager
import greenlet
from sim_process import green_process

def add(a, b):
    print("a + b  is ", a + b)
    return a + b

def mult(a, b):
    print("a * b is ", a*b)
    return a * b

@green_process
def process1(manager, queue, a, b):
    def init(id, manager):
        print("init: ", id)
        callback_tup = sim_process.commit_event(queue, 1, manager, self, (add, [a,b]))
        args = callback_tup[1]
        callback_tup[0](*args)
    self = sim_process.current_process()
    init("id: 1", manager)
    print("INFO: init 1 ok")
    # main_loop
    callback_tup = sim_process.commit_event(queue, 1, manager, self, (mult, [a,b]))
    args = callback_tup[1]
    callback_tup[0](*args)
    print("process1 end")

@green_process
def process2(manager, queue, a, b):
    def init(id, manager):
        print("init: ", id)
        callback_tup = sim_process.commit_event(queue, 1, manager, self, (add, [a,b]))
        args = callback_tup[1]
        callback_tup[0](*args)
    self = sim_process.current_process()
    init("id: 2", manager)


    print("process2 end")

def main():
    queue = []

    l1 = sim_process.make_process(process1)
    l2 = sim_process.make_process(process2)    
    
    args1 = [2, 3]
    args2 = [3, 4]
    ls = [[l1, args1], [l2, args2]]
    sim_manager.start_manager(queue, 20, ls)
main() 