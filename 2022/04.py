import aocd
from aocd import submit

DAY = 4


def main():
    print(get_data())
    print(part_a())
    print(part_b())
    # print(submit(part_a(), part="a", day=DAY, year=2022))
    # print(submit(part_b(), part="b", day=DAY, year=2022))
å

def get_data():
    return [x for x in aocd.get_data(day=DAY, year=2022).splitlines()]


def part_a():
    total = 0
    for row in get_data():
        start, finish = row.split(',')[0].split('-')
        set_1 = set(range(int(start), int(finish)+1))
        start_2, finish_2 = row.split(',')[1].split('-')
        set_2 = set(range(int(start_2), int(finish_2)+1))
        if set_1.issubset(set_2) or set_2.issubset(set_1):
            total += 1
    return total


def part_b():
    total = 0
    for row in get_data():
        start, finish = row.split(',')[0].split('-')
        set_1 = set(range(int(start), int(finish)+1))
        start_2, finish_2 = row.split(',')[1].split('-')
        set_2 = set(range(int(start_2), int(finish_2)+1))
        if set_1.intersection(set_2):
            total += 1
    return total


if __name__ == "__main__":
    main()
