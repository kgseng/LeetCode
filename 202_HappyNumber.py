# Write an algorithm to determine if a number n is happy.
# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

class Solution(object):
    def square(self, num):
        square_num = 0
        while num > 0:
            square_num += (num%10)**2
            num = num//10
        return square_num
    
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        fast, slow = n, n
        while True:
            fast = self.square(self.square(fast))
            slow = self.square(slow)
            if slow == fast: break
        return slow == 1

    