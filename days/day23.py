from lib import load_input


def solve(data):
    # return part_one(data.splitlines()[0])
    return part_two(data.splitlines()[0])


def part_one(data):
    cups = [int(char) for char in data]
    cur_index = 0

    for i in range(100):
        taken = [cups[(cur_index + i) % len(data)] for i in range(1, 4)]
        cur_value = cups[cur_index]
        cups = [cup for cup in cups if cup not in taken]
        dest = (cur_value - 1) % (len(data) + 1)
        while dest not in cups:
            dest = (dest - 1) % (len(data) + 1)
        dest_index = (cups.index(dest) + 1) % len(data)
        cups[dest_index:dest_index] = taken
        cur_index = (cups.index(cur_value) + 1) % len(data)

    rotate = cups.index(1)
    cups = cups[rotate:] + cups[:rotate]
    return ''.join(map(str, cups[1:]))


def part_two(data):
    class Cup:
        def __init__(self, val):
            self.val = val
            self.next = None

        def __repr__(self):
            return f"<Cup {self.val}, {self.next.val}>"

    nums = [int(char) for char in data]
    nums.extend(range(len(data) + 1, 1000001))
    cups_list = [Cup(num) for num in nums]
    for i, cup in enumerate(cups_list):
        cup.next = cups_list[(i + 1) % len(cups_list)]
    cups = {c.val: c for c in cups_list}
    cur = cups[nums[0]]

    for i in range(10000000):
        if i % 1000000 == 0:
            print(i)
        taken = [cur.next.val, cur.next.next.val, cur.next.next.next.val]
        dest = (cur.val - 1) % (len(cups_list) + 1)
        while dest not in cups or dest in taken:
            dest = (dest - 1) % (len(cups_list) + 1)
        dest_cup = cups[dest]
        after_dest = dest_cup.next
        dest_cup.next = cur.next
        cur.next = cur.next.next.next.next
        dest_cup.next.next.next.next = after_dest
        cur = cur.next

    return cups[1].next.val * cups[1].next.next.val


if __name__ == "__main__":
    # print(solve(load_input(23, "small")))
    print(solve(load_input(23)))
