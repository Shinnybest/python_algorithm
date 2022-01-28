class BinaryMaxHeap:
    def __init__(self):
        # 첫번째 요소를 None 으로 만들어준다.
        self.items = [None]

    def __len__(self):
        # override
        # underscore 로 둘러싸여 있는 함수의 경우, magic function 이라고 부르는데 모든 함수에 적용이 되는 함수라는 뜻
        # 여기서 len 의 경우 python 내장함수라 자동으로 배열 길이를 구해주지만 여기서는 인덱스 1부터 사용하기로 해서,
        # len(배열)에서 1을 빼준 것을 len 으로 설정하도록 하는 magic 함수를 만들어야 한다.
        return len(self.items) - 1

    def _percolate_up(self):
        cur = len(self)
        # left 라면 2 * cur, right 라면 2 * cur + 1 이므로 parent 는 항상 cur // 2
        parent = cur // 2 # parent 는 부모의 인덱스 값

        # 루트노드까지 만일 현재 노드의 값이 부모노드보다 크다면 계속 그 값을 바꿔주고 인덱스 값도 바꿔준다.
        while parent > 0:
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        biggest = cur
        # 위에서 인덱스 1부터 시작하기 때문에 left, right 값이 이렇게 가능
        left = 2 * cur
        right = 2 * cur + 1

        # 자식노드가 더 크다면 자리를 바꿔준다.
        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left

        # 더 큰 자식노드와 자리를 바꾼다.
        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right

        if biggest != cur:
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            self._percolate_down(biggest)


    def insert(self, k):
        # k 값을 가장 마지막에 넣어주고 위로 한단계씩 올려준다.
        self.items.append(k)
        self._percolate_up()


    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        # 마지막 노드를 루트 노드 자리에 올려준다.
        self.items[1] = self.items[-1]
        # 원래 루트노드였던 가장 마지막에 위치한 노드를 pop 해준다.
        self.items.pop()
        # 루트 노드부터 시작해서 max heap 의 정의에 맞는 위치를 찾아 내려간다.
        self._percolate_down(1)

        return root # return 값은 원래 root 노드였던 것을 반환해주도록 한다.