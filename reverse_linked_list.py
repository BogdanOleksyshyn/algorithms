class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# [1,2,3,4,5] -> left 2, right 4 -> [1,4,3,2,5]
# [5] -> left 1 right 1 -> [5]

def reverse_list(head, left, right):
    reversed_linked_list = head
    if not head or left == right:
        return head

    dummy = ListNode(0, head)
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    stack = []
    current = prev.next

    for _ in range(right - left + 1):
        stack.append(current)
        current = current.next

    while stack:
        prev.next = stack.pop()
        prev = prev.next

    prev.next = current

    return dummy.next

if __name__ == '__main__':
    head1 = ListNode(1,
                     ListNode(2,
                              ListNode(3,
                                       ListNode(4,
                                                ListNode(5, None)))))
    left1 = 2
    right1 = 4
    head1_reversed = reverse_list(head1, left1, right1)

    head2 = ListNode(5, None)
    left2 = 1
    right2 = 1
    head2_reversed = reverse_list(head2, left2, right2)
    print()
