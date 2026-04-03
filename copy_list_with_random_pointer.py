class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


# Step 1: create all nodes with just values
node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

# Step 2: set the next pointers
node0.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

# Step 3: set the random pointers
node0.random = node6
node1.random = node0
node2.random = node2
node3.random = node1
node4.random = node5
node5.random = node4
node6.random = node2
node7.random = None


def print_list(head):
    current = head
    while current is not None:
        if current.random is not None:
            print(current.val,"=>",current.random.val)
        else :print(current.val, end=" -> ")
        current = current.next
    print("None")


def copyRandomList(head):
    if not head:
        return None
        
        
    hashmap = {}
    new_head = Node(head.val)
    curr = new_head
    curr_head = head

    while curr:
        hashmap[curr_head] = curr
        if curr_head.next:
            curr.next = Node(curr_head.next.val) or None
        else:
            curr.next = None
        # curr.random = None
        curr = curr.next
        curr_head = curr_head.next

    curr = new_head
    curr_head = head
    # print(hashmap)
    while curr:
        if curr_head.random is not None:
            curr.random = hashmap[curr_head.random]
        else:
            curr.random = None
        curr = curr.next
        curr_head = curr_head.next
    print_list(new_head)
    return new_head


(copyRandomList(node0))
