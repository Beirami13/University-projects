# Zigzag Matrix

Fills an `n × n` matrix with numbers from `1` to `n²` in a zigzag diagonal pattern.

For `n = 4`:

```text
1   2   6   7
3   5   8   13
4   9   12  14
10  11  15  16
```

## How it works

The matrix is filled diagonal by diagonal.

For every cell:

```text
i + j = s
```

where `s` represents the current diagonal.

The direction changes for each diagonal:

```text
→
←
→
←
```

For even diagonals, `i` and `j` are swapped to reverse the direction.

## Input

```text
4
```

## Output

```text
1 2 6 7
3 5 8 13
4 9 12 14
10 11 15 16
```
