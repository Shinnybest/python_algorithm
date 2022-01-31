# 풀이 1: SelectionSort
# 가장 왼쪽부터 minimum을 차곡차곡 쌓아나가는 방식
def sortColors(nums):
    iters = len(nums) - 1 # iters = 마지막 요소의 인덱스 값
    for iter in range(iters):
        minimum = iter
        for cur in range(iter+1, len(nums)):
            if nums[cur] < nums[minimum]:
                minimum = cur
        if minimum != iter:
            nums[minimum], nums[iter] = nums[iter], nums[minimum]

    print(nums)

# 풀이 2: Counter 활용
# 딕셔너리형의 key와 value 값을 이용하여 문제를 풀어준다.
import collections
def sortColors(nums):
    c = collections.Counter(nums)
    print(c) # Counter({2: 2, 0: 2, 1: 2})
    print(c[0]) # 2
    print(c[1]) # 2
    print(c[2]) # 2

    for i in range(c[0]):            # for i in range(2):
        nums[i] = 0                  # nums[0] = 0, nums[1] = 1
    for j in range(c[1]):            # for i in range(2):
        nums[j + c[0]] = 1           # nums[0 + 2] = 1, nums[1 + 2] = 1
    for w in range(c[2]):            # for i in range(2):
        nums[w + c[0] + c[1]] = 2    # nums[0 + 2 + 2] = 2, nums[1 + 2 + 2] = 2

    print(nums) # [0, 0, 1, 1, 2, 2]

# 풀이 3: 1을 pivot 으로 sort
def sortColors(nums):
    left = -1
    right = 0
    wall = len(nums)

    while right < wall: # right 오른쪽으로 한칸씩 이동 -> wall 값과 같아지면 while 문 탈출!
        # 1을 기준으로 잡을 수 있는 것은 해당 문제에서 값이 0(1보다 작음), 1, 2(1보다 큼) 밖에 없기 때문이다.
        if nums[right] > 1:
            wall -= 1
            nums[wall], nums[right] = nums[right], nums[wall]

        elif nums[right] < 1:
            left += 1 # 0이 들어갈 공간을 하나 만들어준다.
            nums[left], nums[right] = nums[right], nums[left]
            right += 1 # 오른쪽으로 한칸 이동해준다.
        else:
            right += 1

    print(nums)

# 풀이 2와 비교 & 참고
def sortColors(nums):
    a = 0
    b = 0
    c = 0

    for num in range(len(nums)):
        if nums[num] == 0:
            a += 1
        if nums[num] == 1:
            b += 1
        if nums[num] == 2:
            c += 1
    for i in range(a):
        nums[i] = 0
    for i in range(b):
        nums[i + a] = 1
    for i in range(c):
        nums[i + a + b] = 2

    print(nums)


arr = [2, 0, 1, 1, 2, 0]
sortColors(arr)