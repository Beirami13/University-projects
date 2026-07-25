import random

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def count_children(board, row, n):
    count = 0
    for col in range(n):
        if is_safe(board, row, col):
            count += 1
    return count


def monte_carlo(n, trials):
    total = 0
    for _ in range(trials):
        board = [-1] * n
        level = 0
        estimate = 1
        while level < n:
            children = count_children(board, level, n)
            if children == 0:
                break
            estimate *= children
            choices = []
            for col in range(n):
                if is_safe(board, level, col):
                    choices.append(col)
            board[level] = choices[random.randint(0, len(choices) - 1)]
            level += 1
        total += estimate
    return total / trials

n = int(input())
trials = int(input())

print(monte_carlo(n, trials))