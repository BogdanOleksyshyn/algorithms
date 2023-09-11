class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def cut_linked_list(head, size):
    sublist_head = head
    current = head
    for i in range(size-1):
        current = current.next if current else None

    sublist_tail = current.next if current else None
    if current:
        current.next = None

    return sublist_head, sublist_tail


def get_list_size(head):
    current = head
    list_size = 0
    while current:
        list_size += 1
        current = current.next
    return list_size


if __name__ == '__main__':
    head1 = ListNode(1,
                    ListNode(2,
                             ListNode(3,
                                      ListNode(4,
                                               ListNode(5,
                                                        ListNode(6,
                                                                 ListNode(7,
                                                                          ListNode(8,
                                                                                   ListNode(9,
                                                                                            ListNode(10,
                                                                                                     None))))))))))
    k1 = 3

    head2 = ListNode(1,
                    ListNode(2,
                             ListNode(3, None)))
    k2 = 5



    sublist_head1, sublist_tail1 = cut_linked_list(head1, 3)
    sublist_head2, sublist_tail2 = cut_linked_list(head2, 5)
    print()
