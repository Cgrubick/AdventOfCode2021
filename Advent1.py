
def get_input():
    with open("Advent_of_Code1input.txt", "r") as f:
        return [int(line.strip()) for line in f]

def part_1(depth):
    return sum([1 for i in range(len(depth)) if depth[i] > depth[i-1]])

def part_2(depth):
    return [(depth[i] + depth[i+1] + depth[i+2]) for i in range(len(depth) - 2)]

print(f'Part 1 = {part_1(get_input())}. Part 2 = {part_1(part_2(get_input()))}.')

