class Solution:
  def threeSumClosest(self, nums, target):
    nums.sort()
    n = len(nums)
    d = 2**32
    ans = 0
    for i in range(n - 2):
      s, t = i + 1, n - 1
      while s < t:
        sum3 = nums[i] + nums[s] + nums[t]
        if sum3 == target: return target
        diff = abs(sum3 - target)
        if diff < d: ans, d = sum3, diff        
        if sum3 > target: 
          t -= 1 
        else: 
          s += 1
    return ans
