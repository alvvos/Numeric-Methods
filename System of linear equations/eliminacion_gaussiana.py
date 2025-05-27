import numpy as np


def gauss_elimination(A, b):
    n = len(b)
    assert A.shape == (n, n)
    # Eliminación Gaussiana
    for k in range(n - 1):
        for i in range(k + 1, n):
            if A[k, k] != 0:
                # Fi - mik * Fk -> Fi
                mik = A[i, k] / A[k, k]
                # A[i, k] = 0 # No es necesario almacenar los 0's
                A[i, k + 1 : n] = A[i, k + 1 : n] - mik * A[k, k + 1 : n]
                b[i] = b[i] - mik * b[k]
            else:
                print(f"División por cero en el paso {k} de la eliminación Gaussiana.")
                return None
        if A[n - 1, n - 1] == 0:
            print("Matriz singular.")
            return None

    # Sustitución Regresiva
    for k in range(n - 1, -1, -1):
        # x = np.zeros_like(b)
        # x[k] = (b[k] - np.dot(A[k, k+1:n], x[k+1:n])) / A[k, k]
        # Podemos utilizar el propio vector b para guardar los xk
        b[k] = (b[k] - np.dot(A[k, k + 1 : n], b[k + 1 : n])) / A[k, k]

    return b


if __name__ == "__main__":
    # A = np.array([[1.0, 1.0, 0.0], [2.0, 1.0, -1.0], [3.0, -1.0, -1.0]])
    # b = np.array([2.0, 2.0, 1.0]) 

    # x_sol = gauss_elimination(A.copy(), b.copy())

    # print("Vector solución x: ", x_sol)

    A = np.array([[0.49 * 1.0e-17, 0.51 * 1.0e-17], [1.0, 1.0]])
    b = np.array([1.0e-17, 2.0])
    x = gauss_elimination(A, b)
    print(x)
