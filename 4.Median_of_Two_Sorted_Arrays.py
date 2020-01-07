class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        
        lenth = len(nums)
        if lenth % 2 == 1:
            median = nums[(lenth - 1)// 2]
        else:
            median = (nums[lenth // 2] + nums[(lenth - 1) // 2] ) / 2
        
        return median
