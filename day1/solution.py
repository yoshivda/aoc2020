

def solve(filename):
    with open(filename) as f:
       nums = [int(line) for line in f]
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == 2020:
                return nums[i] * nums[j]


if __name__ == "__main__":
    print(solve("input.txt"))
