# ideas:
# - take out all the prime factors from num using while loop
# - if what is left is 1, then true, otherwise false


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num>=2 and num%2==0:
            num = num/2
        while num>=3 and num%3==0:
            num = num/3
        while num>=5 and num%5==0:
            num = num/5
        return num==1