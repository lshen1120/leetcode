class Solution(object):
    def searchRange(self, nums, target):
        start = -1
        end = -1
        index = 0
        while index < len(nums):
            if nums[index] == target:
                start = index
                end = index
                index += 1
                while index < len(nums):
                    if nums[index] == target:
                        end = index
                    index += 1
            else:
                index += 1
        return [start, end]
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """


print  Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
