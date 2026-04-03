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

n = 2



def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    slow = fast = dummy
    prev = None
    for _ in range(n):
        fast = fast.next

    while fast:
        prev = slow
        slow = slow.next
        fast = fast.next
    prev.next = slow.next
    slow.next = None
    
    return dummy.next

# My initial solution that worked

# def deleteNode(head, node):

#     curr = head
#     prev = curr

#     if head == node:
#         head = head.next
#         node.next = None

#     while curr:
#         if curr != node:
#             prev = curr
#             curr = curr.next
#         else:
#             prev.next = curr.next
#             curr.next = None
#             break
#     return head


# def removeNthFromEnd(head, n):
#     hashmap = {}
#     i = 1

#     curr = head
#     while curr:
#         hashmap[i] = curr
#         curr = curr.next
#         i += 1
#     node_to_delete = i - n
#     # print(hashmap, i, node_to_delete)

#     head = deleteNode(head, hashmap[node_to_delete])


print(removeNthFromEnd(list1, n))
