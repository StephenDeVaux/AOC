import aocd
from aocd import submit

DAY = 5

stacks = [
    ['Answer is : '],
    ['N', 'W', 'B'],
    ['B', 'M', 'D', 'T', 'P', 'S', 'Z', 'L'],
    ['R', 'W', 'Z', 'H', 'Q'],
    ['R', 'Z', 'J', 'V', 'D', 'W'],
    ['B', 'M', 'H', 'S'],
    ['B', 'P', 'V', 'H', 'J', 'N', 'G', 'L'],
    ['S', 'L', 'D', 'H', 'F', 'Z', 'Q', 'J'],
    ['B', 'Q', 'G', 'J', 'F', 'S', 'W'],
    ['J', 'D', 'C', 'S', 'M', 'W', 'Z'],
]


def main():
    print(get_data())
    # print(part_a())
    print(part_b())
    # print(submit(part_a(), part="a", day=DAY, year=2022))
    # print(submit(part_b(), part="b", day=DAY, year=2022))


def get_data():
    data = [x for x in aocd.get_data(day=DAY, year=2022).splitlines()]
    return data[10:]


def move_box(pos_start, pos_to):
    stacks[pos_to].insert(0, stacks[pos_start].pop(0))


def move_multi_boxes(boxes, pos_start, pos_to):
    stacks[pos_to] = stacks[pos_start][:boxes] + stacks[pos_to]
    stacks[pos_start] = stacks[pos_start][boxes:]


def part_a():
    instructions = get_data()
    for inst in instructions:
        _, boxes, _, pos_start, _, pos_to = inst.split()
        for _ in range(int(boxes)):
            move_box(int(pos_start), int(pos_to))

    return "".join(stack[0] for stack in stacks)


def part_b():
    instructions = get_data()
    for inst in instructions:
        _, boxes, _, pos_start, _, pos_to = inst.split()
        move_multi_boxes(int(boxes), int(pos_start), int(pos_to))

    return "".join(stack[0] for stack in stacks)


if __name__ == "__main__":
    main()
