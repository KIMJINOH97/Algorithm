def solution(n, k, cmd):
    answer = ['O' for i in range(n)]

    class Node:
        def __init__(self, data):
            self.pre = 0
            self.data = data
            self.next = 0

    class LinkedList:
        def __init__(self, data):
            first = Node(data)
            self.head = first
            self.present = first
            self.tail = first
            self.stack = []

        def append(self, data):
            new_node = Node(data)
            new_node.pre = self.tail
            self.tail.next = new_node
            self.tail = new_node

        def delete(self):
            present = self.present
            preNode = present.pre
            nextNode = present.next

            self.stack.append(present)

            # 삭제노드가 첫번째 일 때
            if self.present == self.head:
                nextNode.pre = 0
                self.head = nextNode
                self.present = nextNode
            # 삭제노드가 마지막 일 때
            elif self.present == self.tail:
                preNode.next = 0
                self.tail = preNode
                self.present = preNode
            else:
                nextNode.pre = preNode
                preNode.next = nextNode
                self.present = nextNode

        def undo(self):
            node = self.stack.pop()

            if node.pre == 0:
                self.head.pre = node
                self.head = node
            elif node.next == 0:
                self.tail.next = node
                self.tail = node
            else:
                node.pre.next = node
                node.next.pre = node

        def down(self, cnt):
            for i in range(cnt):
                self.present = self.present.next

        def up(self, cnt):
            for i in range(cnt):
                self.present = self.present.pre

    link = LinkedList(0)

    for i in range(1, n):
        link.append(i)

    link.down(k)

    for cm in cmd:
        command = cm[0]

        if command == 'C':
            link.delete()
        elif command == 'Z':
            link.undo()
        elif command == 'U':
            link.up(int(cm[2:]))
        elif command == 'D':
            link.down(int(cm[2:]))

    s = link.stack
    while s:
        d = s.pop().data
        answer[d] = 'X'

    return ''.join(answer)
