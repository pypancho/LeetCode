class Solution:
    def twoSum(self, nums, target):
        temps = {}
        finals = {}
        for index, item in enumerate(nums):
            sub = target - item
            if sub not in temps:
                temps[item] = index
                #print(temps)
            else:
                return(temps[sub], index)