# List의 Node를 정의하는 클래스

class ListNode:
    def __init__(self, newItem, nextNode:'ListNode'):
        self.item = newItem  # 노드에 저장할 아이템
        self.next = nextNode  # 다음 노드를 가리키는 포인터