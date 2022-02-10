class Solution:
    def isPalindrome(self, s: str) -> bool:
        string1=''
        for i in s:
            if (i.isalnum()):
                string1+=i
            elif(len(s)==0):
                return True
        
        string1=string1.lower()
        
        string2=string1[::-1]
        if (string1==string2):
            return True
        return False