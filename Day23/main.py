# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
from collections import defaultdict
import sympy


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1 = part1(data)
    part1_time = time.time()
    answer2 = part2()
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

    return data


def value(v, reg):
    try:
        return int(v)
    except ValueError:
        return reg[v]


def part1(data):

    registers = defaultdict(int)
    i = 0
    number_mul = 0
    
    while 0 <= i < len(data):
        parts = data[i].strip().split()
        if parts[0] == "set":
            registers[parts[1]] = value(parts[2], registers)
        elif parts[0] == "mul":
            registers[parts[1]] *= value(parts[2], registers)
            number_mul += 1
        elif parts[0] == "sub":
            registers[parts[1]] -= value(parts[2], registers)
        elif parts[0] == "jnz":
            if value(parts[1], registers) != 0:
                i += value(parts[2], registers)
                continue
        i += 1
    return number_mul


def part2():
    h=0
    for b in range(108100,125101, 17):
        if len(sympy.divisors(b)) > 2:
            h += 1
    return h


if __name__ == "__main__":
    main()