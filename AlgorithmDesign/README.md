# Advanced Algorithms

A collection of algorithm implementations in Python for optimization and computational problems.

## Projects

### 1. Matrix Multiplication (Divide & Conquer vs Strassen)
Comparison of two matrix multiplication methods:
- **Divide & Conquer** method
- **Strassen** method

Accepts matrix sizes that are powers of 2 and displays execution time.

### 2. N-Queens Problem (Monte Carlo)
Estimates the number of solutions for the N-Queens problem using the Monte Carlo method. Inputs:
- n: chessboard size
- trials: number of simulation runs

### 3. Traveling Salesman Problem (TSP)
Solves TSP using Dynamic Programming and displays the optimal path.

Example with 4 cities:
- Path: 0 → 1 → 3 → 2 → 0
- Optimal cost: 80

## Technologies
- Python 3.x
- Standard library only

## Run
```bash
# Matrix Multiplication
python "Naive vs. Strassen.py"

# N-Queens
python N_Queens.py

# TSP
python tsp_dynamic_programming.py
