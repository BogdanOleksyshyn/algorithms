class Node:
    def __init__(self, value, next_node=None, previous_node=None):
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node

class SortedLinkedList:
    def __init__(self):
        self.counter = 0
        self.head = self.tail = None

    def add(self, value):
        current_node= Node(value)
        if self.head is None:
            self.head = self.tail = current_node
        elif current_node.value <= self.head.value:
            self.head.previous_node = current_node
            current_node.next_node = self.head
            self.head = current_node
        elif current_node.value >= self.tail.value:
            self.tail.next_node = current_node
            current_node.previous_node = self.tail
            self.tail = current_node
        else:
            cursor = self.head
            for i in range(self.counter-1):
                cursor = cursor.next_node
                if value <= cursor.value:
                    current_node.next_node = cursor
                    current_node.previous_node = cursor.previous_node
                    cursor.previous_node.next_node = current_node
                    cursor.previous_node = current_node
                    break

        self.counter += 1


if __name__ == "__main__":
    linked_list = SortedLinkedList()
    for i in [3,4, 5, 2, 3.5]:
        linked_list.add(i)
    print('_________')