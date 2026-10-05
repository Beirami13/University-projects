n = int(input())

matrix = [[0] * n for _ in range(n)]
num = 1

start = 0
end = n - 1

while start <= end:

    for j in range(start, end + 1):
        matrix[start][j] = num
        num += 1

    for i in range(start + 1, end + 1):
        matrix[i][end] = num
        num += 1

    for j in range(end - 1, start - 1, -1):
        matrix[end][j] = num
        num += 1

    for i in range(end - 1, start, -1):
        matrix[i][start] = num
        num += 1

    start += 1
    end -= 1

for row in matrix:
    print(*row)