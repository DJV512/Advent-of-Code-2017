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
    input = 265149
    sample = 1024

    # Note: this won't work for every number. Indeed, it doesn't work for the sample input.
    # I drew out the spiral and figured out how it would look at my input value,
    # and from there could tell that each square number took
    # (square_number ^ (1/2) - 1) steps to get to the center

    nearest_square = int(input ** (1/2))
    next_square = nearest_square + 1
    next_square_steps = next_square  - 1
    total_steps = next_square_steps - (next_square**2 - input)
    
    return total_steps


def part2():
    return None


if __name__ == "__main__":
    main()