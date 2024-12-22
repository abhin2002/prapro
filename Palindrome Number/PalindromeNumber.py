class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        Flag = True
        n = 1

        num = x
        temp = x
        reverse = 0

        while x//10 > 0:
            n = n+1
            x = x // 10

        for i in reversed(range(n)):
            reverse = reverse + ((temp % 10) * 10 ** i)
            temp = temp // 10 
        
        print(n)
        print(reverse)

        if num == reverse:
            return True
        else:
            return False
        
S = Solution()

print(S.isPalindrome(-121))


