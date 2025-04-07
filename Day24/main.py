# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
from copy import deepcopy


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1, answer2 = part1(data)
    part1_time = time.time()
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


def part1(data):

    stack = []

    for line in data:
        parts = line.strip().split("/")
        if "0" in parts:
            parts.remove("0")
            available = parts[0]
            stack.append(([line.strip()], available))
    
    possibles = []

    while stack:
        bridge, available = stack.pop()
        possibles.append(bridge)

        for line in data:
            if line.strip() not in bridge:
                parts = line.strip().split("/")
                if available in parts:
                    parts.remove(available)
                    next_available = parts[0]
                    new_bridge = deepcopy(bridge)
                    new_bridge.append(line.strip())
                    stack.append((new_bridge, next_available))
        
    
    strengths = []
    longest = 0
    best_long = []
    for possible in possibles:
        new_best = False
        match_best = False
        if len(possible) > longest:
            longest = len(possible)
            new_best = True
        elif len(possible) == longest:
            match_best = True
        strength = 0
        for part in possible:
            parts = part.split("/")
            strength += int(parts[0]) + int(parts[1])
        strengths.append(strength)
        if new_best:
            best_long = []
            best_long.append(strength)
        if match_best:
            best_long.append(strength)

    answer1 = max(strengths)
    answer2 = max(best_long)

    return answer1, answer2









def part2(data):
    return None


if __name__ == "__main__":
    main()