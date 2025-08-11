from listNode import ListNode

class LinkedList:
    def __init__(self):
        self.__head = ListNode('dummy', None)  # 리스트의 첫 번째 노드를 가리키는 포인터
        self.__numItems = 0  # 리스트의 크기

    def isEmpty(self):
        """리스트가 비어있는 지를 알려주는 함수
        
        Returns -> bool:
            리스트의 원소가 0이면 True, 이외에는 False
        """
        return (self.__numItems == 0)

    def getSize(self):
        """리스트의 크기를 반환하는 함수

        Returns -> int:
            리스트의 원소 개수
        """
        return self.__numItems

    def clear(self):
        """리스트를 비우는 함수
        
        Returns -> None:
        """
        self.__head = ListNode("dummy", None)
        self.__numItems = 0
        return None

    def append(self, newItem):
        """리스트의 마지막에 새로운 원소를 추가하는 함수
        Args:
            newItem: 추가할 원소
        Returns -> None:
        """
        newNode = ListNode(newItem, self.__head)  # 새 노드를 생성
        self.__head.next = newNode  # 새 노드를 리스트의 첫 번째 노드로 설정
        self.__numItems += 1  # 리스트 크기 증가

    def insert(self, newItem, index):
        """리스트의 특정 위치에 새로운 원소를 삽입하는 함수
        Args:
            newItem: 삽입할 원소
            index: 삽입할 위치 (0부터 시작)
        Returns -> None:
        """
        if index < 0 or index > self.__numItems:
            raise IndexError("Index out of bounds")
        newNode = ListNode(newItem, None)
        if index == 0:
            self.__head.next = newNode  # 새 노드를 리스트의 첫 번째 노드로 설정
            self.__numItems += 1
        else:
            current = self.__head.next # List 순회
            for i in range(index - 1):
                current = current.next
            # current는 index-1번째 노드를 가리킴
            newNode.next = current.next
            current.next = newNode
            # 새 노드를 index 위치에 삽입

        self.__numItems += 1  # 리스트 크기 증가
        return newItem

    def pop(self, index):
        """리스트에서 특정 위치의 원소를 제거하고 반환하는 함수
        Args:
            index: 제거할 원소의 위치 (0부터 시작)
        Returns -> item:
            제거된 원소
        """
        if index < 0 or index >= self.__numItems:
            raise IndexError("Index out of bounds")
        if index == 0:
            item = self.__head.next.item
            self.__head.next = self.__head.next.next
            self.__numItems -= 1
            return item
        current = self.__head.next()
        for i in range(index - 1):
            current = current.next
            # current는 index-1번째 노드를 가리킴
        item = current.next.item
        current.next = current.next.next
        self.__numItems -= 1
        return item

    def remove(self, item):
        """리스트에서 특정 원소를 제거하는 함수
        Args:
            item: 제거할 원소
        Returns -> item:
            제거된 원소
        """
        current = self.__head.next
        previous = self.__head
        while current is not None:
            if current.item == item:
                previous.next = current.next
                self.__numItems -= 1
                return item
            previous = current
            current = current.next
        raise ValueError("Item not found in the list")

    def __getnode(self, index:int):
        """리스트에서 특정 위치의 노드를 반환하는 함수
        Args:
            index: 노드를 찾을 위치 (0부터 시작)
        Returns -> ListNode:
            특정 위치의 노드
        """
        if self.__isEmpty:
            return None
        current = self.__head.next
        for i in range(index):
            current = current.next

    def get(self, index:int):
        """리스트에서 특정 위치의 원소를 반환하는 함수
        Args:
            index: 원소를 찾을 위치 (0부터 시작)
        Returns -> item:
            특정 위치의 원소
        """
        if self.isEmpty:
            return None
        if (index>=0 and index<=self.__numItems -1):
            return self.__getnode(i).item
        else:
            return None

    def index(self, x):
        """리스트에서 특정 원소의 인덱스를 반환하는 함수
        Args:
            x: 찾을 원소
        Returns -> int:
            원소의 인덱스 (0부터 시작), 원소가 없으면 None
        """
        current = self.__head.next
        for i in range(self.__numItems):
            if current.item == x:
                return i
            current = current.next
        return None

