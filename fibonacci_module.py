def generate_fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(sum(fib_series[-2:]))
    return fib_series
