import heapq

def getTopKElements(heap, k):
    returnList = []
    
    pQueue = [(-heap[0], 0)]

    while k > 0 and pQueue:
        value, index = heapq.heappop(pQueue)
        returnList.append(-value)
        k -= 1

        left = 2 * index + 1
        if left < len(heap):
            heapq.heappush(pQueue, (-heap[left], left))

        right = 2 * index + 2
        if right < len(heap):
            heapq.heappush(pQueue, (-heap[right], right))

    return returnList

# Test
print(getTopKElements([15, 13, 12, 10, 8, 9], 5))  # Output: [15, 13, 12, 10, 9]
