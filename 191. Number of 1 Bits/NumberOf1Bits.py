class Solution:
    def hammingWeight(self, n: int) -> int:
        string1 =str(bin(n))
        count1=0
        for i in string1:
            if i=='1':
                count1+=1
        return count1
        