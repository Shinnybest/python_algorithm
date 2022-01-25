from collections import deque
from prac import make_tree_by

def test_max_depth(lst):
    root = make_tree_by(lst, 0) # return 값은 결국 parent <-
    if not root: # parent 값이 None 이라면
        return 0 # return 0을 해준다.

    q = deque([root])
    # print(q)
    # q = deque([Treenode(lst[0])])
    depth = 0

    while q:
        depth += 1
        for _ in range(len(q)):
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    return depth


assert test_max_depth(lst=[]) == 0
assert test_max_depth(lst=[3, 9, 20, None, None, 15, 7]) == 3