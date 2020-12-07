from lib import load_input


def solve(data):
    return part_one(data.splitlines())
    # return part_two(data.splitlines())


def parse_data(data):
    all_bags = dict()
    for line in data:
        color = line.split("bag")[0].strip()
        info = line.split("contain")[1].strip()
        can_contain = []
        for contain in info.split(", "):
            split = contain.split()
            can_contain.append((split[0], ''.join(split[1:-1])))
        all_bags.update({color.replace(" ", ""): can_contain})
    return all_bags


def part_one(data):
    # Strip count, values now are list of color
    all_bags = {k: [t[1] for t in v] for k, v in parse_data(data).items()}

    possible = set()
    for bag in all_bags:
        if "shinygold" in all_bags[bag]:
            possible.add(bag)

    # Find all bags containing any possible bag
    for _ in range(len(data)):
        for bag, contents in all_bags.items():
            if bag not in possible:
                if any(color in possible for color in contents):
                    possible.add(bag)

    return len(possible)


def amount_of_bags_inside(current, all_bags):
    res = 1
    for amount, color in all_bags[current]:
        if color != "other":
            res += int(amount) * amount_of_bags_inside(color, all_bags)
    return res


def part_two(data):
    return amount_of_bags_inside("shinygold", parse_data(data)) - 1


if __name__ == "__main__":
    print(solve(load_input(7, "small")))
    print(solve(load_input(7, "small2")))
    print(solve(load_input(7)))
