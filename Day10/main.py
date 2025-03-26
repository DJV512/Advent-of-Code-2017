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


output = False  # Toggle this flag to enable/disable prints
def debug_print(*args, **kwargs):
    if output:
        print(*args, **kwargs)


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.read()

    return [int(x) for x in data.strip().split(",")]


def part1(data):

    i = 0
    skip = 0
    numbers = [x for x in range(256)]
    for length in data:
        debug_print(f"{length=}, {i=}, {skip=}")
        to_reverse=[]
        for x in range(length):
            to_reverse.append(numbers[(i+x)%256])
        now_reversed = list(reversed(to_reverse))
        debug_print(f"{now_reversed=}")
        for x in range(length):
            numbers[(i+x)%256] = now_reversed[x]
        i += length + skip
        skip += 1
    
    return numbers[0]*numbers[1]



def part2():

    with open(FILENAME, "r") as f:
        data = f.read()

    instructions = []
    for char in data:
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
        for i, num in enumerate(sixteen):
            if i == 0:
                continue
            elif i == 1:
                result = sixteen[0] ^ num
            else:
                result ^= num
        
        part = hex(result).lstrip("0x")
        if len(part) == 1:
            part = "0" + part
        answer += part
    
    return answer
    

if __name__ == "__main__":
    main()