




def decorator(func):
    def f(a, b):
        r = func(a,b)
        print("jjjjj")
        return r
    return f

@decorator
def func(a, b):
    print(a,b)
    return (a,b)

func(1,2)