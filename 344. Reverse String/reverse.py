class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        if len(s)==0:
            return s
        pop=''
        
        for char in range (len(s)):
            pop += s.pop()
            
        for character in pop:
            s.append(character)