# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
from collections import defaultdict
from copy import deepcopy


def main():
    start_time = time.time()

    data, center = parse_data()
    parse_time = time.time()

    part2_data = deepcopy(data)

    answer1 = part1(data, center)
    part1_time = time.time()
    answer2 = part2(part2_data, center)
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


output = True  # Toggle this flag to enable/disable prints
def debug_print(*args, **kwargs):
    if output:
        print(*args, **kwargs)


def clean():
    return "."


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.readlines()

    matrix = utils.grid_parse_list(data)
    length = len(matrix)
    width = len(matrix[0])
    center = (int(length/2), int(width/2))

    matrix = utils.grid_parse_dict(data)
    cluster = defaultdict(clean)
    for key in matrix:
        cluster[key] = matrix[key]
    
    return cluster, center



def part1(data, center):

    position = center
    direction = (-1,0)
    infection_caused = 0

    for _ in range(10000):
        node = data[position]
        if node == "#":
            if direction == (-1,0):
                direction = (0,1)
            elif direction == (1,0):
                direction = (0,-1)
            elif direction == (0,1):
                direction = (1,0)
            elif direction == (0,-1):
                direction = (-1,0)
            
            data[position] = "."
        else:
            if direction == (-1,0):
                direction = (0,-1)
            elif direction == (1,0):
                direction = (0,1)
            elif direction == (0,1):
                direction = (-1,0)
            elif direction == (0,-1):
                direction = (1,0)
            
            data[position] = "#"
            infection_caused += 1
        
        position = (position[0] + direction[0], position[1] + direction[1])
        
    return infection_caused


def part2(data, center):
    position = center
    direction = (-1,0)
    infection_caused = 0

    for _ in range(10000000):
        node = data[position]
        if node == "#":
            if direction == (-1,0):
                direction = (0,1)
            elif direction == (1,0):
                direction = (0,-1)
            elif direction == (0,1):
                direction = (1,0)
            elif direction == (0,-1):
                direction = (-1,0)
            data[position] = "F"
        elif node == ".":
            if direction == (-1,0):
                direction = (0,-1)
            elif direction == (1,0):
                direction = (0,1)
            elif direction == (0,1):
                direction = (-1,0)
            elif direction == (0,-1):
                direction = (1,0)
            data[position] = "W"
        elif node == "W":
            infection_caused += 1
            data[position] = "#"
        elif node == "F":
            direction = (direction[0]*(-1), direction[1]*(-1))
            data[position] = "."

        position = (position[0] + direction[0], position[1] + direction[1])
        
    return infection_caused


if __name__ == "__main__":

    main()