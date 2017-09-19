# ideas:
# - compute the sums each time is too slow
# - better store the cumulative sums
# - append() function in python


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.csums = [0]
        for x in nums:
            self.csums.append(self.csums[-1] + x)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.csums[j+1] - self.csums[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)