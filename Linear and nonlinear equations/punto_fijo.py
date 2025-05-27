def punto_fijo(g, x0, tol=1.0e-6, maxit=100, verbose=True):
    k = 0
    error = tol + 1
    xk = x0

    if verbose:
        print("k\t x_k")
        print(f"{k}\t {xk}")
    while error > tol and k <= maxit:
        xk_next = g(xk)
        error = abs(xk_next - xk)
        xk = xk_next
        k += 1
        if verbose:
            print(f"{k}\t {xk}")
    return xk


def f(x):
    return x**2 - x - 1.0


def g(x):
    return x**2 - 1


x0 = 2
tol = 1e-4
maxit = 50

x_root = punto_fijo(g, x0, tol, maxit)

print("xk: ", x_root)
print("f(xk): ", f(x_root))
