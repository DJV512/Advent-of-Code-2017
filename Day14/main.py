FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

import time
import utils
from collections import Counter


def main():
    start_time = time.time()

    parse_time = time.time()

    answer1, disk = part1()
    part1_time = time.time()
    answer2 = part2(disk)
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



def part1():
    input = "hwlqcszp"
    sample = "flqrgnkx"

    disk = []

    for q in range(128):

        round_input = f"{input}-{q}"
        debug_print(round_input)

        instructions = []
        for char in round_input:
            instructions.append(ord(char))
        
        instructions += [17,31,73,47,23]

        i = 0
        skip = 0
        numbers = [x for x in range(256)]
        for _ in range(64):
            for length in instructions:
                to_reverse=[]
                for x in range(length):
                    to_reverse.append(numbers[(i+x)%256])
                now_reversed = list(reversed(to_reverse))
                for x in range(length):
                    numbers[(i+x)%256] = now_reversed[x]
                i += length + skip
                skip += 1

        answer = ""
        for x in range(0, 256, 16):
            sixteen = numbers[x:x+16]
            debug_print(f"{sixteen=}")
            for i, num in enumerate(sixteen):
                if i == 0:
                    continue
                elif i == 1:
                    result = sixteen[0] ^ num
                else:
                    result ^= num
            
            debug_print(f"{result=}")
            
            part = hex(result)[2:]
            if len(part) == 1:
                part = "0" + part
            if len(part) == 0:
                part = "00"
            answer += part

        debug_print(f"{answer=}")
        
        final_result = ""
        for char in answer:
            new_addition = bin(int(char, 16))[2:].zfill(4)
            final_result += new_addition
        
        disk.append(final_result)

    in_use = 0
    for row in disk:
        debug_print(row)
        count = Counter(row)
        in_use += count["1"]

    return in_use, disk


def part2(disk):
    length = len(disk)
    width = len(disk[0])

    regions = 0
    seen = set()
    for y in range(length):
        for x in range(width):
            if disk[y][x] == "1" and (y,x) not in seen:
                regions += 1
                queue = []
                queue.append((y,x))
                visited = set()
                while queue:
                    location = queue.pop()

                    visited.add(location)
                    
                    if disk[location[0]][location[1]] == "0":
                        continue

                    if disk[location[0]][location[1]] == "1":
                        seen.add(location)

                        for direction in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                            next_location = (location[0] + direction[0], location[1] + direction[1])

                            if 0 <= next_location[0] < length and 0 <= next_location[1] < width and next_location not in seen and next_location not in visited:
                                queue.append(next_location)

    return regions


if __name__ == "__main__":
    main()