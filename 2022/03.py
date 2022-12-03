import aocd
from aocd import submit

DAY = 3


def main():
    print(get_data())
    print(part_a())
    print(part_b())
    # print(submit(part_a(), part="a", day=DAY, year=2022))
    # print(submit(part_b(), part="b", day=DAY, year=2022))


def get_data():
    return [x for x in aocd.get_data(day=DAY, year=2022).splitlines()]


def part_a():
    return sum(get_letter_score(find_common_item(row)) for row in get_data())


def part_b():
    total = 0
    set_3 = []
    for sack in get_data():
        if len(set_3) < 3:
            set_3.append(sack)
        else:
            item = set(set_3[0]) & set(set_3[1]) & set(set_3[2])
            total += get_letter_score(item.pop())
            set_3 = [sack]

    item = set(set_3[0]) & set(set_3[1]) & set(set_3[2])
    total += get_letter_score(item.pop())

    return total


def find_common_item(sack):
    p1, p2 = sack[:len(sack) // 2], sack[len(sack) // 2:]
    item = set(p1) & set(p2)
    return item.pop()


def get_letter_score(char):
    if char.isupper():
        return ord(char) - 38
    return ord(char) - 96


if __name__ == "__main__":
    main()
