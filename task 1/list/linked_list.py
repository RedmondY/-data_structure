class LNode(object):
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


class LList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def insert(self, index, elem):
        if index > self.len:
            raise IndexError('Out of range')
        else:
            node = Node(elem)
            if index == 0:
                node.next = self._head
                self._head = node
            elif index == self.len:
                self.append(elem)
            else:
                head = self._head
                cur_index = 0
                while head:
                    if cur_index + 1 == index:
                        nex = head.next
                        head.next = node
                        node.next = nex
                        break
                    cur_index += 1
                    head = head.next
        self.len += 1
