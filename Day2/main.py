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
        data = f.readlines()

    numbers = []
    for line in data:
        parts = line.strip().split()
        numbers.append(parts)

    return numbers


def part1(data):

    checksum = 0
    for row in data:
        low = 100000000000000
        high = 0
        for num in row:
            if int(num) > high:
                high = int(num)
            if int(num) < low:
                low = int(num)
        checksum += (high-low)
    return checksum


def part2(data):

    checksum = 0
    for row in data:
        for num1 in row:
            for num2 in row:
                if num1 != num2:
                    if int(num1) % int(num2) == 0:
                        checksum += int((int(num1)/int(num2)))
    return checksum


if __name__ == "__main__":
    main()