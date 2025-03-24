# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
from collections import Counter


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

    phrases = []
    for line in data:
        phrases.append(line.strip().split())

    return phrases


def part1(data):
    valid = 0
    for parts in data:
        if len(parts) == len(set(parts)):
            valid +=1
    return valid


def part2(data):
    valid = 0
    for parts in data:
        seen = set()
        good = True
        for i, part1 in enumerate(parts):
            if good:
                for j, part2 in enumerate(parts):
                    if good:
                        if i != j and (part2, part1) not in seen:
                            seen.add((part1, part2))
                            count1 = Counter(part1)
                            count2 = Counter(part2)
                            if count1 == count2:
                                good = False
        if good:
            valid += 1


    return valid


if __name__ == "__main__":
    main()