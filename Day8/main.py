# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
from collections import defaultdict


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
        data = f.readlines()

    instructions = []
    for line in data:
        parts = line.strip().split()
        instructions.append((parts[0], parts[1], int(parts[2]), parts[4], parts[5], int(parts[6])))

    return instructions


def part1(data):

    registers = defaultdict(int)
    for r2change, direction, amount, r2check, op, cutoff in data:
        if op == ">":
            if registers[r2check] > cutoff:
                if direction == "inc":
                    registers[r2change] += amount
                else:
                    registers[r2change] -= amount
        elif op == "<":
            if registers[r2check] < cutoff:
                if direction == "inc":
                    registers[r2change] += amount
                else:
                    registers[r2change] -= amount
        elif op == ">=":
            if registers[r2check] >= cutoff:
                if direction == "inc":
                    registers[r2change] += amount
                else:
                    registers[r2change] -= amount
        elif op == "<=":
            if registers[r2check] <= cutoff:
                if direction == "inc":
                    registers[r2change] += amount
                else:
                    registers[r2change] -= amount
        elif op == "==":
            if registers[r2check] == cutoff:
                if direction == "inc":
                    registers[r2change] += amount
                else:
                    registers[r2change] -= amount
        elif op == "!=":
            if registers[r2check] != cutoff:
                if direction == "inc":
                    registers[r2change] += amount
                else:
                    registers[r2change] -= amount
        
    return max(registers.values())


def part2(data):
    registers = defaultdict(int)
    highest = 0
    for r2change, direction, amount, r2check, op, cutoff in data:
        if op == ">":
            if registers[r2check] > cutoff:
                if direction == "inc":
                    registers[r2change] += amount
                else:
                    registers[r2change] -= amount
        elif op == "<":
            if registers[r2check] < cutoff:
                if direction == "inc":
                    registers[r2change] += amount
                else:
                    registers[r2change] -= amount
        elif op == ">=":
            if registers[r2check] >= cutoff:
                if direction == "inc":
                    registers[r2change] += amount
                else:
                    registers[r2change] -= amount
        elif op == "<=":
            if registers[r2check] <= cutoff:
                if direction == "inc":
                    registers[r2change] += amount
                else:
                    registers[r2change] -= amount
        elif op == "==":
            if registers[r2check] == cutoff:
                if direction == "inc":
                    registers[r2change] += amount
                else:
                    registers[r2change] -= amount
        elif op == "!=":
            if registers[r2check] != cutoff:
                if direction == "inc":
                    registers[r2change] += amount
                else:
                    registers[r2change] -= amount
        
        if registers[r2change] > highest:
            highest = registers[r2change]
        
    return highest


if __name__ == "__main__":
    main()