class Node:
    def __init__(self, value, next_node=None, previous_node=None):
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node


class LinkedList:
    def __init__(self, head = None, tail = None):
        self.counter = 0
        self.head = head
        self.tail = tail

    def add_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.previous_node = node
            node.next_node = self.head
            self.head = node
        self.counter += 1

    def add_tail(self, node):
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            node.previous_node = self.tail
            self.tail = node
        self.counter += 1

    def print_list_head_tale(self, from_node: Node):
        temp = from_node
        for i in range(self.counter):
            print(temp.value)
            temp = temp.next_node

    def find_from_head(self, value):
        from_node = self.head
        for node in range(self.counter):
            if value == from_node.value:
                print(f"We have value={value} in node={from_node}")
                return from_node
            else:
                pass
                # print(f"Value {value} is not present in node={from_node}")
            from_node = from_node.next_node

    def remove_item_from_head(self, value):

        deleted_node = self.find_from_head(value)
        if deleted_node:
            print(f"Removing value {value}")
            if not deleted_node.previous_node and not deleted_node.next_node:
                self.head = self.tail = None

            elif not deleted_node.previous_node:
                deleted_node.next_node.previous_node = deleted_node.previous_node
                self.head = deleted_node.next_node
            elif not deleted_node.next_node:
                deleted_node.previous_node.next_node = deleted_node.next_node
                self.tail = deleted_node.previous_node

            elif deleted_node.next_node and deleted_node.previous_node:
                deleted_node.next_node.previous_node = deleted_node.previous_node
                deleted_node.previous_node.next_node = deleted_node.next_node

            self.counter -= 1


if __name__ == "__main__":
    print("Linked list 1")
    linked_list = LinkedList()
    linked_list.add_tail(Node(value=5))
    linked_list.add_head(Node(value=4))
    linked_list.add_tail(Node(value=6))
    linked_list.add_tail(Node(value=7))
    linked_list.print_list_head_tale(from_node=linked_list.head)
    print("Linked list 2")
    linked_list2 = LinkedList()
    for i in range(1,6):
        linked_list2.add_tail(Node(i))
    linked_list2.print_list_head_tale(from_node=linked_list2.head)
    linked_list2.find_from_head(4)
    print("-----")

    linked_list2.remove_item_from_head(3)
    linked_list2.print_list_head_tale(from_node=linked_list2.head)

    linked_list2.remove_item_from_head(1)
    linked_list2.print_list_head_tale(from_node=linked_list2.head)
    linked_list2.remove_item_from_head(5)
    linked_list2.print_list_head_tale(from_node=linked_list2.head)
    linked_list2.remove_item_from_head(4)
    linked_list2.print_list_head_tale(from_node=linked_list2.head)
    linked_list2.remove_item_from_head(2)
    print(f"linked_list2 head {linked_list2.head}, tail {linked_list2.tail}")
    print("******")
