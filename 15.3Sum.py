nums = [-1,0,1,2,-1,-4]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums or len(nums)<3: #检查是否为空或者少于3个数
            return(res)

        nums.sort()#先排序，省事
        for i in range(len(nums)):

            if nums[i]>0: #从第i个开始计算，nums[i]都大于0，没必要继续了
                break
            elif i>0 and nums[i] == nums[i-1]: #跳过连续重复项，从第二个开始检查起
                continue
            else:
                left = i + 1 #left从nums[i]走起
                right = len(nums) - 1 #right从最后一个走起
                while(left<right): #left和right碰到一起，停止
                    temp = nums[i] + nums[left]+ nums[right] #一定要这个，不要重复算在下面的步骤中
                    if  temp == 0:
                        res.append([nums[i], nums[left], nums[right]])
                        while (left<right and nums[left]==nums[left+1]): #跳过重复项
                            left = left + 1
                        while (left<right and nums[right]==nums[right-1]):#跳过重复项
                            right = right - 1
                        left = left + 1
                        right = right - 1
                    elif    temp<0:
                        left = left + 1
                    elif    temp>0:
                        right = right - 1

        return (res)
