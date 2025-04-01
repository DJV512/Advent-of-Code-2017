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
    input = 328
    buffer = [0]
    position = 0
    
    for x in range(1, 2018):
        length = len(buffer)
        move = input % length
        after_move = (position + move) % length
        position = after_move+1
        buffer.insert(position, x)

    pos_2017 = buffer.index(2017)

    return buffer[pos_2017 + 1]


def part2():
    input = 328
    length = 1
    position = 0
    nums_at_pos_1 = []
    
    for x in range(1, 50000001):
        move = input % length
        after_move = (position + move) % length
        position = after_move+1
        if position == 1:
            nums_at_pos_1.append(x)
        length += 1

    return nums_at_pos_1[-1]


if __name__ == "__main__":
    main()