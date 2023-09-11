class Node:
    def __init__(self, value, next_node=None, previous_node=None):
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node


class LinkedList:
    def __init__(self):
        self.counter = 0
        self.head = None
        self.tail = None

    def add_head(self, value):
        current = Node(value=value)
        if self.head is None:
            self.head = self.tail = current
        else:
            self.head.previous_node = current
            current.next_node = self.head
            self.head = current
        self.counter += 1

    def add_tail(self, value):
        current = Node(value=value)
        if self.tail is None:
            self.head = self.tail = current
        else:
            self.tail.next_node = current
            current.previous_node = self.tail
            self.tail = current
        self.counter += 1

    def find_by_value(self, value):
        candidate = self.head
        for node in range(self.counter):
            if candidate.value == value:
                print(f"Value found in node {candidate}")
                return candidate
            candidate = candidate.next_node

    def delete_by_value(self, value):
        candidate = self.find_by_value(value)
        if candidate:
            if self.tail == self.head:
                self.tail = self.head = None
            elif candidate is not self.tail and candidate is not self.head:
                candidate.next_node.previous_node = candidate.previous_node
                candidate.previous_node.next_node = candidate.next_node
            elif candidate is self.head:
                candidate.next_node.previous_node = None
                self.head = candidate.next_node
            elif candidate is self.tail:
                candidate.previous_node.next_node = None
                self.tail = candidate.previous_node
            self.counter -= 1

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            iter_item = self.current
            self.current = self.current.next_node
            return iter_item.value



if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add_head(5)
    linked_list.add_head(4)
    linked_list.add_tail(6)
    linked_list.add_tail(7)
    print(linked_list.find_by_value(6).value)
    print("--------------")
    linked_list2 = LinkedList()
    for i in range(1, 6):
        linked_list2.add_tail(i)
    linked_list2.delete_by_value(3)
    linked_list2.delete_by_value(1)
    linked_list2.delete_by_value(5)
    print("************")
    # linked_list2.delete_by_value(2)
    # linked_list2.delete_by_value(4)
    # print("===========")
    iterator = iter(linked_list2)
    for i in iterator:
        print(i)
    linked_real_list = list(iterator)
    print(f"Linked list first element {linked_real_list[0]}")