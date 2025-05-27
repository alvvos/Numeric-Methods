import math

def newton(f, df, xo, TOL, MAXIT, verbose):
    k = 0
    xk = xo
    if verbose:
        print("k\t x_k")
        print(f"{k}\t {xk}")
    error = TOL + 1
    while error > TOL and k < MAXIT:
        if (df(xk) != 0):
            xk_next = xk-((f(xk))/(df(xk)))
            error = abs(xk_next - xk)
            xk = xk_next
            k+=1
            if verbose:
                print(f"{k}\t {xk}")
    return xk

def f(x): return math.log(x) + x
def df(x): return 1/x + 1

x0 = 1
tol = 1e-4
maxit = 50

x_root = newton(f, df, x0, tol, maxit, True)
print("xk: ", x_root)
print("f(xk): ", f(x_root))