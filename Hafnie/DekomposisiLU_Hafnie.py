import numpy as np

def LU(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1

        for j in range(i, n):
            U[i][j] = A[i][j]
            for k in range(i):
                U[i][j] = U[i][j] - (L[i][k] * U[k][j])

        for j in range(i + 1, n):
            L[j][i] = A[j][i]
            for k in range(i):
                L[j][i] -= L[j][k] * U[k][i]
            L[j][i] /= U[i][i]

    return L, U

def Ly(L, b):
    n = len(L)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]

    return y

def Ux(U, y):
    n = len(U)
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for k in range(i + 1, n):
            x[i] -= U[i][k] * x[k]
        x[i] /= U[i][i]

    return x

# Meminta pengguna memasukkan ukuran matriks
n = int(input("Masukkan ukuran matriks (n x n): "))
A = np.zeros((n, n))
b = np.zeros(n)

# Meminta pengguna memasukkan elemen-elemen matriks A
print("Masukkan elemen-elemen matriks A:")
for i in range(n):
    for j in range(n):
        A[i][j] = float(input(f"A[{i}][{j}]: "))

# Meminta pengguna memasukkan elemen-elemen vektor b
print("Masukkan elemen-elemen vektor b:")
for i in range(n):
    b[i] = float(input(f"b[{i}]: "))

L, U = LU(A)
print("Matrix L:")
print(L)
print("Matrix U:")
print(U)

y = Ly(L, b)
print("Matrix y:")
print(y)

x = Ux(U, y)
print("Matriks x:")
print(x)
