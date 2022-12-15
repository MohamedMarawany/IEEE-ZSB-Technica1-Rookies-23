class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            minHeap += [[x**2 + y**2, x, y]]

        heapq.heapify(minHeap)

        res = []
        for i in range(k):
            d, x, y = heapq.heappop(minHeap)
            res.append([x, y])

        return res
