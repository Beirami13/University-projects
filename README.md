# University Projects

Python coursework from my Computer Engineering degree at the University of Zanjan. The repository has two parts: assignments from the **Algorithm Design** course and problems I solved for **programming tournaments**.

## Contents

### 1. [Algorithm Design](AlgorithmDesign/README.md)

| Program | What it does | Technique |
|---------|--------------|-----------|
| `Naive vs. Strassen.py` | Multiplies two matrices with the divide-and-conquer method and with Strassen's algorithm, then compares the running time of both | Divide and conquer |
| `N_Queens.py` | Estimates the number of solutions of the N-Queens problem for a given board size and number of trials | Monte Carlo estimation |
| `tsp_dynamic_programming.py` | Finds the cheapest tour and the optimal path for the Traveling Salesman Problem | Dynamic programming with bitmasks (Held-Karp) |

### 2. Programming Tournaments

| Problem | What it does | Folder |
|---------|--------------|--------|
| Zigzag Matrix | Fills an `n × n` matrix with `1` to `n²` along diagonals in a zigzag order | [zigzag_matrix](programming%20tournament/zigzag_matrix/README.md) |
| Spiral Matrix | Fills an `n × n` matrix with `1` to `n²` in a spiral from the outside to the center | [spiral_matrix_OI](programming%20tournament/spiral_matrix_OI/README.md) |

Each tournament problem reads `n` from standard input and prints the matrix, so it can be used directly as a contest solution.

## Repository structure

```text
University-projects/
├── README.md
├── AlgorithmDesign/
│   ├── README.md
│   ├── Naive vs. Strassen.py
│   ├── N_Queens.py
│   └── tsp_dynamic_programming.py
└── programming tournament/
    ├── zigzag_matrix/
    │   ├── README.md
    │   └── zigzag_matrix.py
    └── spiral_matrix_OI/
        ├── README.md
        └── spiral_matrix_OI.py
```

## Requirements

- Python 3.x
- Standard library only (no packages to install)

## How to run

```bash
# Algorithm Design
python "AlgorithmDesign/Naive vs. Strassen.py"
python AlgorithmDesign/N_Queens.py
python AlgorithmDesign/tsp_dynamic_programming.py

# Programming tournaments
python "programming tournament/zigzag_matrix/zigzag_matrix.py"
python "programming tournament/spiral_matrix_OI/spiral_matrix_OI.py"
```

### Example

```text
$ python "programming tournament/zigzag_matrix/zigzag_matrix.py"
4
1 2 6 7
3 5 8 13
4 9 12 14
10 11 15 16
```

## What I practiced

- Divide and conquer, and why Strassen's method can beat the straightforward recursive approach on large matrices
- Estimating a hard counting problem with random sampling instead of full search
- Memoization and bitmask dynamic programming for an exponential problem
- Solving contest problems by finding the pattern in the indices instead of simulating by hand
- Measuring running time with `time.perf_counter()`

## Notes

- The matrix multiplication program accepts sizes that are powers of 2 (2, 4, 8, ..., 256) and asks you to type the matrix values.
- The TSP solution runs in about `O(n² · 2ⁿ)` time, so it is only practical for a small number of cities.
- N-Queens returns an estimate, so results change slightly between runs.