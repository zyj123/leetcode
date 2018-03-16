class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_len = len(nums)
        for i in range(0, nums_len - 1):
            for j in range(i + 1, nums_len):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            if target - i in nums[1:]:
                return [nums.index(i), len(nums) - 1 - nums[::-1].index(target - i)]
        return False

obj = Solution()
res = obj.twoSum([3,2,4], 6)
# print(res)

num = [1,2,3]
i = num[0:-1]
print(i)