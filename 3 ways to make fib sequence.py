# 3 different ways to make a fib sequence
# algorithm is fib(n-1) + fib(n-2)

# recursion
def fib1(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib1(n-1)+fib1(n-2)


# dynamic programming
# make an array and keep appending to it

def fib2(n):
    f = [0,1]
    for i in range(2,n+2):
        f.append(fib2(n-1) + fib2(n-2))
    return f[n+1]

# memoization
# using dictionary
def fibmemo(n):
    print('123')
print(fib1(5))
print(fib2(6))