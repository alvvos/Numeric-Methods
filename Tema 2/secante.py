import math


def secante(f, x1, x2, tol=1.0e-6, maxit=100, verbose=True):
    k = 0
    xk = x2
    xk_prev = x1

    error = abs(xk - xk_prev)

    if verbose:
        print("k\t x_k")
        print(f"{k - 1}\t {xk_prev}")
        print(f"{k}\t {xk}")

    while error > tol and k <= maxit:
        fxk = f(xk)
        fxkprev = f(xk_prev)

        x_new = xk - fxk * (xk - xk_prev) / (fxk - fxkprev)

        k += 1
        xk_prev = xk
        xk = x_new
        # xk_prev, xk = xk, xk - fxk * (xk - xk_prev) / (fxk - fxkprev)
        error = abs(xk - xk_prev)

        if verbose:
            print(f"{k}\t {xk}")
    return xk


def f(x):
    return math.log(x) + x


x1 = 1.0
x2 = 2.0
tol = 1e-4
maxit = 50

x_root = secante(f, x1, x2, tol, maxit)

print("xk: ", x_root)
print("f(xk): ", f(x_root))
