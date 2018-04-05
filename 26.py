class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while True:
            try:
                if nums[i] == nums[i + 1]:
                    nums.remove(nums[i])
                else:
                    i += 1
            except IndexError:
                break
