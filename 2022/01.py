import aocd
from aocd import submit

DAY = 1


def main():
    print(part_a())
    print(part_b())
    # print(submit(part_a(), part="a", day=DAY, year=2022))
    # print(submit(part_b(), part="b", day=DAY, year=2022))


def get_data():
    return [x for x in aocd.get_data(day=DAY, year=2022).splitlines()]


def part_a():
    elves = get_calories_per_elves()
    return max(elves)


def part_b():
    elves = get_calories_per_elves()
    elves_sorted = sorted(elves)
    return elves_sorted[-1] + elves_sorted[-2] + elves_sorted[-3]


def get_calories_per_elves():
    data = get_data()
    elves = [0]
    key = 0
    for item in data:
        if item == '':
            key += 1
            elves.append(0)
        else:
            elves[key] += int(item)
    return elves


if __name__ == "__main__":
    main()
