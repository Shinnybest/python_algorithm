def findIndex(target):
    nums = [4, 6, 7, 9]
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

    findIndex(10)

def find(nums, target):
    for i, n in enumerate(nums):
        compliment = target - n

        if compliment in nums[i+1:]:
            return [nums.index(n), nums[i+1:].index(compliment) + i + 1]

def twoSum(nums, target):
        summap = {}
        for i, n in enumerate(nums):
            summap[n] = i

        for i, n in enumerate(nums):
            if target - n in summap and i != summap[target - n]:
                return [i, summap[target - n]]


def findSum(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num], i]

        nums_map[num] = i