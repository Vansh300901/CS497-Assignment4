class Solution(object):
    def shortestSubarray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        numsSize = len(nums)
    
        sumCounter = [0] * (numsSize + 1)
        for i in range(numsSize):
            sumCounter[i + 1] = sumCounter[i] + nums[i]

        returnLength = -1
        tempDeque = deque()

        for i in range(numsSize + 1):
            while tempDeque and sumCounter[i] - sumCounter[tempDeque[0]] >= k:
                if returnLength == -1:
                    returnLength =  i - tempDeque.popleft()
                else:
                    returnLength = min(returnLength, i - tempDeque.popleft())

            while tempDeque and sumCounter[i] <= sumCounter[tempDeque[-1]]:
                tempDeque.pop()

            tempDeque.append(i)

        return returnLength
                        

