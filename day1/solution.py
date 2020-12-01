

def solve(filename):
    with open(filename) as f:
       nums = [int(line) for line in f]
    # return part_one(nums)
    return part_two(nums)


def part_one(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == 2020:
                return nums[i] * nums[j]


def part_two(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if i == j or i == k or j == k:
                    continue
                if nums[i] + nums[j] + nums[k] == 2020:
                    return nums[i] * nums[j] * nums[k]


if __name__ == "__main__":
    print(solve("input.txt"))
