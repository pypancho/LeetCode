class Solution:
    def maxArea(self, height) -> int:
        left=0
        right=len(height)-1
        area=0
        while left<right:#条件使用夹逼准则
            #水容量取新计算的和之前的最大值
            area=max(area,(right-left)*min(height[left],height[right]))
            #左右同时向中间推进，每次只要计算长的那根就行
            if  height[left]<height[right]:
                left+=1
            else:
                right-=1
        return area
