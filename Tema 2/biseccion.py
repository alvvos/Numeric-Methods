from math import log


def biseccion(f, a, b, tol=1.0e-6, verbose=False):
    if f(a) * f(b) == 0.0:
        if f(a) == 0.0:
            return a
        else:
            return b
    if f(a) * f(b) > 0.0:
        print("ERROR: LA FUNCION TIENE EL MISMO SIGNO EN a y b")
        return None

    k = -1
    if verbose:
        print("k\t x_k")
    while abs(b - a) > tol:
        k += 1
        xk = (a + b) / 2
        if verbose:
            print(f"{k}\t {xk}")
        if f(a) * f(xk) < 0.0:
            b = xk
        elif f(b) * f(xk) < 0.0:
            a = xk
        else:
            break
    return xk


# def f(x):
#     y = log(x) + x
#     return y

f = lambda x: log(x) + x
a = 0.1
b = 1.0
tol = 1.0e-4

x_root = biseccion(f, a, b, tol, verbose=True)

if x_root is not None:
    print("xk: ", x_root)
    print("f(xk): ", f(x_root))
