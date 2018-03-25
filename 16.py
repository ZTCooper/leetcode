class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return
        if len(nums) == 3 and sum(nums) == 0:
            return 0
        nums.sort()
        i = 0
        mini_gap = float("inf")     # infinity
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                summary = nums[i] + nums[j] + nums[k]
                if summary < target:
                    j += 1
                elif summary > target:
                    k -= 1
                elif summary == target:
                    return summary
                if abs(summary - target) < mini_gap:
                    mini_gap = abs(summary - target)
                    result = summary
            i += 1
        return result


s = Solution()
print(s.threeSumClosest([-1, 2, 1, -4], 1))
