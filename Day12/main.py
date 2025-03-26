# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
import networkx as nx

def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1,answer2 = part1(data)
    part1_time = time.time()
    # answer2 = part2(data)
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

    pipes = {}
    for line in data:
        parts = line.strip().split(" <-> ")
        pipes[parts[0]] = parts[1].split(", ")

    return pipes


def part1(data):
    G = nx.Graph()
    for line in data:
        for edge in data[line]:
            G.add_edge(line,edge)

    total_nodes = len(list(nx.connected_components(G)))
    for x in list(nx.connected_components(G)):
        if "0" in x:
            return len(x), total_nodes


def part2(data):
    return None


if __name__ == "__main__":
    main()