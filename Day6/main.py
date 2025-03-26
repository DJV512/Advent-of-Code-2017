# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
from copy import deepcopy


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1, data_state = part1(data)
    part1_time = time.time()
    answer2 = part2(data, data_state)
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


output = False  # Toggle this flag to enable/disable prints
def debug_print(*args, **kwargs):
    if output:
        print(*args, **kwargs)


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.read()

    return [int(x) for x in data.strip().split()]


def part1(data):
    mutable_data = deepcopy(data)
    length = len(mutable_data)
    data_state = "-".join([str(x) for x in mutable_data])
    seen = set()
    seen.add(data_state)
    steps = 0
    while True:
        steps += 1
        position = mutable_data.index(max(mutable_data))
        to_add = mutable_data[position]
        mutable_data[position] = 0
        for i in range(1, to_add+1):
            mutable_data[(position + i)%length] += 1
        data_state = "-".join([str(x) for x in mutable_data])
        debug_print(f"{steps=}, {mutable_data=}")
        if data_state in seen:         
            return steps, data_state
        seen.add(data_state)

    

def part2(data, cycle_state):
    debug_print(data)
    mutable_data = deepcopy(data)
    length = len(mutable_data)
    data_state = "-".join([str(x) for x in mutable_data])
    seen = set()
    seen.add(data_state)
    steps = 0
    cycle_list = []
    while True:
        steps += 1
        position = mutable_data.index(max(mutable_data))
        to_add = mutable_data[position]
        mutable_data[position] = 0
        for i in range(1, to_add+1):
            mutable_data[(position + i)%length] += 1
        data_state = "-".join([str(x) for x in mutable_data])
        debug_print(f"{steps=}, {mutable_data=}")
        if data_state == cycle_state:
            cycle_list.append(steps)
            if len(cycle_list) == 2:
                return cycle_list[1]-cycle_list[0]
        seen.add(data_state)


if __name__ == "__main__":
    main()