import heapq

from heap.structures import BinaryMaxHeap


def t_maxheap_we_made(lst, k):
    maxheap = BinaryMaxHeap()

    # for 문 : 힙정렬 시간복잡도 계산의 토대
    for elem in lst:
        maxheap.insert(elem)

    return [maxheap.extract() for _ in range(k)][k - 1]


def t_maxheap_heapq(lst, k):
    return heapq.nlargest(k, lst)[-1]


assert t_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 1) == 6
assert t_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 2) == 5
assert t_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 3) == 5
assert t_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
assert t_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 5) == 3
assert t_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 6) == 3
assert t_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 7) == 2
assert t_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 8) == 2
assert t_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 9) == 1


assert t_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 1) == 6
assert t_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 2) == 5
assert t_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 3) == 5
assert t_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
assert t_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 5) == 3
assert t_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 6) == 3
assert t_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 7) == 2
assert t_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 8) == 2
assert t_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 9) == 1