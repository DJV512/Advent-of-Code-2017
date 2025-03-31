FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

import time
import utils


def main():
    start_time = time.time()

    parse_time = time.time()

    answer1 = part1()
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


def part1():
    # Sample Input
    # inputA = 65
    # inputB = 8921

    # Real Input
    inputA = 722
    inputB = 354

    matches = 0
    for _ in range(40000000):
        inputA = (inputA * 16807) % 2147483647
        inputB = (inputB * 48271) % 2147483647

        binaryA = bin(inputA)[-16:]
        binaryB = bin(inputB)[-16:]

        if binaryA == binaryB:
            matches += 1

    return matches


def part2():
     # Sample Input
    # inputA = 65
    # inputB = 8921

    # Real Input
    inputA = 722
    inputB = 354

    comparisons = 0
    matches = 0
    while comparisons < 5000000:
        inputA = (inputA * 16807) % 2147483647
        while inputA % 4 != 0:
            inputA = (inputA * 16807) % 2147483647

        inputB = (inputB * 48271) % 2147483647
        while inputB % 8 != 0:
            inputB = (inputB * 48271) % 2147483647

        comparisons += 1
        binaryA = bin(inputA)[-16:]
        binaryB = bin(inputB)[-16:]

        if binaryA == binaryB:
            matches += 1

    return matches


if __name__ == "__main__":
    main()