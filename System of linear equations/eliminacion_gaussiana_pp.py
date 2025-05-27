import numpy as np


def intercambiar_filas(v, i, j):
    if len(v.shape) == 1:
        v[i], v[j] = v[j], v[i]
    else:
        v[[i, j], :] = v[[j, i], :]


def gauss_elimination(A, b, tol=1.0e-15):
    n = len(b)
    assert A.shape == (n, n)
    # Eliminación Gaussiana con Pivotaje Parcial
    for k in range(n - 1):
        # Pivotaje Parcial
        p = np.argmax(A[k:n, k]) + k
        if np.abs(A[p, k]) < tol:  # Distinto de cero "numéricamente"
            print("Pivote tras pivotaje parcial (casi) cero")
            return None
        if p != k:
            intercambiar_filas(A, p, k)
            intercambiar_filas(b, p, k)
        # Eliminación Gaussiana
        for i in range(k + 1, n):
            # Fi - mik * Fk -> Fi
            mik = A[i, k] / A[k, k]
            # A[i, k] = 0 # No es necesario almacenar los 0's
            A[i, k + 1 : n] = A[i, k + 1 : n] - mik * A[k, k + 1 : n]
            b[i] = b[i] - mik * b[k]

        if np.abs(A[n - 1, n - 1]) < tol:  # Distinto de cero "numéricamente"
            print("Pivote tras pivotaje parcial (casi) cero")
            return None
    # Sustitución Regresiva
    for k in range(n - 1, -1, -1):
        # x = np.zeros_like(b)
        # x[k] = (b[k] - np.dot(A[k, k+1:n], x[k+1:n])) / A[k, k]
        # Podemos utilizar el propio vector b para guardar los xk
        b[k] = (b[k] - np.dot(A[k, k + 1 : n], b[k + 1 : n])) / A[k, k]

    return b


if __name__ == "__main__":
    A = np.array([[1.0, 1.0, 0.0], [2.0, 1.0, -1.0], [3.0, -1.0, -1.0]])
    b = np.array([2.0, 2.0, 1.0])

    x_sol = gauss_elimination(A.copy(), b.copy())

    print("Vector solución x: ", x_sol)
