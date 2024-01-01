class Solution:
    def isPalindrome(self, x):
        reversed_num = str(x)[::-1]
        if(str(x) == reversed_num):
            return True
        else:
            return False

##FINISHED##
