# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1, answer2 = part1(data)
    part1_time = time.time()

    print("---------------------------------------------------")
    print(f"Part 1 Answer: {answer1}")
    print()
    print(f"Part 2 Answer: {answer2}")
    print()
    print(f"Data Parse Execution Time: {1000*(parse_time - start_time):.2f} ms")
    print(f"Part 1 Execution Time:     {1000*(part1_time - parse_time):.2f} ms")
    print(f"Total Execution Time:      {1000*(part1_time - start_time):.2f} ms")
    print("---------------------------------------------------")


output = True  # Toggle this flag to enable/disable prints
def debug_print(*args, **kwargs):
    if output:
        print(*args, **kwargs)


def parse_data():

    with open(FILENAME, "r") as f:
        data = f.read()

    return data


def part1(data):

    score = 0
    depth = 0
    garbage_count = 0
    garbage = False
    skip = False
    for char in data:
        if skip:
            skip = False
            continue
        if char == "!":
            skip = True
        elif garbage and char != ">":
            garbage_count += 1
        elif char == "<":
            garbage = True
        elif char == ">":
            garbage = False
        elif char == "{":
            depth += 1
            score += depth
        elif char == "}":
            depth -= 1

    return score, garbage_count


if __name__ == "__main__":
    main()