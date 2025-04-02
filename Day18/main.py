# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
from collections import defaultdict, deque


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

    return data


def value(v, reg):
    try:
        return int(v)
    except ValueError:
        return reg[v]


def part1(data):

    registers = defaultdict(int)
    i = 0
    
    while 0 <= i < len(data):
        parts = data[i].strip().split()

        if parts[0] == "snd":
            sound = registers[parts[1]]
        elif parts[0] == "set":
            registers[parts[1]] = value(parts[2], registers)
        elif parts[0] == "add":
            registers[parts[1]] += value(parts[2], registers)
        elif parts[0] == "mul":
            registers[parts[1]] *= value(parts[2], registers)
        elif parts[0] == "mod":
            registers[parts[1]] %= value(parts[2], registers)
        elif parts[0] == "rcv":
            if registers[parts[1]] != 0:
                return sound
        elif parts[0] == "jgz":
            if registers[parts[1]] > 0:
                i += value(parts[2], registers)
                continue
        i += 1


def part2(data):

    registers0 = defaultdict(int)
    registers0["p"] = 0
    i = 0
    zero_to_one = deque()

    registers1 = defaultdict(int)
    registers1["p"] = 1
    j = 0
    one_to_zero = deque()

    count_1_sends = 0

    while True:
        
        while 0 <= i < len(data):
            
            parts = data[i].strip().split()

            if parts[0] == "snd":
                debug_print(f"Sending {registers0[parts[1]]}")
                zero_to_one.append(value(parts[1], registers0))
            elif parts[0] == "set":
                registers0[parts[1]] = value(parts[2], registers0)
            elif parts[0] == "add":
                registers0[parts[1]] += value(parts[2], registers0)
            elif parts[0] == "mul":
                registers0[parts[1]] *= value(parts[2], registers0)
            elif parts[0] == "mod":
                registers0[parts[1]] %= value(parts[2], registers0)
            elif parts[0] == "rcv":
                if len(one_to_zero) != 0:
                    received = one_to_zero.popleft()
                    registers0[parts[1]] = received
                    debug_print(f"Program 0 receives {received}!")
                else:
                    break
            elif parts[0] == "jgz":
                if value(parts[1], registers0) > 0:
                    i += value(parts[2], registers0)
                    continue
            debug_print(f"After {i=}, registers0 = {dict(registers0)}")
            i+=1
        
        debug_print(f"Program 0 stopped at {i=}")
        debug_print(dict(registers0))
        debug_print(f"{zero_to_one=}")
        debug_print(f"{one_to_zero=}")
        debug_print()
        debug_print()
        # time.sleep(2)

        while 0 <= j < len(data):
            parts = data[j].strip().split()

            if parts[0] == "snd":
                debug_print(f"Sending {registers1[parts[1]]}")
                one_to_zero.append(value(parts[1], registers1))
                count_1_sends += 1
            elif parts[0] == "set":
                registers1[parts[1]] = value(parts[2], registers1)
            elif parts[0] == "add":
                registers1[parts[1]] += value(parts[2], registers1)
            elif parts[0] == "mul":
                registers1[parts[1]] *= value(parts[2], registers1)
            elif parts[0] == "mod":
                registers1[parts[1]] %= value(parts[2], registers1)
            elif parts[0] == "rcv":
                if len(zero_to_one) != 0:
                    received = zero_to_one.popleft()
                    registers1[parts[1]] = received
                    debug_print(f"Program 1 receives {received}!")
                else:
                    break
            elif parts[0] == "jgz":
                if value(parts[1], registers1) > 0:
                    j += value(parts[2], registers1)
                    continue
            debug_print(f"After {j=}, registers1 = {dict(registers1)}")
            j+=1

        debug_print(f"Program 1 stopped at {j=}")
        debug_print(dict(registers1))
        debug_print(f"{zero_to_one=}")
        debug_print(f"{one_to_zero=}")
        debug_print()
        debug_print()
        # time.sleep(2)
        
        if (len(zero_to_one) == 0 and len(one_to_zero) == 0) or (i < 0 or i >= len(data)) and (j < 0 or j >= len(data)):
            return count_1_sends
 


if __name__ == "__main__":
    main()