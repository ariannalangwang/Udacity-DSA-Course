def fib(n):
    counter = 0
    first = 0
    second = 1
    temp = 0
    while counter <= n:
        print(first)
        temp = first + second
        first = second
        second = temp
        counter += 1


fib(10)

"""Implement a function recursively to get the desired Fibonacci sequence value.
Your code should have the same input/output as the iterative code."""

def get_fib(n):
    if n == 0:
        return 0
    if n == 1: 
        return 1
    return get_fib(n-1) + get_fib(n-2)

# Test cases
print('recursive solutions:')
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
