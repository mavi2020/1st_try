def fibonaci(n):
    if n==0:
        return 0
    elif n == 1:
        return 1

    return fibonaci(n-1) + fibonaci(n-2)

print(fibonaci(2))