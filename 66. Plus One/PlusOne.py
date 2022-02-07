class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list1 = []
        string=''
        num = 0
        for i in digits:
            string+=str(i)
            num = int (string)+1
        num1 =str(num)
        for j in num1:
            list1.append(int(j))
        return list1