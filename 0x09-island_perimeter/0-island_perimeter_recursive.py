#!/usr/bin/python3
""" Island perimeter solution
Create a function def island_perimeter(grid):
    that returns the perimeter of the island described in grid:

grid is a list of list of integers:
- 0 represents water
- 1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn't have “lakes” (water inside that isn't
connected to the water surrounding the island).

Approach:
    -find the first wall
        -> implementation in get_first_wall function
    - walk along the sides of the walls and measure length
        -> implementation in check_walls function
"""


def island_perimeter(grid):
    """ computes and return the perimeter of island in grid """
    sum = 0
    if not grid:
        return sum

    width = len(grid[0])
    height = len(grid)

    start_position = get_first_wall(grid, height, width)
    if not start_position:
        return sum
    start_row, start_col = start_position

    init_position = [start_row, start_col, False]

    first_square_prm = get_first_square_prm(grid, start_row,
                                            start_col, width - 1)
    other_blocks_prm = check_walls(
        grid, start_row, start_col, height - 1, width - 1, '0', init_position
    )
    if other_blocks_prm > 1:
        other_blocks_prm -= 1
    sum = first_square_prm + other_blocks_prm

    return sum


def get_first_wall(grid, height, width):
    """searches for first wall and returns its position"""
    for start_row in range(height):
        for start_col in range(width):
            if grid[start_row][start_col]:
                return start_row, start_col
    return None


def get_first_square_prm(grid, start_row, start_col, width):
    """ computes the perimeter of 1st square """
    perimeter = 3
    left = 0
    if width > start_col:
        left = grid[start_row][start_col + 1]

    if left:
        perimeter = 2

    return perimeter


