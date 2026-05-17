import heapq
import math

points = [[0,2],[2,2]]
k = 1


def kClosest(points,k):
        minHeap = []
        res  = []
#  (sqrt((x1 - x2)^2 + (y1 - y2)^2)).
        for i, point in enumerate(points):
            distance = math.sqrt(((point[0] - 0) ** 2) + ((point[1] - 0) ** 2))
            heapq.heappush(minHeap,[distance, i])
        
        for i in range(k):
            closest = heapq.heappop(minHeap)
            res.append(points[closest[1]])
        return res
    
print(kClosest(points,k))