class Solution(object):

    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        leftIndex = 0 
        rightIndex = len(arr) - 1
        while (leftIndex < rightIndex):
            mid = (leftIndex + rightIndex) // 2
            if arr[mid] < x:
                leftIndex = mid + 1
            else:
                rightIndex = mid
        
        rightIndex = leftIndex
        leftIndex -= 1
    
        while k > 0:
            if (leftIndex >= 0 and abs(arr[leftIndex] - x) <= abs(arr[rightIndex] - x)) or (rightIndex >= len(arr)):
                leftIndex -= 1
            else:
                rightIndex += 1
            k -= 1
        
        return arr[leftIndex+1:rightIndex]







