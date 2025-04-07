FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

import time
import utils
from collections import defaultdict


def main():
    start_time = time.time()

    parse_time = time.time()

    answer1 = part1()
    part1_time = time.time()
    part2_time = time.time()

    print("---------------------------------------------------")
    print(f"Part 1 Answer: {answer1}")
    print()
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
    total_steps = 12667664
    cursor = 0
    state = 1
    tape = defaultdict(int)

    rules = {
        1: {
          0: [1, 1, 2],
          1: [0, -1, 3]
        },
        2: {
          0: [1, -1, 1],
          1: [1, 1, 4]
        },
        3: {
          0: [0, -1, 2],
          1: [0, -1, 5]
        },
        4: {
          0: [1, 1, 1],
          1: [0, 1, 2]
        },
        5: {
          0: [1, -1, 6],
          1: [1, -1, 3]
        },
        6: {
          0: [1, 1, 4],
          1: [1, 1, 1]
        },
    }

    for _ in range(total_steps):
        value = tape[cursor]

        tape[cursor] = rules[state][value][0]
        cursor += rules[state][value][1]
        state = rules[state][value][2]
    
    return sum(1 for key in tape if tape[key] == 1)
    


if __name__ == "__main__":
    main()