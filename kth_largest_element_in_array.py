import heapq

nums = [2, 3, 1, 5, 4]
k = 2


def findKthLargest(nums, k):
    maxheap = [-num for num in nums]
    heapq.heapify(maxheap)
    
    for i in range(k-1):
        heapq.heappop(maxheap)
    return -heapq.heappop(maxheap)


print(findKthLargest(nums,k))
