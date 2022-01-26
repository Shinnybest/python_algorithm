from collections import defaultdict

def findMinTreeHeight(n, edges):
    # 0. 만일 n의 값이 1이면 [0] 리스트 하나만 반환해준다.
    if n == 1:
        return [0]

    # 1. 리스트로 주어진 그래프를 딕셔너리로 만든다. 무방향이기 때문에 인접행렬과 같은 형식으로 만들어준다.
    graph = defaultdict(list)

    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)

    # 2. 리프노드부터 계속 제거를 해줘야 한다. 리프노드는 해당 키 값의 밸류 길이가 1인 점을 이용한다.
    leaves = []
    for x in graph:
        if len(graph[x]) == 1:
            leaves.append(x)

    # 해당 키 값들을 하나의 빈 리스트에 담고, 그 리스트의 밸류값을 키 값으로 가지는 graph의 요소들을 삭제해준다.
    # n의 개수가 2 이하가 될 때까지 반복
    while n>2:
        n -= len(leaves) # 내가 생각하지 못한 부분
        new_leaves = []
        for y in leaves:
            # value 길이가 1인 key 값의 value를 pop해서 ele에 담아준다.
            ele = graph[y].pop()
            # 똑같은 값을 찾아서 제거해준다.
            graph[ele].remove(y)

            # key값이 ele인 value 리스트에서 y 요소를 삭제해줌으로써 value 길이가 1이된 것들의 key 값을 다시 new_leaves라는 새로운 list에 담아준다.
            if len(graph[ele]) == 1:
                new_leaves.append(ele)
        leaves = new_leaves # 내가 생각하지 못한 부분 (중요! 문제풀이 tip)
                            # 새롭게 만든 리스트를 leaves 변수에 담아준다. -> 이를 통해 while 안에서 for문을 재사용할 수가 있게 된다.
    # 3. 마지막에 len이 1인 key 값들을 반환해준다. leaves 리스트의 요소 개수는 1개 혹은 2개이다.
    return leaves

# example
arr = [[0, 1], [1, 2], [2, 3], [3, 4], [1, 5]]
# 딕셔너리 형태로 보여줄 경우
# {0: [1], 1:[0, 2, 5], 2: [1, 3], 3: [2, 4], 4: [3], 5: [1]}

findMinTreeHeight(6, arr)