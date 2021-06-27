import math

def goldenSection(a, b, tol):
    r = (-1.0 + math.sqrt(5)) / 2
    x = a + r * (b - a)
    y = b - r * (b - a)
    u = f(x)
    v = f(y)
    while abs((b - a)) > tol:
        if u > v:
            b = x
            x = y
            u = v
            y = b - r * (b - a)
            v = f(y)
        else:
            a = y
            y = x
            v = u
            x = a + r * (b - a)
            u = f(x)
    print((a + b) / 2)
    print(f((a + b) / 2))


def f(x):
    #return 2*x**3 + 3*x**2 - 12*x + 4
    #return math.exp(-x) * math.cos(x)
    return x**4 - 6 * x**3 + 30 * x - 4


goldenSection(-3, 2, 10**-10)