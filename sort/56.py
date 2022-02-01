# 풀이 1: merge sort를 이용한 방식
def merge(interval_1, interval_2):
    arraylist = []
    i = j = 0

    while i < len(interval_1) and j < len(interval_2):
        if interval_1[i][0] < interval_2[j][0]:
            arraylist.append(interval_1[i])
            i += 1

        else:
            arraylist.append(interval_2[j])
            j += 1

    while i < len(interval_1):
        arraylist.append(interval_1[i])
        i += 1

    while j < len(interval_2):
        arraylist.append(interval_2[j])
        j += 1

    return arraylist


def mergesort(intervals):
    if len(intervals) <= 1:
        return intervals

    mid = len(intervals) // 2
    L = intervals[:mid]
    R = intervals[mid:]

    return merge(mergesort(L), mergesort(R))


def sort_intervals(arr):
    empty = []

    iters = len(arr) - 1
    for iter in range(iters):
        if arr[iter][0] <= arr[iter+1][1] and arr[iter][1] <= arr[iter+1][1]:
            empty.append(arr[iter+1])

        elif arr[iter][0] <= arr[iter+1][1] and arr[iter+1][1] <= arr[iter][1]:
            empty.append([arr[iter][0], arr[iter+1][1]])
            arr[iter+1] = [arr[iter][0], arr[iter+1][1]]

    return print(empty)

sort_intervals(mergesort([[1,3],[2,6],[8,10],[15,18]]))

# 풀이 2: sort 적용 후 현재 첫번째 값이 바로 이전 두번째 값보다 작을 경우 값을 바꿔주는 형식.
class Solution:
    def merge(self, intervals):
        merged = []
        for arr in sorted(intervals, key=lambda x: x[0]):
            if merged and arr[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], arr[1])

            else:
                merged.append(arr)

        return merged