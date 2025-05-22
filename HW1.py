def der(a):
    b = []
    for i in range(1, len(a)):
        b.append(a[i] * i)
    return b


def pol(x, a):
    res = 0
    for i in range(len(a)):
        res += (x ** i) * a[i]
    return res


def step(x0):
    return x0 - pol(x0, a)/pol(x0, der(a))


def simple_step(xc, x0):
    return xc - pol(xc, a)/pol(x0, der(a))


def bin(x1, x2, e):
    if pol(x1, a) * pol(x2, a) < 0:
        while abs(x1 - x2) > e:
            x_n = (x1 + x2) / 2
            if pol(x1, a) * pol(x_n, a) < 0:
                x2 = x_n
            elif pol(x_n, a) * pol(x2, a) < 0:
                x1 = x_n

            elif pol(x1, a) * pol(x_n, a) == 0:
                return x_n

        return (x1+x2) / 2

    else:
        x1 -= 50
        x2 += 50


def Newton(x0, e):
    s = (step(x0) - x0) / (1 - (step(x0) - x0) / (x0 - step(x0)))
    while abs(s) > e:
        s = (step(x0) - x0)/(1 - (step(x0) - x0)/(x0 - step(x0)))
        x0 = step(x0)
    return x0


def easy_Newton(xc, e):
    s = (step(xc) - xc) / (1 - (step(xc) - xc) / (xc - step(xc)))
    while abs(s) > e:
        s = (step(xc) - xc)/(1 - (step(xc) - xc)/(xc - step(xc)))
        xc = simple_step(xc, x0)
    return xc


a = [-4, 0, 1]
x0 = 8
x1, x2 = 1, 3
e = 0.000000001
print(bin(x1, x2, e))
print(Newton(x0, e))
print(easy_Newton(x0, e))
