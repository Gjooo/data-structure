from listNode import ListNode

class LinkedList:
    def __init__(self):
        self.__head = ListNode('dummy', None)  # ����Ʈ�� ù ��° ��带 ����Ű�� ������
        self.__numItems = 0  # ����Ʈ�� ũ��

    def isEmpty(self):
        """����Ʈ�� ����ִ� ���� �˷��ִ� �Լ�
        
        Returns -> bool:
            ����Ʈ�� ���Ұ� 0�̸� True, �̿ܿ��� False
        """
        return (self.__numItems == 0)

    def getSize(self):
        """����Ʈ�� ũ�⸦ ��ȯ�ϴ� �Լ�

        Returns -> int:
            ����Ʈ�� ���� ����
        """
        return self.__numItems

    def clear(self):
        """����Ʈ�� ���� �Լ�
        
        Returns -> None:
        """
        self.__head = ListNode("dummy", None)
        self.__numItems = 0
        return None

    def append(self, newItem):
        """����Ʈ�� �������� ���ο� ���Ҹ� �߰��ϴ� �Լ�
        Args:
            newItem: �߰��� ����
        Returns -> None:
        """
        newNode = ListNode(newItem, self.__head)  # �� ��带 ����
        self.__head.next = newNode  # �� ��带 ����Ʈ�� ù ��° ���� ����
        self.__numItems += 1  # ����Ʈ ũ�� ����

    def insert(self, newItem, index):
        """����Ʈ�� Ư�� ��ġ�� ���ο� ���Ҹ� �����ϴ� �Լ�
        Args:
            newItem: ������ ����
            index: ������ ��ġ (0���� ����)
        Returns -> None:
        """
        if index < 0 or index > self.__numItems:
            raise IndexError("Index out of bounds")
        newNode = ListNode(newItem, None)
        if index == 0:
            self.__head.next = newNode  # �� ��带 ����Ʈ�� ù ��° ���� ����
            self.__numItems += 1
        else:
            current = self.__head.next # List ��ȸ
            for i in range(index - 1):
                current = current.next
            # current�� index-1��° ��带 ����Ŵ
            newNode.next = current.next
            current.next = newNode
            # �� ��带 index ��ġ�� ����

        self.__numItems += 1  # ����Ʈ ũ�� ����
        return newItem

    def pop(self, index):
        """����Ʈ���� Ư�� ��ġ�� ���Ҹ� �����ϰ� ��ȯ�ϴ� �Լ�
        Args:
            index: ������ ������ ��ġ (0���� ����)
        Returns -> item:
            ���ŵ� ����
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
            # current�� index-1��° ��带 ����Ŵ
        item = current.next.item
        current.next = current.next.next
        self.__numItems -= 1
        return item

    def remove(self, item):
        """����Ʈ���� Ư�� ���Ҹ� �����ϴ� �Լ�
        Args:
            item: ������ ����
        Returns -> item:
            ���ŵ� ����
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
        """����Ʈ���� Ư�� ��ġ�� ��带 ��ȯ�ϴ� �Լ�
        Args:
            index: ��带 ã�� ��ġ (0���� ����)
        Returns -> ListNode:
            Ư�� ��ġ�� ���
        """
        if self.__isEmpty:
            return None
        current = self.__head.next
        for i in range(index):
            current = current.next

    def get(self, index:int):
        """����Ʈ���� Ư�� ��ġ�� ���Ҹ� ��ȯ�ϴ� �Լ�
        Args:
            index: ���Ҹ� ã�� ��ġ (0���� ����)
        Returns -> item:
            Ư�� ��ġ�� ����
        """
        if self.isEmpty:
            return None
        if (index>=0 and index<=self.__numItems -1):
            return self.__getnode(i).item
        else:
            return None

    def index(self, x):
        """����Ʈ���� Ư�� ������ �ε����� ��ȯ�ϴ� �Լ�
        Args:
            x: ã�� ����
        Returns -> int:
            ������ �ε��� (0���� ����), ���Ұ� ������ None
        """
        current = self.__head.next
        for i in range(self.__numItems):
            if current.item == x:
                return i
            current = current.next
        return None

