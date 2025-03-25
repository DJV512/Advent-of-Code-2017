# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1, possibles = part1(data)
    part1_time = time.time()
    answer2 = part2(data, possibles)
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

    programs = {}
    for line in data:
        if "->" in line:
            parts = line.strip().split(" -> ")
            left = parts[0].split()
            right = parts[1].split(", ")
            programs[left[0]] = [int(left[1][1:-1]), right]
        else:
            parts = line.strip().split()
            programs[parts[0]] = [int(parts[1][1:-1])]

    return programs


def part1(data):
    
    possibles = []
    for program in data:
        if len(data[program]) > 1:
            possibles.append(program)
    
    for possible1 in possibles:
        maybe = True
        for possible2 in possibles:
            if possible1 != possible2:
                if possible1 in data[possible2][1]:
                    maybe = False
        if maybe:
            return possible1, possibles



def part2(data, possibles):

    keep_going = True
    while keep_going:
        keep_going = False
        for possible in possibles:
            add = False
            if len(data[possible]) == 2:
                weights = []
                for program in data[possible][1]:
                    if len(data[program]) == 1:
                        weights.append(data[program][0])
                    else:
                        try:
                            weights.append(data[program][0]+data[program][2])
                        except IndexError:
                            keep_going = True
                            add = True
                            break
                if not add:
                    data[possible].append(sum(weights))
                if len(set(weights)) > 1:
                    for i in range(2,len(weights)):
                        if weights[i] != weights[i-1] and weights[i] != weights[i-2]:
                            index = i
                            break
                        elif weights[i-1] != weights[i] and weights[i-1] != weights[i-2]:
                            index = i
                            break
                        elif weights[i-2] != weights[i-1] and weights[i-2] != weights[i]:
                            index = i
                            break
                    try:
                        diff = weights[index] - weights[index-1]
                    except IndexError:
                        diff = weights[index] - weights[index+1]
                    
                    return data[data[possible][1][index]][0] - diff


if __name__ == "__main__":
    main()