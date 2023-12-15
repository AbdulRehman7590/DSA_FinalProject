class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, item, priority):
        # Insert the item with its priority in the correct position
        index = 0
        while index < len(self.queue) and self.queue[index][0] <= priority:
            index += 1
        self.queue.insert(index, (priority, item))

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty priority queue")
        _, item = self.queue.pop(0)
        return item

    def is_empty(self):
        return len(self.queue) == 0

# Example usage:
pq = PriorityQueue()
pq.push("Task 1", 3)
pq.push("Task 2", 1)
pq.push("Task 3", 2)
pq.push("Most Important",0)
while not pq.is_empty():
    print(pq.pop())
