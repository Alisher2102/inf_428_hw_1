class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        counter = 1

        for index, number in enumerate(nums):
            if index + 1 < len(nums) and number < nums[index + 1]:
                counter += 1
            else:
                answer = max(answer, counter)
                counter = 1

        return max(answer, counter)  # Handle the case where the longest sequence is at the end
        
        