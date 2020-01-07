class Solution:
    def isMatch(self, t: str, p: str) -> bool:
        # 创建 (len(text)+1)*(len(pattern)+1)的二维布尔list，且初始化为False；T：Table
        T = [[False] * (len(p) + 1) for _ in range(len(t) + 1)]
        # T(Table)的row指代t的每一个字符，col指代p的每一个字符；
        #表中存储的是bool值，若之前字符全部相等，则为True，否则为False
        T[0][0] = True #若t和p为空，则必为True
        
        #先处理pattern若每隔一个字符就一个*的，诸如a*， a*b*， a*b*c*这类的
        for i in range(1,len(T[0])):
            if (p[i-1] == '*'):
                T[0][i] = T[0][i-2]
        
        for i in range(1,len(T)):
            for j in range(1,len(T[0])):
                if p[j-1] in {t[i-1], '.'}:
                    T[i][j] = T[i-1][j-1]
                elif p[j-1] == '*':
                    T[i][j]=T[i][j-2]
                    if p[j-2] in {t[i-1], '.'}:
                        T[i][j] = T[i][j] or T[i-1][j]
                else:
                    T[i][j] = False
        return T[-1][-1]
