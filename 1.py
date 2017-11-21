class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return
        buff_dict = {}      #{3:0, 4:1,  }
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i
                
                #[3, 2, 4] 6
                