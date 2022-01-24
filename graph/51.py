def nqueens(n):

    # 인덱스의 값을 row, 해당 값을 colume 값으로 하는 하나의 리스트를 만든다.
    # 시간 복잡도가 O(n^2)인 이중 행렬보다 시간복잡도가 O(n)이 되어서 더 빠르다.
    # 또 하나의 장점은 같은 행(row)에 두개가 중복되는 것은 방지해주는 효과가 있다.
    visited = [-1] * n
    # 문제의 답과는 상관 없지만 print 값을 출력할 때 좋다.
    cnt = 0
    # visited -> List(List(str)) -> str 로 값 변환을 해줘야 하기 때문에 우선 answer는 빈 리스트로 해둔다.
    answer = []


    # 백트레킹을 위한 함수이다.
    def check(nth_row):
        for row in range(nth_row):
            # 만약에 이전 row 값과 같거나(즉, 같은 colume에 위치하거나), 대각선의 값이 같으면 false를 반환
            # 대각선의 경우 뒷 부분은 음수가 나올 수 있어서 절대값을 붙여주었다.
            if visited[nth_row] == visited[row] or (nth_row - row) == abs(visited[nth_row] - visited[row]):
                return False
        return True

    def dfs(row):
        if row >= n:
            nonlocal cnt
            cnt += 1
            print("*" * 80)
            print(f"{cnt}번째 답 - visited: {visited}")
            grid = [['.'] * n for _ in range(n)]  # index의 의미가 없이 그냥 0 ~ n-1까지 돌린다.
            for idx, value in enumerate(visited):
                grid[idx][value] = 'Q'
            result = []
            for row in grid:
                print(row)
                result.append(''.join(row))
            answer.append(result)
            return

        # 0부터 (n-1)까지 계속 반복문을 돌려준다.
        for col in range(n):
            visited[row] = col
            if check(row) is True:
                dfs(row + 1)

    dfs(0)
    return print(answer)

nqueens(4)
