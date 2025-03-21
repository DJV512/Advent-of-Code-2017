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
    return data


def part1(data):
    length = len(data.strip())
    sum = 0
    for i in range(1, length-1):
        if data[i] == data[i-1]:
            sum += int(data[i])
    if data[0] == data[-1]:
        sum += int(data[0])
    return sum


def part2(data):
    length = len(data.strip())
    half = length // 2
    sum = 0
    for i in range(length):
        next = (i + half) % length
        if data[i] == data[next]:
            sum += int(data[i])
    return sum


if __name__ == "__main__":
    main()