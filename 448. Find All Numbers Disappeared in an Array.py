class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # For each number i in nums,
        # we mark the number that i points as negative.
        # Then we filter the list, get all the indexes
        # who points to a positive number
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])
        print(nums)

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

obj = Solution()
res = obj.findDisappearedNumbers([1,2,3,4,3,2,5,6,7])

print(res)
