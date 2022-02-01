import sys

N = int(sys.stdin.readline())

lst = []

for i in range(N):
    lst.append(str(sys.stdin.readline().rstrip()))
    # rstrip()을 해주지 않으면 \n이 함께 출력된다.

lst = set(lst) # 중복숫자 제거
lst = list(lst) # 다시 리스트형으로 반환
lst.sort() # sort를 먼저 함으로써 사전순 배열이 되도록 한다.
lst.sort(key = lambda x: len(x)) # 이미 사전순 배열이 마친 상태에서 길이가 짧은 것 먼저 앞으로 보내준다.
                                 # Timsort => merge sort + insertion sort 와 연관이 있을 것 같다.
for i in lst:
    print(i)