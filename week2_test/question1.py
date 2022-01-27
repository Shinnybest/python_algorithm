def solution(dirs):
    steps = {
        "U": [0, 1],
        "D": [0, -1],
        "R": [1, 0],
        "L": [-1, 0]
    }

    arr = []
    cur = [0, 0]

    for i in range(len(dirs)):
        prev = cur
        move = [steps[dirs[i]][0], steps[dirs[i]][1]]
        cur = [prev[0] + move[0], prev[1] + move[1]]

        # x축, y축 다 -5 미만이거나 5 초과일 경우 움직이지 않고 머무른다.
        if cur[0] < -5 or cur[0] > 5 or cur[1] < -5 or cur[1] > 5:
            cur = prev
            continue

        # 이전 - 현재, 현재 - 이전은 같은 값이라 동시에 고려
        if [prev, cur] not in arr and [cur, prev] not in arr:
            arr.append([prev, cur])

    answer = len(arr)
    return answer

solution("ULURRDLLU")