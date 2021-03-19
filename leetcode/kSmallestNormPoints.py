import heapq


def kClosest(points, k):
    dist = [(-x*x - y*y, [x, y]) for x, y in points]
    heap = dist[:k]
    heapq.heapify(heap)
    for d in dist[k:]:
        if d[0] > heap[0][0]:
            heapq.heappop(heap)
            heapq.heappush(heap, d)
    return [h[1] for h in heap]


if __name__ == '__main__':
    print(kClosest([[1, 3], [-2, 2]], 2))
    print(kClosest([[3, 3], [5, -1], [-2, 4]], 2))