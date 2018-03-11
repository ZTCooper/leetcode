'''
extend()方法合并两列表
sort()方法排序
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        
        if len(nums1) % 2 == 0:
            median = (nums1[len(nums1)//2] + nums1[len(nums1)//2-1])/2
        else:
            median = nums1[len(nums1)//2]
        
        return float(median)
        