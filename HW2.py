def deriv(a):
    b = []
    for i in range(1, len(a)):
        b.append(a[i] * i)
    return b


def g(x0):
    return (x0**2 + 6) / 5


def pol(x, a):
    res = 0
    for i in range(len(a)):
        res += (x ** i) * a[i]
    return res


def step(x0):
    return x0 - pol(x0, a) / pol(x0, deriv(a)) * c


def Newton_Broid(x0, e):
    a = 0
    while a < 10000:
        s = (step(x0) - x0)/(1 - (step(x0) - x0) / (x0 - step(x0)))
        if abs(s) < e:

            print(f"Корень: {x0}, итераций: {a}")
            return x0
        a += 1
        x0 = step(x0)
    raise ValueError("Превышен лимит итерация. Корень не найден")


def Sec(x0, x1, e):
    for i in range(max_iter):
        Fx0 = pol(x0, a)
        Fx1 = pol(x1, a)
        if abs(Fx1) < e:
            print(f"Корень: {x1}, итераций: {i}")
            return x1

        xN = x1 - Fx1 * (x1 - x0) / (Fx1 - Fx0)
        x0, x1 = x1, xN
    raise ValueError("Превышен лимит итерация. Корень не найден")

def Iter(x0, e, max_iters):
    for i in range(max_iter):
        x_n = g(x0)
        if abs(x_n - x0) < e:
            print(f"Корень: {x_n}, итераций: {i}")
            return x_n
        x0 = x_n
    raise ValueError("Превышен лимит итерация. Корень не найден")


a = [-4, 0, 1]
x0 = 1
x1 = 1.25
e = 0.000000001
c = 0.7
max_iter = 1000
print(Newton_Broid(x0, e))
print(Sec(x0, x1, e))
print(Iter(x0, e, max_iter))
