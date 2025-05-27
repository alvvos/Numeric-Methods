def jacobi(A, b, x, tol=1.e-5, maxit=100):
    d = np.copy(np.diag(A))
    np.fill_diagonal(A, 0.0)
    err = 1.0
    iters = 0
    while (err > tol and iters < maxit):
        iters += 1
        xnew = (b - np.dot(A, x)) / d
        err = np.linalg.norm(xnew - x, np.inf)
        x = np.copy(xnew)
    print('Iteraciones necesarias para convergencia:', iters)
    return x