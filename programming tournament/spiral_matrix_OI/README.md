# Spiral Matrix

This program fills an `n × n` matrix with numbers from `1` to `n²` in a spiral pattern, starting from the outside and moving toward the center.

For example, for `n = 4`:

```text
1   2   3   4
12  13  14  5
11  16  15  6
10  9   8   7
```

## How it works

The easiest way to think about the program is:

**Go right → go down → go left → go up → repeat.**

We keep two variables:

```python
start = 0
end = n - 1
```

They tell us which part of the matrix we are currently filling.

For `n = 4`:

```text
start = 0
end = 3
```

So we start with the whole matrix.

### 1. Go right

Fill the top row from left to right:

```text
1  2  3  4
```

### 2. Go down

Then fill the right column from top to bottom:

```text
1  2  3  4
         5
         6
         7
```

### 3. Go left

Then fill the bottom row from right to left:

```text
1  2  3  4
         5
         6
10 9  8  7
```

### 4. Go up

Finally, go up along the left side:

```text
1   2   3   4
12          5
11          6
10  9   8   7
```

Now the outside layer is complete.

We move one step inward:

```python
start += 1
end -= 1
```

Then we repeat the same four movements for the smaller inner part.

Eventually, we reach the center.

## Main idea

The program does not try to calculate the exact position of every number.

Instead, it simply follows the spiral:

```text
→ → → →
      ↓
      ↓
← ← ← ←
↑
↑
```

Then it moves one layer inward and repeats.

## Input

The program asks for the size of the matrix:

```text
4
```

## Output

```text
1 2 3 4
12 13 14 5
11 16 15 6
10 9 8 7
```

## Algorithm

1. Create an empty `n × n` matrix.
2. Start `num` from `1`.
3. Fill the top row from left to right.
4. Fill the right column from top to bottom.
5. Fill the bottom row from right to left.
6. Fill the left column from bottom to top.
7. Move the boundaries inward.
8. Repeat until the matrix is full.
