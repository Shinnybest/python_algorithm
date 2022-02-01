# 머지소트
def merge(lst1, lst2):
    arr = []
    i = j = 0

    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            arr.append(lst1[i])
            i += 1

        else:
            arr.append(lst2[j])
            j += 1

    while i < len(lst1):
        arr.append(lst1[i])
        i += 1

    while j < len(lst2):
        arr.append(lst2[j])
        j += 1

    return arr


def mergeSort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    L_sorted = lst[:mid]
    R_sorted = lst[mid:]

    return merge(mergeSort(L_sorted), mergeSort(R_sorted))


assert mergeSort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]
assert mergeSort([3, 2, 1, 5, 3, 2, 3]) == [1, 2, 2, 3, 3, 3, 5]