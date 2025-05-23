import numpy as np

def gauss_elimination(A, b, verbose=True):
    A = A.astype(float).copy()
    b = b.astype(float).copy()
    n = len(b)
    assert A.shape == (n, n)

    if verbose:
        print("Matriz aumentada inicial:")
        print(np.hstack((A, b.reshape(-1, 1))))
        print()

    # Eliminación Gaussiana
    for k in range(n - 1):
        if A[k, k] == 0:
            print(f"División por cero en el paso {k} de la eliminación Gaussiana.")
            return None

        for i in range(k + 1, n):
            mik = A[i, k] / A[k, k]
            A[i, k + 1 : n] -= mik * A[k, k + 1 : n]
            A[i, k] = 0.0  # Hacer explícito el 0 para claridad
            b[i] -= mik * b[k]

            if verbose:
                print(f"Paso {k}, Fila {i}: F{i} - ({mik:.3e}) * F{k} -> F{i}")
                print("Matriz aumentada:")
                print(np.hstack((A, b.reshape(-1, 1))))
                print()

    if A[n - 1, n - 1] == 0:
        print("Matriz singular.")
        return None

    # Sustitución Regresiva
    for k in range(n - 1, -1, -1):
        b[k] = (b[k] - np.dot(A[k, k + 1 : n], b[k + 1 : n])) / A[k, k]
        if verbose:
            print(f"Sustitución hacia atrás en x[{k}]:")
            print(f"x[{k}] = {b[k]:.6f}")
            print()

    return b


if __name__ == "__main__":
    A = np.array([[0.49 * 1.0e-17, 0.51 * 1.0e-17], [1.0, 1.0]])
    b = np.array([1.0e-17, 2.0])
    x = gauss_elimination(A, b, verbose=True)
    print("Vector solución x:", x)
