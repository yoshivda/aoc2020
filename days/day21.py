from lib import load_input


def solve(data):
    # return part_one(data.splitlines())
    return part_two(data.splitlines())


def parse_data(data):
    all_ings = []
    possible = dict()
    for line in data:
        ings, allergens = line.split("(contains ")
        all_ings.extend(ings.split())
        ings = set(ings.split())
        allergens = allergens[:-1]
        for allergen in allergens.split(", "):
            if allergen in possible:
                possible[allergen] = possible[allergen].intersection(ings)
            else:
                possible[allergen] = ings
    return all_ings, possible


def part_one(data):
    all_ings, possible = parse_data(data)
    return sum(len([x for x in all_ings if x == ing]) for ing in set(all_ings)
               if all(ing not in ings for _, ings in possible.items()))


def part_two(data):
    _, possible = parse_data(data)

    treated = set()
    while any(len(x) > 1 for _,  x in possible.items()):
        possible = {a: i if len(i) == 1 else i - treated for a, i in possible.items()}
        treated = treated.union(*(i for i in possible.values() if len(i) == 1))
    return ",".join(next(iter(v)) for _, v in sorted(possible.items()))


if __name__ == "__main__":
    print(solve(load_input(21, "small")))
    print(solve(load_input(21)))
