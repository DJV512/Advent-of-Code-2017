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

    moves = data.strip().split(",")

    return moves


def part1(data):
    s_input = ["a", "b", "c", "d", "e"]
    r_input = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]

    line = r_input

    for move in data:
        if move[0] == "s":
            distance = int(move[1:])
            half1 = line[0:len(line)-distance]
            half2 = line[len(line)-distance:]
            line = half2 + half1
        elif move[0] == "x":
            parts = move[1:].split("/")
            first = line[int(parts[0])]
            second = line[int(parts[1])]
            line[int(parts[1])] = first
            line[int(parts[0])] = second
        elif move[0] == "p":
            parts = move[1:].split("/")
            first = line.index(parts[0])
            second = line.index(parts[1])
            line[first] = parts[1]
            line[second] = parts[0]
        else:
            raise TypeError("Invalid move")
    
    return "".join(line)


def part2(data):
    line = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]

    codes = {}
    for z in range(37):
        for move in data:
            if move[0] == "s":
                distance = int(move[1:])
                half1 = line[0:len(line)-distance]
                half2 = line[len(line)-distance:]
                line = half2 + half1
            elif move[0] == "x":
                parts = move[1:].split("/")
                first = line[int(parts[0])]
                second = line[int(parts[1])]
                line[int(parts[1])] = first
                line[int(parts[0])] = second
            elif move[0] == "p":
                parts = move[1:].split("/")
                first = line.index(parts[0])
                second = line.index(parts[1])
                line[first] = parts[1]
                line[second] = parts[0]
            else:
                raise TypeError("Invalid move")
        
            codes[z+1] = "".join(line)

    index = 1000000000 % 36
    
    return codes[index]


if __name__ == "__main__":
    main()