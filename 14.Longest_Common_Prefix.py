class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return '' 
        res = ''
        strs = sorted(strs)#按照字符串里的先后顺序排序
        for i in strs[0]:
            if strs[-1].startswith(res+i): #这样就只检查第一个和最后一个字符串
                res += i
            else:
                break
        return res
