class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        returnList = []
        for i in range(0,len(arr)):
            for j in range(i+1, len(arr)):
                returnList.append((arr[i]*1.0/arr[j],arr[i],arr[j]))
        
        returnList = sorted(returnList, key= lambda elements: elements[0])
        for index, element in enumerate(returnList):
            if index==k-1:
                return [element[1],element[2]]