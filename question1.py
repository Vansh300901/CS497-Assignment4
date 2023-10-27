class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        return_list = []
        temp_dict = {}
        max = 0

        for num in nums:
            if num in temp_dict.keys():
                temp_dict[num] += 1
            else:
                temp_dict[num] = 1
        
        for i in range(k):
            for key in temp_dict.keys():
                if temp_dict[key] > max:
                    tempKey = key
                    max = temp_dict[key]

            return_list.append(tempKey)
            del temp_dict[tempKey]
            max = 0

        return return_list



        