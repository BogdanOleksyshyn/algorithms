class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_size(head):
    current = head
    size = 0
    while current:
        size += 1
        current = current.next
    return size


if __name__ == '__main__':
    head = None
    head1 = ListNode(val=1)

    head10 = ListNode(1,
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
    print(get_size(head))
    print(get_size(head1))
    print(get_size(head10))