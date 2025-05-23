import numpy as np

def gauss_seidel(A, b, x, tol=1.e-5, maxit=100):
    n = len(b)
    err = 1.0
    iters = 0
    xnew = np.zeros_like(x)

    while (err > tol and iters < maxit):
        iters += 1
    for i in range(n):
        s1 = np.dot(A[i, :i], xnew[:i])
        s2 = np.dot(A[i, i+1:], x[i+1:])
        xnew[i] = (b[i] - s1 - s2) / A[i, i]
    err = np.linalg.norm(xnew - x, np.inf)
    x = np.copy(xnew)
    print('Iteraciones necesarias para convergencia:', iters)
    return x