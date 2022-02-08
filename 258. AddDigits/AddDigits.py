class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0 : 
            return 0
        if num % 9 == 0 : 
            return 9
        else : 
            return (num % 9)
        
        # num1 = str (num)
        # list1 = []
        # sum1=0
        # list2 = []
        # sum2 = 0
        # for i in num1:
        #     list1.append(int (i))
        # for j in list1: 
        #     sum1 +=j
        # if sum1 >=9:
        #     num1 = str (sum1)
        #     for k in num1:
        #         list2.append(int (k))
        #     for a in list2:
        #         sum2 += a
        #     return sum2
        # return sum1