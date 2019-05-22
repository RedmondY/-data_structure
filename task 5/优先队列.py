Left = lambda x: 2 * x + 1
Right = lambda x: 2 * x + 2


class PriorityQueue:
    def __init__(self, queue):
        self.queue = queue
        if self.queue:
            self.build_heap()
        self.heap_size = 0

    def put(self, key, value):
        self.queue.append((key, value))
        self.build_heap()

    def get(self):
        if self.heap_size > 0:
            target = self.queue.pop(0)[1]
            self.build_heap()
            return target
        else:
            print("IndexError: pop from empty list")
            return

    def peek(self):
        if self.heap_size > 0:
            return self.queue.pop(0)[1]
        else:
            print("IndexError: pop from empty list")
            return

    def build_heap(self):
        self.heap_size = len(self.queue)
        for i in range(self.heap_size // 2 - 1, -1, -1):
            self.min_heap(i)

    def min_heap(self, i):
        while True:
            left = Left(i)
            right = Right(i)

            if right < self.heap_size and self.queue[right][0] < self.queue[i][0]:
                min_index = right
            else:
                min_index = i

            if left < self.heap_size and self.queue[left][0] < self.queue[min_index][0]:
                min_index = left
            else:
                pass

            if min_index == i:
                break
            self.queue[i], self.queue[min_index] = self.queue[min_index], self.queue[i]

            i = min_index


if __name__ == "__main__":
    queue = [(1, 2), (1, 2), (2, 3), (3, 4)]
    PQ = PriorityQueue(queue)
    # print(PQ.peek())
    PQ.put(5, 6)
    PQ.put(0, 1)
    # print(PQ.peek())
    print(PQ.get())
    print(PQ.get())
    print(PQ.get())
    print(PQ.get())
    print(PQ.get())
    print(PQ.get())
    print(PQ.get())


