class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

list1 = node1


def hasCycle(head):
    slow = head
    fast = head

    while slow and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    return False


# def hasCycle(head):

#     seen = {}

#     if not head:
#         return False

#     node = head

#     while node:
#         if node in seen:
#             return True
#         else:
#             seen[node] = True
#             node = node.next
#     return False

print(hasCycle(node1))
