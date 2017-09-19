# ideas:
# - Three steps
# - 1. find the range: 0-9, 10-99 or 100-999, etc
# - 2. find the number and position of the digit
# - 3. extract the digit from the number
# - Note: the commented solution is actually faster, without involving type transformation

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 9:
            return n
        else:
            k = 1 # number of digits in current number
            while n > 9*k*(10**(k-1)):
                n = n - 9*k*(10**(k-1))
                k = k + 1
            # i = n % k # position of the digit in current number
            # print (i)
            # if i > 0:
            #     x = 10**(k-1) + (n // k) # current number
            #     x = x // (10**(k-i)) # get rid of the last k-i digits
            #     x = x % 10 # get rid of the first i-1 digits
            #     return x
            # else:
            #     x = 10**(k-1) + (n // k) - 1 # current number
            #     x = x % (10**(i+1)) # get rid of the first i-1 digits
            #     return x
            i = (n-1) % k  # position
            x = (n-1)//k + 10**(k-1)  # number
            s = str(x)
            return int(s[i])