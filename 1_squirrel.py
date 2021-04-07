def squirrel(N):
    factorial = 1
    for i in range(1, N + 1):
        factorial *= i
    while(factorial != 0):
        emerald = factorial
        factorial = factorial // 10
    return emerald