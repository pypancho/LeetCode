s = 'MCMXCIV'

class Solution:
    def romanToInt(self, s: str) -> int:
        
        syb = {
            "M":1000, "CM":900, "D":500, "CD":400,
            "C":100, "XC":90, "L":50, "XL":40,
            "X":10, "IX":9, "V":5, "IV":4,
            "I":1
            }
        num = 0

        i = 0
        while(i<len(s)):
            if s[i:i+2] in syb:
                print(s[i:i+2])
                num = num + syb[s[i:i+2]]
                i = i + 2
        
            else:
                num = num + syb[s[i]]
                i = i + 1
        

        return(num)
