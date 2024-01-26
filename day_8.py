import input

lines = input.read_argv()
grid = [[int(x) for x in list(line)] for line in lines.strip().split()]
print(grid)


def visible_trees(grid: list[list[int]]):
    visible_count = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            tree = grid[i][j]
            if (
                all(tree > grid[i][k] for k in range(j - 1, -1, -1))
                or all(tree > grid[i][k] for k in range(j + 1, len(grid[i])))
                or all(tree > grid[k][j] for k in range(i - 1, -1, -1))
                or all(tree > grid[k][j] for k in range(i + 1, len(grid)))
            ):
                visible_count += 1
    return visible_count + ((len(grid) * 2) + len(grid[0] * 2) - 4)


def scenic_score(tree: int, position: tuple[int, int], grid: list[list[int]]):
    i, j = position
    left = right = up = down = 0

    for k in range(j - 1, -1, -1):
        left += 1
        if grid[i][k] >= tree:
            break
    for k in range(j + 1, len(grid[i])):
        right += 1
        if grid[i][k] >= tree:
            break
    for k in range(i - 1, -1, -1):
        up += 1
        if grid[k][j] >= tree:
            break
    for k in range(i + 1, len(grid)):
        down += 1
        if grid[k][j] >= tree:
            break
    return left * right * up * down


def max_scenic_score(grid: list[list[int]]):
    max_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            score = scenic_score(grid[i][j], (i, j), grid)
            if score > max_score:
                max_score = score
    return max_score


def silver():
    return visible_trees(grid)


def gold():
    return max_scenic_score(grid)


print("silver:", silver())
print("gold:", gold())
