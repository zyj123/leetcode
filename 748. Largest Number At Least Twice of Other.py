class Solution(object):


    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        if all([2*i <= m for i in nums if i != m]):
            return nums.index(m)
        return -1


obj = Solution()
res = obj.dominantIndex([0,0,0,1])
print(res)
