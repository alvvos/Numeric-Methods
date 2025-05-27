import numpy as np

def solve_lu(LU, b):
    n = LU.shape[0]
    b = b.copy().astype(float)

    # Paso 1: Sustitución hacia adelante (Ly = b)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - np.dot(LU[i, :i], y[:i])
        # L[i, i] se asume 1, así que no se divide

    # Paso 2: Sustitución hacia atrás (Ux = y)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(LU[i, i + 1:], x[i + 1:])) / LU[i, i]

    return x
