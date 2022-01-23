# [1, 2, 3]

# def findSubsets():
#     nums = [1, 2, 3]
#     result = []
#     def dfs(index, subset):
#
#         if len(nums) == len(subset):
#             return
#
#         for i in range(index, len(nums)):
#             result.append(subset + [nums[i]])
#             # print('result', result)
#             # print('i', i)
#
#             dfs(i+1, subset + [nums[i]])
#
#
#     dfs(0, [])
#     return print(result)

# findSubsets()

def subset():
    nums = [1, 2, 3]
    result = []
    def dfs(index, subset):
        result.append(subset)

        for i in range(index, len(nums)):
            dfs(i+1, subset + [nums[i]])


    dfs(0, [])
    return print(result)

subset()