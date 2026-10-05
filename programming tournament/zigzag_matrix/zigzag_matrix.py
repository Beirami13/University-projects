n = int(input())

matrix = [[0] * n for _ in range(n)]
num = 1

for s in range(2 * n - 1):
    for i in range(n):
        j = s - i

        if 0 <= j < n:
            if s % 2 == 0:
                matrix[j][i] = num
            else:
                matrix[i][j] = num
            num += 1

for row in matrix:
    print(*row)