class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_new = []
        x_new = str(x)
        for i in x_new:
            list_new.append(i)
        list_reverse = list_new [::-1]
        if (list_reverse == list_new):
            return True