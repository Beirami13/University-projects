import time
import sys

sys.setrecursionlimit(100000)


def add(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def subtract(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C


def split(A):
    n = len(A)
    mid = n // 2
    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]
    return A11, A12, A21, A22


def merge(C11, C12, C21, C22):
    n = len(C11) * 2
    C = [[0 for _ in range(n)] for _ in range(n)]
    mid = n // 2

    for i in range(mid):
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]
    return C


def divide_conquer(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    A11, A12, A21, A22 = split(A)
    B11, B12, B21, B22 = split(B)

    C11 = add(divide_conquer(A11, B11), divide_conquer(A12, B21))
    C12 = add(divide_conquer(A11, B12), divide_conquer(A12, B22))
    C21 = add(divide_conquer(A21, B11), divide_conquer(A22, B21))
    C22 = add(divide_conquer(A21, B12), divide_conquer(A22, B22))

    return merge(C11, C12, C21, C22)


def multiply_strassen(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    A11, A12, A21, A22 = split(A)
    B11, B12, B21, B22 = split(B)

    M1 = multiply_strassen(add(A11, A22), add(B11, B22))
    M2 = multiply_strassen(add(A21, A22), B11)
    M3 = multiply_strassen(A11, subtract(B12, B22))
    M4 = multiply_strassen(A22, subtract(B21, B11))
    M5 = multiply_strassen(add(A11, A12), B22)
    M6 = multiply_strassen(subtract(A21, A11), add(B11, B12))
    M7 = multiply_strassen(subtract(A12, A22), add(B21, B22))

    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)

    return merge(C11, C12, C21, C22)


def read_matrix(n, name):
    print(f"\nMatrix {name} ({n}x{n}):")
    matrix = []
    for i in range(n):
        row = []
        while True:
            try:
                values = input(f"Row {i + 1}: ").strip().split()
                if len(values) != n:
                    print(f"Please enter {n} numbers!")
                    continue
                row = [int(x) for x in values]
                break
            except ValueError:
                print("Please enter valid integers!")
        matrix.append(row)
    return matrix

def print_matrix(matrix, name):
    print(f"\n{name}:")
    for row in matrix:
        print(" ".join(f"{x:8}" for x in row))

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def main():
    print("Matrix Multiplication: Divide & Conquer vs Strassen")
    while True:
        try:
            n = int(input("\nEnter matrix size (power of 2: 2, 4, 8, 16, 32, 64, 128, 256): "))
            if n < 2 or n > 256:
                print("Please enter a number between 2 and 256!")
                continue
            if not is_power_of_two(n):
                print("Please enter a power of 2 (2, 4, 8, 16, 32, 64, 128, 256)!")
                continue
            break
        except ValueError:
            print("Please enter a valid integer!")

    A = read_matrix(n, "A")
    B = read_matrix(n, "B")

    print("\nEntered matrices:")
    print_matrix(A, "Matrix A")
    print_matrix(B, "Matrix B")

    print("Method 1: Divide & Conquer")

    time_divide = 0
    start_time = time.perf_counter()
    C_divide = divide_conquer(A, B)
    end_time = time.perf_counter()
    time_divide = end_time - start_time

    print_matrix(C_divide, "Result (Divide & Conquer)")
    print(f"\nTime: {time_divide:.10f} seconds")

    print("\n" + "=" * 70)
    print("Method 2: Strassen")
    print("=" * 70)

    time_strassen = 0
    start_time = time.perf_counter()
    C_strassen = multiply_strassen(A, B)
    end_time = time.perf_counter()
    time_strassen = end_time - start_time

    print_matrix(C_strassen, "Result (Strassen)")
    print(f"\nTime: {time_strassen:.10f} seconds")

    print("\n" + "=" * 70)
    print("Final Report:")
    print("=" * 70)
    print(f"Matrix size: {n}x{n}")
    print(f"Divide & Conquer time: {time_divide:.10f} seconds")
    print(f"Strassen time: {time_strassen:.10f} seconds")

if __name__ == "__main__":
    main()