class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s=Counter(s)
        t=Counter(t)
        for i,v in t.items():
            if(s[i]==v):
                continue
            return i
        # result = ''
        # if (s==""):
        #     result =t
        # for i in s:
        #     for j in range (len(t)):
        #         if (i !=t[j]):
        #             result = t[j]
        #         elif (j+1<len(t) and t[j]==t[j+1]):
        #             result = t[j+1]
        # return result
        
        