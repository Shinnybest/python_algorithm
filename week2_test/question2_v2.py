def solution(numbers, target):
    answer = 0
    n = len(numbers)

    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1

        else:
            # 가지치기처럼 모든 경우의 수를 계산해준다.
            dfs(idx + 1, result - numbers[idx])
            dfs(idx + 1, result + numbers[idx])

    # result 0부터 시작하고 idx 가 0이어야 13, 14줄에서 numbers 의 첫번째 값부터 +/-를 모두 고려한 가지치기가 나온다.
    dfs(0, 0)

    return answer