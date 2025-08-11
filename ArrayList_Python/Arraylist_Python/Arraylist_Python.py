from list.listNode import ListNode

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
        return self.__numItems

    def clear(self):
        self.__head = ListNode("dummy", None)
        self.__numItems = 0

    def append(self, newItem):
        newNode = ListNode(newItem, self.__head)  # 새 노드를 생성
        self.__head.next = newNode  # 새 노드를 리스트의 첫 번째 노드로 설정
        self.__numItems += 1  # 리스트 크기 증가

    def insert(self, newItem, index):
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
        if self.__isEmpty:
            return None
        current = self.__head.next
        for i in range(index):
            current = current.next

    def get(self, index:int):
        if self.isEmpty:
            return None
        if (index>=0 and index<=self.__numItems -1):
            return self.__getnode(i).item
        else:
            return None

    def index(self, x):
        current = self.__head.next
        for i in range(self.__numItems):
            if current.item == x:
                return i
            current = current.next

        return None
    
