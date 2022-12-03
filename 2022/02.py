import aocd
from aocd import submit

DAY = 2


def main():
    print(get_data())
    print(part_a())
    print(part_b())
    # print(submit(part_a(), part="a", day=DAY, year=2022))
    # print(submit(part_b(), part="b", day=DAY, year=2022))


def get_data():
    return [x for x in aocd.get_data(day=DAY, year=2022).splitlines()]


def part_a():
    total = 0
    for play in get_data():
        total += calc_score(play)
    return total


def part_b():
    total = 0
    for play in get_data():
        total += calc_score2(play)
    return total


def calc_score(play):
    plays = {
        'A X': 3 + 1,
        'A Y': 6 + 2,
        'A Z': 0 + 3,
        'B X': 0 + 1,
        'B Y': 3 + 2,
        'B Z': 6 + 3,
        'C X': 6 + 1,
        'C Y': 0 + 2,
        'C Z': 3 + 3,
    }
    return plays[play]


def calc_score2(play):
    plays = {
        'A X': 0 + 3,
        'A Y': 3 + 1,
        'A Z': 6 + 2,
        'B X': 0 + 1,
        'B Y': 3 + 2,
        'B Z': 6 + 3,
        'C X': 0 + 2,
        'C Y': 3 + 3,
        'C Z': 6 + 1,
    }
    return plays[play]


if __name__ == "__main__":
    main()
