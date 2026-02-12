class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node5 = ListNode(5)
node4 = ListNode(4)
node3 = ListNode(3, node5)
node2 = ListNode(2, node4)
node21 = ListNode(1, node3)
node1 = ListNode(1, node2)

list1 = node1
list2 = node21


# [1,2,4]
# [1,3,5]
def mergeTwoLists(list1, list2):
    dummy = ListNode(0)
    nodel = dummy
    nodel1 = list1
    nodel2 = list2
    while nodel1 and nodel2:
        if nodel1.val < nodel2.val:

            nodel.next = nodel1
            nodel = nodel.next
            nodel1 = nodel1.next

        else:
            nodel.next = nodel2
            nodel = nodel.next
            nodel2 = nodel2.next

    if node1:
        nodel.next = nodel1
    else:
        nodel.next = node2

    return dummy.next.next.next.val


print(mergeTwoLists(list1, list2))
