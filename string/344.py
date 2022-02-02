from collections import deque

# 일종의 투포인터 활용한 스왑형식
def reverseWords(s):
    # left는 0항이고 right은 len(s) - 1항이다. 처음부터 끝까지 표시한 것
    left, right = 0, len(s) - 1
    # 아직 right이 left보다 크면
    if left < right:
        # 그 값을 다 바꿔준다
        s[left] = s[right]
        # 그리고 left는 오른쪽으로 한칸씩 이동하고
        left += 1
        # right은 왼쪽으로 한칸씩 이동한다.
        right -= 1


# 단어를 예를 들어서
# apple이라고 치면
# reverseword = a + ''
# reverseword = p + a
# reverseword = p + pa
# reverseword = l + ppa
# reverseword = e + lppa

def reverse(s):
    reverseword = ""
    for char in s:
        reverseword = char + reverseword

    reverseword = list(reverseword)

# 리스트에 reverse를 해주면 역순으로 출력된다.
def rev(s):
    s.reverse()

# [::-1]을 리스트값에 적용하면 해당 리스트가 역순으로 출력된다.
def flip(s):
    s = s[::-1]

arr_in = ['a', 'p', 'p', 'l', 'e']