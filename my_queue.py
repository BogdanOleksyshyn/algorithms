class Node:
    def __init__(self, value, previous=None):
        self.value = value
        self.previous = previous
        self.next = next


class MyQueue:
    def __init__(self):
        self.size = 0
        self.top = None
        self.bottom = None

    def add_item(self, value):
        item = Node(value=value)
        if self.top is None:
            self.top = self.bottom = item
        else:
            item.previous = self.top
            self.top.next = item
            self.top = item

        self.size +=1

    def remove_item(self):
        if self.top == self.bottom == None:
            print("Queue is empty nothing to remove")
            return
        elif self.bottom == self.top:
            self.bottom = self.top = None
        else:
            self.bottom = self.bottom.next
        self.size -= 1

if __name__ == '__main__':
    my_queue = MyQueue()
    for i in range(1,6):
        my_queue.add_item(i)
    print('________')
    my_queue.remove_item()
    my_queue.remove_item()
    print()
    my_queue.remove_item()
    my_queue.remove_item()
    my_queue.remove_item()
    my_queue.remove_item()


