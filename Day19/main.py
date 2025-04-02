# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils


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


output = False  # Toggle this flag to enable/disable prints
def debug_print(*args, **kwargs):
    if output:
        print(*args, **kwargs)


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.readlines()

    return data


def part1(data):
    startx = data[0].index("|")
    position = (0, startx)
    direction = (1, 0)
    path = ""
    steps = 1

    while 0 <= position[0] < len(data) and 0 <= position[1] < len(data[0]):
        position = (position[0]+direction[0], position[1]+direction[1])
        
        if data[position[0]][position[1]] == " ":
            break

        steps += 1

        if direction in [(1,0), (-1,0)]:
            if data[position[0]][position[1]] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                path += data[position[0]][position[1]]
                debug_print(path)
                continue
            elif data[position[0]][position[1]] == "|" or data[position[0]][position[1]] == "-":
                continue
            elif data[position[0]][position[1]] == "+":
                if position[1] != len(data[0])-1:
                    if data[position[0]][position[1]+1] == "-" or data[position[0]][position[1]+1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        direction = (0, 1)
                    else:
                        direction = (0, -1)
                else:
                    direction = (0, -1)

        elif direction in [(0,1), (0,-1)]:
            if data[position[0]][position[1]] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                path += data[position[0]][position[1]]
                debug_print(path)
                continue
            elif data[position[0]][position[1]] == "|" or data[position[0]][position[1]] == "-":
                continue
            elif data[position[0]][position[1]] == "+":
                if position[0] != len(data)-1:
                    if data[position[0]+1][position[1]] == "|" or data[position[0]+1][position[1]] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        direction = (1, 0)
                    else:
                        direction = (-1, 0)
                else:
                    direction = (-1, 0)

    return path, steps


if __name__ == "__main__":
    main()