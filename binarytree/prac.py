from structures import TreeNode

def make_tree_by(lst, idx): # 리스트에 인덱스를 부여해서 하나의 트리를 만드는 함수
    # parent 변수에 None 값을 담는다.
    parent = None
    # 만일 리스트의 길이보다 인덱스가 작다면
    if idx < len(lst):
        # 리스트의 인덱스를 밸류값에 담는다.
        value = lst[idx]
        # 만일 밸류값이 None 이라면 None 값을 return 한다.
        if value is None:
            return
        # Treenode 라는 클래스의 value 값을 넣고 그걸 parent 라고 한다.
        parent = TreeNode(value)
        # parent의 left는 리스트에 인덱스 값을 2idx + 1 해주는 것
        parent.left = make_tree_by(lst, 2 * idx + 1)
        # parent의 right는 리스트에 인덱스 값을 2idx + 2 해주는 것
        parent.right = make_tree_by(lst, 2 * idx + 2)

    return parent, lst # Treenode(lst[idx])