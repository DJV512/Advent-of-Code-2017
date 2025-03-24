# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
from copy import deepcopy


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1 = part1(deepcopy(data))
    part1_time = time.time()
    answer2 = part2(deepcopy(data))
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
        data = f.readlines()

    jumps = []
    for line in data:
        jumps.append(int(line.strip()))

    return jumps


def part1(data):
    i = 0
    steps = 0
    while i < len(data):
        current_step = data[i]
        jump_to = i + current_step
        data[i] = current_step + 1
        i = jump_to
        steps += 1
    return steps


def part2(data):
    i = 0
    steps = 0
    while i < len(data):
        current_step = data[i]
        jump_to = i + current_step
        if current_step >= 3:
            data[i] -= 1
        else:
            data[i] = current_step + 1
        i = jump_to
        steps += 1
    return steps


if __name__ == "__main__":
    main()