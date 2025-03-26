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


output = True  # Toggle this flag to enable/disable prints
def debug_print(*args, **kwargs):
    if output:
        print(*args, **kwargs)


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.read()

    return [x for x in data.strip().split(",")]


def part1(data):

    position = (0,0)
    for direction in data:
        if direction == "ne":
            position = (position[0]-1, position[1]+1)
        elif direction == "nw":
            position = (position[0]-1, position[1]-1)
        elif direction == "sw":
            position = (position[0]+1, position[1]-1)
        elif direction == "se":
            position = (position[0]+1, position[1]+1)
        elif direction == "s":
            position = (position[0]+1, position[1])
        elif direction == "n":
            position = (position[0]-1, position[1])
        
    return max(abs(position[0]), abs(position[1]))


def part2(data):

    position = (0,0)
    max_dist = 0
    for direction in data:
        if direction == "ne":
            position = (position[0]-1, position[1]+1)
        elif direction == "nw":
            position = (position[0]-1, position[1]-1)
        elif direction == "sw":
            position = (position[0]+1, position[1]-1)
        elif direction == "se":
            position = (position[0]+1, position[1]+1)
        elif direction == "s":
            position = (position[0]+1, position[1])
        elif direction == "n":
            position = (position[0]-1, position[1])
        
        if abs(position[0]) > max_dist:
            max_dist = abs(position[0])
        if abs(position[1]) > max_dist:
            max_dist = abs(position[1])
        
    return max_dist


if __name__ == "__main__":
    main()