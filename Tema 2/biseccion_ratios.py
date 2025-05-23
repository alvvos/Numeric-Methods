from math import log


def ratios_biseccion(f, a, b, tol=1.0e-6):
    errores = []
    if f(a) * f(b) == 0.0:
        if f(a) == 0.0:
            return a
        else:
            return b
    if f(a) * f(b) > 0.0:
        print("ERROR: LA FUNCION TIENE EL MISMO SIGNO EN a y b")
        return None

    k = -1
    print("k\t x_k \t\t r")
    while abs(b - a) > tol:
        errores.append(abs(b - a))
        k += 1
        xk = (a + b) / 2

        if f(a) * f(xk) < 0.0:
            b = xk
        elif f(b) * f(xk) < 0.0:
            a = xk
        else:
            break
        if len(errores) >= 3:
            e3 = errores[-1]
            e2 = errores[-2]
            e1 = errores[-3]
            ratio = log(e2 / e3) / log(e1 / e2)
            errores.pop(0)
            print(f"{k}\t {xk:.10f} \t {ratio}")

    return xk


# def f(x):
#     y = log(x) + x
#     return y

f = lambda x: log(x) + x
a = 0.1
b = 1.0
tol = 1.0e-4

x_root = ratios_biseccion(f, a, b, tol)

if x_root is not None:
    print("xk: ", x_root)
    print("f(xk): ", f(x_root))
