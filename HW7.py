def jacobi_2x2(A):
    if A.shape != (2, 2):
        raise ValueError("Matrix must be 2x2")
    if not np.allclose(A, A.T):
        raise ValueError("Matrix must be symmetric")

    if abs(A[0, 1]) < 1e-12:
        eigenvalues = [A[0, 0], A[1, 1]]
        eigenvectors = np.eye(2)
        return eigenvalues, eigenvectors

    theta = 0.5 * np.arctan2(2 * A[0, 1], A[0, 0] - A[1, 1])
    c, s = np.cos(theta), np.sin(theta)

    R = np.array([[c, -s], [s, c]])
    D = R.T @ A @ R

    eigenvalues = [D[0, 0], D[1, 1]]
    eigenvectors = R
    return eigenvalues, eigenvectors


A2 = np.array([[3.0, 2.0],
               [2.0, 4.0]])
vals2, vecs2 = jacobi_2x2(A2)
tol = 1e-8
print("\n2x2 Eigenvalues:", vals2)
print("2x2 Eigenvectors:\n", vecs2)
n = len(vals2)
for i in range(n):
    v = vecs2[:, i]
    λ = vals2[i]
    residual = np.linalg.norm(A2 @ v - λ * v)
    status = "OK" if residual < tol else "FAIL"
    print(f"λ = {λ:.6f}, |Av - λv| = {residual:.2e} → {status}")

def jacobi_nxn(A, eps=1e-10, max_iter=100):
    if not np.allclose(A, A.T):
        raise ValueError("Matrix must be symmetric")

    n = A.shape[0]
    V = np.eye(n)
    A = A.copy()

    for _ in range(max_iter):
        max_val = 0
        p, q = 0, 1
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i, j]) > max_val:
                    max_val = abs(A[i, j])
                    p, q = i, j

        if max_val < eps:
            break

        if A[p, p] == A[q, q]:
            angle = np.pi / 4
        else:
            angle = 0.5 * np.arctan2(2 * A[p, q], A[p, p] - A[q, q])

        c, s = np.cos(angle), np.sin(angle)
        R = np.eye(n)
        R[p, p] = c
        R[q, q] = c
        R[p, q] = -s
        R[q, p] = s

        A = R.T @ A @ R
        V = V @ R

    eigenvalues = np.diag(A)
    eigenvectors = V
    return eigenvalues, eigenvectors

A3 = np.array([[4.0, 1.0, 1.0],
               [1.0, 3.0, 0.0],
               [1.0, 0.0, 2.0]])
vals3, vecs3 = jacobi_nxn(A3)
print("\n3x3 Eigenvalues:", vals3)
print("3x3 Eigenvectors:\n", vecs3)
n = len(vals3)
for i in range(n):
    v = vecs3[:, i]
    λ = vals3[i]
    residual = np.linalg.norm(A3 @ v - λ * v)
    status = "OK" if residual < tol else "FAIL"
    print(f"λ = {λ:.6f}, |Av - λv| = {residual:.2e} → {status}")
