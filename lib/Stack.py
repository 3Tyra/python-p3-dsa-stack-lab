class Stack:
    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
         return self.items == []

    def push(self, item):
        if (not self.full()):
            self.items.append(item)
        else:return None
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()
    def peek(self):
       return self.items[len(self.items)]
    def size(self):
        if self.isEmpty():
            return 0
        else:
            return len(self.items)

    def full(self):
        if len(self.items) == self.limit:
            return True
        else:
            return False

    def search(self, target):
       for i in reversed(range(len(self.items))):
           if self.items[i] == target:
               return len(self.items)-1- i
       return -1