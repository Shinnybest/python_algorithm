# 내가 푼 풀이
n, k = map(int, input().split())

answer = 0
while n >= 1:
    if n % k == 0:
        n = n / k
    else:
        n = n - 1
    answer += 1

answer = answer -1

print(answer)

# 답지 풀이
n, k = map(int, input().split())
result = 0


while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)