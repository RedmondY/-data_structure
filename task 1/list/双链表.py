class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.pre = None


class LinkList(object):
    def __init__(self):
        """初始化链表"""
        self.head = None
        self.tail = None
        self.len = 0

    def append(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            pre = self.head
            while pre.next:
                pre = pre.next
            pre.next, node.pre = node, pre
        self.tail = node
        self.len += 1

    def insert(self, index, val):
        if index > self.len:
            raise IndexError('Out of range')
        else:
            node = Node(val)
            if index == 0:
                node.next, self.head.pre = self.head, node
                self.head = node
            elif index == self.len:
                self.append(val)
            else:
                head = self.head
                cur_index = 0
                while head:
                    if cur_index + 1 == index:
                        nex = head.next
                        head.next, node.pre = node, head
                        node.next, nex.pre = nex, node
                        break
                    cur_index += 1
                    head = head.next
        self.len += 1

    def delete(self, index):
        if index >= self.len:
            raise IndexError("Out of range")
        else:
            if index == 0:
                self.head = self.head.next
                self.head.pre = None
            else:
                head = self.head
                cur_index = 0
                while head:
                    if cur_index + 1 == index:
                        if index == self.len - 1:
                            head.next = None
                            self.tail = head
                        else:
                            head.next = head.next.next
                            head.next.pre = head
                        break
                    cur_index += 1
                    head = head.next


linkList = LinkList()
linkList.append(6)
linkList.append(7)
linkList.insert(0, 1)
linkList.delete(1)
head = linkList.head
tail = linkList.tail

while head:
    print(head.val)
    head = head.next

while tail:
    print(tail.val)
    tail = tail.pre
