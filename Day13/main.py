FILENAME = "sample_input.txt"
# FILENAME = "input.txt"

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


output = False  # Toggle this flag to enable/disable prints
def debug_print(*args, **kwargs):
    if output:
        print(*args, **kwargs)


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.readlines()

    firewall = {}
    for line in data:
        depth, range = line.strip().split(": ")
        firewall[int(depth)] = int(range)

    return firewall


def draw_state(firewall, scan_locations, me_location, max_depth, max_range):
    print(utils.CLEAR)
    for i in range(max_range+1):
        for j in range(max_depth):
            if i == 0:
                print(f"  {j}  ", end="")
            else:
                if j in firewall:
                    if i <= firewall[j]:
                        if me_location == j and i == 1:
                            print(" (", end="")
                        else:
                            print(" [", end="")

                        if scan_locations[j][0] == i-1:
                            print("S", end="")
                        else:
                            print(" ", end="")

                        if me_location == j and i == 1:
                            print(") ", end="")
                        else:
                            print("] ", end="")
                    else:
                        print("     ", end="")

                else:
                    if i == 1:
                        if j == me_location:
                            print(" (.) ", end="")
                        else:
                            print(" ... ", end="")
                    else:
                        print("     ", end="")
        print()
                    



def part1(firewall):
    max_depth = max(firewall) + 1
    max_range = max(firewall.values())
    scan_locations = {x:[0, True] for x in firewall}
    me_location = -1
    severity = 0

    for _ in range(max_depth):
        me_location += 1
        debug_print(f"Picosecond: {me_location}")
        if me_location in scan_locations and scan_locations[me_location][0] == 0:
            
            severity += me_location * firewall[me_location]

        # draw_state(firewall, scan_locations, me_location, max_depth, max_range)
        
        for layer in scan_locations:
            if scan_locations[layer][1]:
                scan_locations[layer][0] += 1
                if scan_locations[layer][0] == firewall[layer]-1:
                    scan_locations[layer][1] = False
            else:
                scan_locations[layer][0] -= 1
                if scan_locations[layer][0] == 0:
                    scan_locations[layer][1] = True
        
        # draw_state(firewall, scan_locations, me_location, max_depth, max_range)

    return severity


def part2(firewall):

    for delay in range(5000000):
        correct = True
        for layer in firewall:
            if (delay+layer) % ((firewall[layer]*2)-2) == 0:
                correct = False
                break
        if correct:
            return delay
    
    return f"Delay needs to be higher than {delay}"



if __name__ == "__main__":
    main()