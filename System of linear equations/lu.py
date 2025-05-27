import numpy as np

def lu_factorization(A):
    A = A.copy().astype(float)  # Asegurarse de trabajar con float y no modificar el original
    n = A.shape[0]
    assert A.shape[0] == A.shape[1], "La matriz A debe ser cuadrada"
    
    L = np.eye(n)  # Matriz identidad para L
    U = np.zeros((n, n))  # Matriz vacía para U

    for k in range(n):
        if A[k, k] == 0:
            raise ValueError(f"Pivote cero en la fila {k}, no se puede continuar sin pivoteo")
        
        U[k, k:] = A[k, k:]  # Rellenar fila k de U

        for i in range(k + 1, n):
            L[i, k] = A[i, k] / A[k, k]  # Guardar multiplicador en L
            A[i, k:] = A[i, k:] - L[i, k] * A[k, k:]  # Eliminar de la fila i

    return L, U
