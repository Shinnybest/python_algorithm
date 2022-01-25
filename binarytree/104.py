# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        # print(root)
        # TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None},
        # right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}
        if not root:
            return 0

        q = deque([root]) # 데크에는 iterable한 형태만 들어갈 수 있어서 root를 꼭 리스트로 감싸주어야 한다.

        depth = 0

        while q:
            # print(q)
            # deque([TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None},
            # right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}])
            depth += 1
            for _ in range(len(q)):
                cur = q.popleft()
                # 여기서 q의 값이 하나이기 때문에 popleft 를 하면 cur 은 q의 유일한 TreeNode 값이 된다.
                # TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None},
                # right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return depth