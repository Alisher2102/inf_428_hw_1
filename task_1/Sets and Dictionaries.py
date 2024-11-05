class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Convert lists to sets to find common elements
        answer = set(nums1) & set(nums2)
        # Convert the set back to a list
        result = list(answer)
        return result
        