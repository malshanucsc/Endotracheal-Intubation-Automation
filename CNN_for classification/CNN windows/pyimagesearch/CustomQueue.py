class CustomQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        if (len(self.items) >= 20):
            self.items.pop(0)
            self.items.append(item)
        else:
            self.items.append(item)

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def dequeue(self):
        return self.items.pop(0)
    def getMax(self):
        print(self.items)
        return max(self.items,key=self.items.count)