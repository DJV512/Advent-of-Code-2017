# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
import re
from copy import deepcopy


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    original_data = deepcopy(data)

    answer1 = part1(data)
    part1_time = time.time()
    answer2 = part2(original_data)
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

    pattern = r"-?\d+,-?\d+,-?\d+"
    particles = {}
    for i, line in enumerate(data):
        matches = re.findall(pattern, line.strip())
        debug_print(matches)
        particles[i] = {}
        particles[i]["p"] = [int(x) for x in matches[0].split(",")]
        particles[i]["v"] = [int(x) for x in matches[1].split(",")]
        particles[i]["a"] = [int(x) for x in matches[2].split(",")]


    return particles


def part1(data):

    manhattan = []

    for x in range(500):
        for particle in data:
            ax, ay, az = data[particle]["a"]
            vx, vy, vz = data[particle]["v"]
            px, py, pz = data[particle]["p"]

            vx += ax
            vy += ay
            vz += az

            data[particle]["v"] = [vx,vy,vz]

            px += vx
            py += vy
            pz += vz
            debug_print(f"time = {x}, {particle=}, position = {px, py, pz}")
            debug_print()
            data[particle]["p"] = [px,py,pz]

    for particle in data:
        debug_print(data[particle]["p"])
        manhattan.append((abs(data[particle]["p"][0])+abs(data[particle]["p"][1])+abs(data[particle]["p"][2])))

    shortest = min(manhattan)
    index = manhattan.index(shortest)

    return index


def part2(data):

    time_since_collision = 0
    timing = 0
    while True:
        timing += 1
        for particle in data:
            ax, ay, az = data[particle]["a"]
            vx, vy, vz = data[particle]["v"]
            px, py, pz = data[particle]["p"]

            vx += ax
            vy += ay
            vz += az

            data[particle]["v"] = [vx,vy,vz]

            px += vx
            py += vy
            pz += vz
            data[particle]["p"] = [px,py,pz]

        positions = set()
        dupes = []
        for particle in data:
            if tuple(data[particle]["p"]) in positions:
                dupes.append(data[particle]["p"])
            else:
                positions.add(tuple(data[particle]["p"]))
        
        collision = False
        for particle in data.copy():
            if data[particle]["p"] in dupes:
                data.pop(particle)
                time_since_collision = 0
                collision = True
        
        if not collision:
            time_since_collision += 1
        
        if time_since_collision > 10:
            break

    return len(data)


if __name__ == "__main__":
    main()