class Node:
    def __init__(self, value, previous=None):
        self.value = value
        self.previous = previous


class Stack:
    def __init__(self):
        self.size = 0
        self.bottom = None
        self.top = None

    def add_element(self, value):
        item = Node(value)
        if self.top is None:
            self.bottom = self.top = item
        else:
            item.previous = self.top
            self.top = item

        self.size += 1

    def remove_element(self):
        if self.top == self.bottom == None:
            print('Stack is empty, nothing to remove')
            return
        elif self.top == self.bottom:
            self.top = self.bottom = None
        elif self.top:
            self.top = self.top.previous
        self.size -=1

if __name__ == "__main__":
    stack = Stack()
    for i in range(1,6):
        stack.add_element(i)
    print("_______")
    for i in range(3):
        stack.remove_element()
    stack.remove_element()
    stack.remove_element()
    print()
    stack.remove_element()
