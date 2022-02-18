class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.split()
        for i in range (len(s1)):
            if i==len(s1)-1:
                return (len(s1[i]))
            
        
            