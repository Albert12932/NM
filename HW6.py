import numpy as np

def jacobi_rotation_method(A, eps=1e-10, max_iter=100):
    n = A.shape[0]
    V = np.eye(n)

    for _ in range(max_iter):
        i, j = np.unravel_index(np.argmax(np.abs(np.triu(A, 1))), A.shape)
        if abs(A[i, j]) < eps:
            break

        if A[i, i] == A[j, j]:
            theta = np.pi / 4
        else:
            theta = 0.5 * np.arctan(2 * A[i, j] / (A[i, i] - A[j, j]))

        cos = np.cos(theta)
        sin = np.sin(theta)

        R = np.eye(n)
        R[i, i] = cos
        R[j, j] = cos
        R[i, j] = -sin
        R[j, i] = sin

        A = R.T @ A @ R
        V = V @ R

    eigenvalues = np.diag(A)
    eigenvectors = V
    return eigenvalues, eigenvectors

A = np.array([[5, 1, 2],
              [1, 4, 1],
              [2, 1, 3]])

print("Исходная матрица:")
print(A)

eigenvalues, eigenvectors = jacobi_rotation_method(A)

print("\nСобственные значения: ")
print(eigenvalues)

print("\nСобственные векторы (в столбцах): ")
print(eigenvectors)