def check_walls(grid, curr_row, curr_col, height, width, direction,
                start_position):
    """ walks along walls like a human would
    and counts each square face """
    sum = 0
    # print(curr_row, curr_col, direction)
    if [curr_row, curr_col, True] == start_position:
        return 0
    if (curr_row, curr_col) == (start_position[0], start_position[1]):
        start_position[2] = True

    if direction == '-y' or direction == '0':
        # check right
        if curr_col:
            if grid[curr_row][curr_col - 1]:
                sum = 0
                next_row = curr_row
                next_col = curr_col - 1
                direction = '-x'
                return sum + check_walls(
                    grid, next_row, next_col,
                    height, width, direction,
                    start_position
                )
        if height > curr_row:  # check ahead
            if grid[curr_row + 1][curr_col]:
                sum = 1
                next_row = curr_row + 1
                next_col = curr_col
                direction = '-y'
                return sum + check_walls(
                    grid, next_row, next_col,
                    height, width, direction,
                    start_position
                )
        if width > curr_col:  # check left
            if grid[curr_row][curr_col + 1]:
                sum = 2
                next_row = curr_row
                next_col = curr_col + 1
                direction = '+x'
                return sum + check_walls(
                    grid, next_row, next_col,
                    height, width, direction,
                    start_position
                )
        # u-turn
        if curr_row:
            if not grid[curr_row - 1][curr_col]:
                return 1
            sum = 3
            next_row = curr_row - 1
            next_col = curr_col
            direction = '+y'
            return sum + check_walls(
                grid, next_row, next_col,
                height, width, direction,
                start_position
            )
        else:
            return 1
    elif direction == '+x' or direction == '0':
        # check right
        if curr_row < height:
            if grid[curr_row + 1][curr_col]:
                sum = 0
                next_row = curr_row + 1
                next_col = curr_col
                direction = '-y'
                return sum + check_walls(
                    grid, next_row, next_col,
                    height, width, direction,
                    start_position
                )
        if width > curr_col:  # check ahead
            if grid[curr_row][curr_col + 1]:
                sum = 1
                next_row = curr_row
                next_col = curr_col + 1
                direction = '+x'
                return sum + check_walls(
                    grid, next_row, next_col,
                    height, width, direction,
                    start_position
                )
        if curr_row:  # check left
            if grid[curr_row - 1][curr_col]:
                sum = 2
                next_row = curr_row - 1
                next_col = curr_col
                direction = '+y'
                return sum + check_walls(
                    grid, next_row, next_col,
                    height, width, direction,
                    start_position
                )
        # u-turn
        if curr_col:
            if not grid[curr_row][curr_col - 1]:
                raise ValueError('prev wall must exist')
            sum = 3
            next_row = curr_row
            next_col = curr_col - 1
            direction = '-x'
            return sum + check_walls(
                grid, next_row, next_col,
                height, width, direction,
                start_position
            )
        else:
            raise ValueError('curr_col has to be > 0')
    elif direction == '+y' or direction == '0':
        # check right
        if width > curr_col:
            if grid[curr_row][curr_col + 1]:
                sum = 0
                next_row = curr_row
                next_col = curr_col + 1
                direction = '+x'
                return sum + check_walls(
                    grid, next_row, next_col,
                    height, width, direction,
                    start_position
                )
        if curr_row:  # check ahead
            if grid[curr_row - 1][curr_col]:
                sum = 1
                next_row = curr_row - 1
                next_col = curr_col
                direction = '+y'
                return sum + check_walls(
                    grid, next_row, next_col,
                    height, width, direction,
                    start_position
                )
        if curr_col:  # check left
            if grid[curr_row][curr_col - 1]:
                sum = 2
                next_row = curr_row
                next_col = curr_col - 1
                direction = '-x'
                return sum + check_walls(
                    grid, next_row, next_col,
                    height, width, direction,
                    start_position
                )
        # u-turn
        if curr_row < height:
            if not grid[curr_row + 1][curr_col]:
                raise ValueError('Not possible to not have value climbing \
                                    down after having climbed up')
            sum = 3
            next_row = curr_row + 1
            next_col = curr_col
            direction = '-y'
            return sum + check_walls(
                grid, next_row, next_col,
                height, width, direction,
                start_position
            )
        else:
            raise ValueError('curr_row must be less than height')
    elif direction == '-x' or direction == '0':
        # check right
        if curr_row:
            if grid[curr_row - 1][curr_col]:
                sum = 0
                next_row = curr_row - 1
                next_col = curr_col
                direction = '+y'
                return sum + check_walls(
                    grid, next_row, next_col,
                    height, width, direction,
                    start_position
                )
        if curr_col:  # check ahead
            if grid[curr_row][curr_col - 1]:
                sum = 1
                next_row = curr_row
                next_col = curr_col - 1
                direction = '-x'
                return sum + check_walls(
                    grid, next_row, next_col,
                    height, width, direction,
                    start_position
                )
        if curr_row < height:  # check left
            if grid[curr_row + 1][curr_col]:
                sum = 2
                next_row = curr_row + 1
                next_col = curr_col
                direction = '-y'
                return sum + check_walls(
                    grid, next_row, next_col,
                    height, width, direction,
                    start_position
                )
        # u-turn
        if curr_col < width:
            if not grid[curr_row][curr_col + 1]:
                raise ValueError('curr_col has to be less than width')
            sum = 3
            next_row = curr_row
            next_col = curr_col + 1
            direction = '+x'
            return sum + check_walls(
                grid, next_row, next_col,
                height, width, direction,
                start_position
            )
        else:
            raise ValueError('curr_col has to be < width')
    elif direction not in ['+x', '-x', '+y', '-y']:
        raise ValueError('wrong direction')

    raise ValueError('Could not walk along the walls :)')


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
    assert (island_perimeter(grid) == 12)

    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
    assert (island_perimeter(grid) == 16)

    grid = [
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]
    ]
    print(island_perimeter(grid))
    assert (island_perimeter(grid) == 22)

    grid = [
        [0, 0, 1, 1, 1, 1],
        [0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]
    ]
    print(island_perimeter(grid))
    assert (island_perimeter(grid) == 26)

    grid = [
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
    assert (island_perimeter(grid) == 4)

    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1]
    ]
    print(island_perimeter(grid))
    assert (island_perimeter(grid) == 4)

    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
    assert (island_perimeter(grid) == 4)

    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
    assert (island_perimeter(grid) == 6)

    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
    assert (island_perimeter(grid) == 0)

    grid = [
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
    assert (island_perimeter(grid) == 4)

    grid = [
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
    assert (island_perimeter(grid) == 4)

    grid = [
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
    assert (island_perimeter(grid) == 4)

    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1]
    ]
    print(island_perimeter(grid))
    assert (island_perimeter(grid) == 20)
