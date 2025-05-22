def func(x, a):
    res = 0
    for i in range(len(a)):
        res += (x ** i) * a[i]
    return res


def step(x0, x1, a):
    funca = func(x0, a)
    res = x0 - ((x1 - x0)*funca/(func(x1, a) - funca)) * c
    return res


def Sec(x0, x1, e):
    for i in range(max_iters):
        Fx0 = func(x0, a)
        Fx1 = func(x1, a)
        x_n = x0 - Fx0 * (x1 - x0) / (Fx1 - Fx0)
        if func(x0, a) * func(x_n, a) < 0:
            x1 = x_n
        elif func(x_n, a) * func(x1, a) < 0:
            x0 = x_n
        elif func(x0, a) * func(x_n, a) == 0:
            return x_n
    return x_n

a = [-2, 0, 1]
x0 = 1
x1 = 2
e = 0.000000001
c = 0.7
max_iters = 10000
ans = Sec(x0, x1, e)
print('x через хорды:', ans)
print(f'При x = {ans}, y = {func(ans, a):.20f}')
print()


def R(fx):
    if fx[0] <= 0:
        return 'a0 должно быть положительным'
    temp = []
    flag = False
    for i in range(len(fx)):
        if fx[i] < 0 and flag==False:
            k = i
            flag = True
        elif fx[i] < 0:
            temp.append(-1 * fx[i])
    temp.append(-1*fx[k])
    temp.sort()
    return 1 + (temp[-1]/fx[0])**(1/k)

def R1(fx):
    fxn = fx[::-1]
    if fxn[0] <= 0:
        for i in range(len(fxn)):
            fxn[i] *= (-1)
    temp = []
    flag = False
    for i in range(len(fxn)):
        if fxn[i] < 0 and flag==False:
            k = i
            flag = True
        elif fxn[i] < 0:
            temp.append(-1 * fxn[i])
    temp.append(-1*fxn[k])
    temp.sort()
    return 1 + (temp[-1]/fxn[0])**(1/k)


def R2(fx):
    fxn = fx
    if len(fxn) % 2 == 0: t = 0
    else: t = 1
    for i in range(t, len(fxn), 2):
        fxn[i] *= (-1)
    if fxn[0] <= 0:
        for i in range(len(fxn)):
            fxn[i] *= (-1)
    temp = []
    flag = False
    for i in range(len(fxn)):
        if fxn[i] < 0 and flag == False:
            k = i
            flag = True
        elif fxn[i] < 0:
            temp.append(-1 * fxn[i])
    temp.append(-1 * fxn[k])
    temp.sort()
    return 1 + (temp[-1]/fxn[0])**(1/k)


def R3(fx):
    fxn = fx[::-1]
    if fxn[0] <= 0:
        for i in range(len(fxn)):
            fxn[i] *= (-1)
    temp = []
    flag = False
    for i in range(len(fxn)):
        if fxn[i] < 0 and flag == False:
            k = i
            flag = True
        elif fxn[i] < 0:
            temp.append(-1 * fxn[i])
    temp.append(-1 * fxn[k])
    temp.sort()
    return 1 + (temp[-1]/fxn[0])**(1/k)


fxs = [1, 2, -5, 8, -7, -3]
print(f'{1/R1(fxs)} <= положительный х <= {R(fxs)}')
print(f'{-1*R2(fxs)} <= отрицательны х <= {-1/R3(fxs)}')
