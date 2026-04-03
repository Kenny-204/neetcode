class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


def make_linked_list(lst):
    head = None
    for val in reversed(lst):
        head = ListNode(val, head)
    return head


# Your lists
l1_vals = [9, 9, 9, 9, 9, 9, 9]
l2_vals = [9, 9, 9, 9]

l1 = make_linked_list(l1_vals)
l2 = make_linked_list(l2_vals)

# node6 = ListNode(6)
# node5 = ListNode(5, node6)
# node4 = ListNode(4, node5)
# node3 = ListNode(3)
# node2 = ListNode(2, node3)
# node1 = ListNode(6, node2)


# l1 = node1
# l2 = node4


def addTwoNumbers(l1, l2):
    remainder = 0
    res = ListNode(0)
    curr1 = l1
    curr2 = l2
    curr3 = res
    while curr1 and curr2:
        sum = curr1.val + curr2.val + remainder
        if remainder > 0:
            remainder = 0
        if sum >= 10:
            digits = str(sum)
            digit1, digit2 = int(digits[0]), int(digits[1])
            print(digit1, digit2)
            curr3.next = ListNode(digit2)
            remainder = digit1
        else:
            curr3.next = ListNode(sum)
        curr1 = curr1.next
        curr2 = curr2.next
        curr3 = curr3.next
    print(curr1)
    while curr1:
        sum = curr1.val +  remainder
        if remainder > 0:
            remainder = 0
        if sum >= 10:
            digits = str(sum)
            digit1, digit2 = int(digits[0]), int(digits[1])
            curr3.next = ListNode(digit2)
            remainder = digit1
        else:
            curr3.next = ListNode(sum)
        curr3 = curr3.next
        curr1 = curr1.next
    while curr2:
        sum =  curr2.val + remainder
        if remainder > 0:
            remainder = 0
        if sum >= 10:
            digits = str(sum)
            digit1, digit2 = int(digits[0]), int(digits[1])
            curr3.next = ListNode(digit2)
            remainder = digit1
        else:
            curr3.next = ListNode(sum)
        curr3 = curr3.next
        curr2 = curr2.next
    if remainder > 0:
        curr3.next = ListNode(remainder)

    return res.next


print_list(addTwoNumbers(l1, l2))
