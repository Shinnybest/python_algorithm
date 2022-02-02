import collections
import re

# 리스트로 변환
# 문자열을 입력받아서 팰린드롬 여부를 확인하는데,
# 1. 대소문자 구분X, 2. 숫자, 영문자만 취급한다는 조건 먼저 고려해준다.
def findPalin(s):
    # 하나의 문자열을 리스트로 변환하기 위해서 빈 리스트 값을 먼저 둔다.
    str = []
    # 문자열의 값들을 하나씩 살펴보기 위해서 for char in s를 해준다.
    for char in s:
        # 만약 숫자+알파벳이라면
        if char.isalnum():
            # 그걸 소문자로 다 바꿔서 넣어준다.
            str.append(char.lower())
    # 양쪽에서 다 없애면 만일 짝수 개수였으면 len이 0이 될거고, 홀수였으면 1이 될거니까 len(str)가 2일 때까지 계속 연산해주어야 한다.
    while (len(str) > 1):
        # 왼쪽에서 빼낸 거와 오른쪽에서 빼낸 거가 다르면 팰린드롬이 아니다. return False해준다.
        if str.pop(0) != str.pop():
            return False
    # 별일없다면 palindrome은 true값을 가지게 된다.
    return True

# 데크 자료형을 위한 최적화
# 큐는 선입선출 방식으로 작동하지만 데크는 양방향 큐이다.
# 즉, 앞, 뒤 방향에서 element를 추가하거나 삭제할 수 있다.
def isPalin(s):
    # 콜렉션을 써서 deque를 하나 만들어준다.
    d = collections.deque()

    # 문자열을 하나의 리스트로 바꿔서 해주는 것은 동일하다.
    for char in s:
        if char.isalnum():
            d.append(char.lower())

    # 데큐를 썼기 때문에 pop(0)은 popleft로 바뀔 수 있다.
    while (len(d) > 1):
        if str.popleft() != str.pop():
            return False

    return True

# Deque기능을 활용하면 속도가 위에 것보다 5배 가까이 빨라지는데 그 이유는,
# pop(0)이 O(n)인 데 반해, 데크의 popleft()는 O(1)이기 때문이다.

# 슬라이싱을 사용
def useSlicing(s):
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)
    print(s) # amanaplanacanalpanama
    print(s[::-1]) # reverse 즉 s의 값을 역순으로 뒤집은 것이다.

    return print(s == s[::-1])

if __name__ == "__main__":
    useSlicing('a man, a plan, a canal: Panama')