def countNegatives(grid):
    m = len(grid)
    n = len(grid[0])

    row = 0
    col = n - 1
    count = 0

    while row < m and col >= 0:
        if grid[row][col] < 0:
            count += m - row
            col -= 1
        else:
            row += 1

    return count
grid = [
    [4, 3, 2, -1],
    [3, 2, 1, -1],
    [1, 1, -1, -2],
    [-1, -1, -2, -3]
]
answer = countNegatives(grid)
print("Number of negative values:", answer)
