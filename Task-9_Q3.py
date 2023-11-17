from functools import reduce
# Number of elements in Fibonacci series
n = 50
#Fibonacci series using lambda and map
fibonacci_series = list(map(lambda x: reduce(lambda a, _: a + [a[-2] + a[-1]], range(x - 2), [0, 1]), range(2, n + 1)))
print(f"Fibonacci series with {n} elements:")
print(fibonacci_series)
