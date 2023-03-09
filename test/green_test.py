import greenlet


def fun1(g):
    print("hello world")
    a = 1
    b = 2
    args = [a, b]
    g.switch(*args)

def fun2(name, age):
    print("hhhhh")
    print(name, age)
    s = greenlet.getcurrent()
    g = greenlet.greenlet(fun1, s)
    a, b = g.switch(s)
    print(a, b)
s = greenlet.greenlet(fun2)
s2 = greenlet.greenlet(fun2)

q = []
import heapq

heapq.heappush(q, (1, s))
heapq.heappush(q, (1, s2))
print(s)