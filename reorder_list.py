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


node6 = ListNode(6)
node5 = ListNode(5, node6)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
node0 = ListNode(0, node1)

list1 = node0
# [1,2,3,4,5]


def splitList(head):
    slow, fast = head, head
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    slow = slow.next
    prev = prev.next
    prev.next = None

    return head, slow


def reverseList(head):
    prev = None
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev


def mergeLists(first, second):
    head = first
    while first and second:
        temp1 = head.next
        temp2 = second.next

        head.next = second
        second.next = temp1
        head = temp1
        second = temp2

    print_list(first)


def reorderList(head):
    if not head.next or not head:
        return

    # first divide the list into two halves first half and second half
    first_half_of_list, second_half_of_list = splitList(head)
    # reverse the second half
    reversed_second_half = reverseList(second_half_of_list)
    # merge the two lists into one
    mergeLists(first_half_of_list, reversed_second_half)


print(reorderList(list1))
