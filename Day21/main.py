# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1 = part1(data)
    part1_time = time.time()
    answer2 = part2(data)
    part2_time = time.time()

    print("---------------------------------------------------")
    print(f"Part 1 Answer: {answer1}")
    print()
    print(f"Part 2 Answer: {answer2}")
    print()
    print(f"Data Parse Execution Time: {1000*(parse_time - start_time):.2f} ms")
    print(f"Part 1 Execution Time:     {1000*(part1_time - parse_time):.2f} ms")
    print(f"Part 2 Execution Time:     {1000*(part2_time - part1_time):.2f} ms")
    print(f"Total Execution Time:      {1000*(part2_time - start_time):.2f} ms")
    print("---------------------------------------------------")


output = False  # Toggle this flag to enable/disable prints
def debug_print(*args, **kwargs):
    if output:
        print(*args, **kwargs)


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.readlines()

    replacements = {}
    for line in data:
        parts = line.strip().split(" => ")
        rotations = possibles(parts[0])
        for rotation in rotations:
            replacements[rotation] = parts[1]

    return replacements


def possibles(pattern):

    patterns = set()
    grid = [list(row) for row in pattern.split("/")]
    for _ in range(4):
        new_pattern = "/".join("".join(row) for row in grid)
        patterns.add(new_pattern)
        new_pattern = "/".join("".join(row[::-1]) for row in grid)
        patterns.add(new_pattern)
        new_pattern = "/".join("".join(row) for row in grid[::-1])
        patterns.add(new_pattern)
        grid = [list(row) for row in zip(*grid[::-1])]

    return patterns 


def reconstruct(grid):
    size = len(grid)
    line_size = int(size ** (0.5))
    interior_size = len(grid[0])

    if size == 1:
        return grid[0]

    else:
        lines = {}
        new_grid = []

        for v in range(line_size):
            for q in range(interior_size):
                lines[f"line{q}"] = ""
            
            for q in range(line_size*v,line_size*(v+1)):
                for z in range(interior_size):
                    lines[f"line{z}"] += grid[q][z]

            for z in range(interior_size):
                new_grid.append(lines[f"line{z}"])

        return new_grid


def part1(data):

    grid = [".#.","..#","###"]

    for _ in range(5):
        size = len(grid)
        if size % 2 == 0:
            new_grid = []
            for i in range(0,len(grid),2):
                for j in range(0,len(grid),2):
                    starting_grid = f"{grid[i][j:j+2]}/{grid[i+1][j:j+2]}"
                    for line in data:
                        if starting_grid == line:
                            new_grid.append([row for row in data[line].split("/")])
                            break
            grid = reconstruct(new_grid)
                    
        else:
            new_grid = []
            for i in range(0,len(grid),3):
                for j in range(0,len(grid),3):
                    starting_grid = f"{grid[i][j:j+3]}/{grid[i+1][j:j+3]}/{grid[i+2][j:j+3]}"
                    for line in data:
                        if starting_grid == line:
                            new_grid.append([row for row in data[line].split("/")])
                            break
            grid = reconstruct(new_grid)

    return sum(1 for row in grid for char in row if char == "#")


def part2(data):
    grid = [".#.","..#","###"]

    for _ in range(18):
        size = len(grid)
        if size % 2 == 0:
            new_grid = []
            for i in range(0,len(grid),2):
                for j in range(0,len(grid),2):
                    starting_grid = f"{grid[i][j:j+2]}/{grid[i+1][j:j+2]}"
                    for line in data:
                        if starting_grid == line:
                            new_grid.append([row for row in data[line].split("/")])
                            break
            grid = reconstruct(new_grid)
                    
        else:
            new_grid = []
            for i in range(0,len(grid),3):
                for j in range(0,len(grid),3):
                    starting_grid = f"{grid[i][j:j+3]}/{grid[i+1][j:j+3]}/{grid[i+2][j:j+3]}"
                    for line in data:
                        if starting_grid == line:
                            new_grid.append([row for row in data[line].split("/")])
                            break
            grid = reconstruct(new_grid)


    return sum(1 for row in grid for char in row if char == "#")


if __name__ == "__main__":
    main()