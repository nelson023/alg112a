def fibonacci_iterative_with_memoization(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        fib_prev = 0
        fib_current = 1
        for i in range(2, n + 1):
            fib_temp = fib_current
            fib_current = fib_prev + fib_current
            fib_prev = fib_temp
            memo[i] = fib_current 
        return fib_current

n = 12
result = fibonacci_iterative_with_memoization(n)
print(f"The {n}-th Fibonacci number is: {result}")
