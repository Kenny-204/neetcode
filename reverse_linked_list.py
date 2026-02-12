head = [0, 1, 2, 3]


def reverseList(head):
    if head == []:
        return []
    node = head
    prev = null

    while node != null:
        temp = node.next
        node.next = prev
        prev = node
        node = temp

    return prev


print(reverseList(head))
