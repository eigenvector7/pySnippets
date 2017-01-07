"""
Recursive implementation of fibonacci sequence. Accepts zero indexed "upto" as the argument.
So - if you want a list with first 10 fibonacci numbers, you should call fibo(9).
"""


def fibo(n):
    fn=[]
    o = ''
    if type(n) != int:
        print("Input should be a number")
    elif n < 0:
        print("Input can not be a negative number")
    elif n == 0:
        fn.append(1)
    elif n == 1:
        fn = fibo(n-1)
        fn.append(1)
    else:
        fn = fibo(n-1)
        print("Hello")
        print(fn)
        o = fn[-1]+fn[-2]
        fn.append(o)
    return fn






