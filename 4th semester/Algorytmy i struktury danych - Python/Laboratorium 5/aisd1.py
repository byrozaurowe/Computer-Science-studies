import heapq as h

class QueueItem:
    def __init__(self, value, priority):
        self.value = value
        self._priority = priority
        self.queue = None
        self.sec_vert = None

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority):
        self._priority = priority
        self.queue.rebuild_queue()

    def set_queue(self, queue):
        self.queue = queue

    def __int__(self):
        return self.priority

    def __lt__(self, other):
        return self._priority < other.priority

    def __str__(self):
        return self.name

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        h.heappush(self.queue, item)
        item.set_queue(self)
        return self

    def rebuild_queue(self):
        h.heapify(self.queue)

    def __len__(self):
        return len(self.queue)

    def top(self):
        return self.queue[0].value
    
    def pop(self):
        return h.heappop(self.queue)

    def priority(self, value, priority):
        iterator = iter(self.queue)
        for item in self.queue:
            if item.value == value and item.priority > priority:
                item.priority = priority

    def print(self):
        for item in self.queue:
            print("(" + str(item.value) + ", " + str(item.priority) + ") ", end='')

def main():
    M = int(input())
    operacja = []
    q = PriorityQueue()
    for i in range(M):
        operacja = input().split()
        if operacja[0] == "insert":
            item = QueueItem(int(operacja[1]), int(operacja[2]))
            q.enqueue(item)
        if operacja[0] == "empty":
            if q.__len__() == 0:
                print("1")
            else:
                print("0")
        if operacja[0] == "top":
            if q.__len__() > 0:
                print(q.top())
            else:
                print()
        if operacja[0] == "pop":
            if q.__len__() > 0:
                print(q.pop().value)
            else:
                print()
        if operacja[0] == "priority":
            q.priority(int(operacja[1]), int(operacja[2]))
        if operacja[0] == "print":
            q.print()
            print()

            


if __name__ == "__main__":
    main()