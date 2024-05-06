# 0x09-island_perimeter
![island](https://i.ytimg.com/vi/U9wr3eD3okc/maxresdefault.jpg)

# island🏝  🏝 🏝 🏝 🏝 🏝

```python
for i, row in enumerate(grid):
    for j, element in enumerate(row):
        # Check if element is land or sea
        if (element == 0):
            continue
```

This part consists of nested loops iterating over each element in the `grid`:

1. `for i, row in enumerate(grid):`: This loop iterates over each row (`row`) in the `grid`. `enumerate(grid)` provides both the index `i` and the actual row `row`.
   
2. `for j, element in enumerate(row):`: This inner loop iterates over each element (`element`) in the current row (`row`). `enumerate(row)` provides both the index `j` and the actual element `element`.

3. `if (element == 0): continue`: Within the inner loop, this condition checks if the current `element` is equal to 0, indicating it's water. If it is, `continue` skips the current iteration of the loop, moving on to the next element.

Moving on to the next part:

```python
# Left check
if (j != 0 and row[j - 1] == 0):
    total_perimeter += 1
if (j == 0):
    # left edge case
    total_perimeter += 1
```

1. This part checks the left side of the current element:

    a. `if (j != 0 and row[j - 1] == 0):`: This condition checks if the current element is not at the leftmost edge of the row (`j != 0`) and if the element to the left (`row[j - 1]`) is water (`== 0`). If both conditions are met, it means there is a boundary, so it increments the `total_perimeter` by 1.

    b. `if (j == 0):`: This condition handles the left edge case. If the current element is at the leftmost edge of the row (`j == 0`), it means there's a boundary, so it increments the `total_perimeter` by 1.

The code following checks the right, upper, and bottom sides of the current element in a similar fashion. Each section has similar conditions and actions for updating the `total_perimeter` variable.

Understanding these steps should provide a clear picture of how the code calculates the perimeter of the island.
