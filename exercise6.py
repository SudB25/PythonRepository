# def sub(a, b):
#     return a-b

# ans = sub(a=10, b=20)
# print(ans)

def fib(x):
    if x==1 or x==2:
        return 1
    else:
        return fib(x-1)+fib(x-2)
