def simple_fib(n: int) -> int:

    a, b = 0, 1

    for _ in range(n):
        a, b = a + b, a

    return a


print(simple_fib(10))
