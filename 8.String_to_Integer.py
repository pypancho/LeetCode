class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str1 = str.strip()
        # 字符串为空，直接返回0，不进行下面的判断
        if len(str1) < 1:
            return 0

        sign = 1 # sign用来区分正负号
        if str1[0] == '-':
            str1 = str1[1:]
            sign = -1
        elif str1[0] == '+':
            str1 = str1[1:]
            sign = 1

        sum = 0
        for c in str1:
            if '0' <= c <= '9':
                sum = sum * 10 + ord(c) - ord('0')
            else:
                sum = sum * sign
                if sum  < -2 ** 31:
                    return -2 ** 31
                elif sum >= 2 ** 31 - 1:
                    return 2 ** 31 - 1
                return sum

        sum = sum * sign
        if sum <= -2 ** 31:
            return -2 ** 31
        elif sum >= 2 ** 31 -1:
            return 2 ** 31 -1
        return sum
