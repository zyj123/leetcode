class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l = []
        next_level = 0
        for i in range(len(l1)):
            if next_level == 1:
                if l1[i] + l2[i] > 9:
                    l.append(l1[i] + l2[i] + 1 - 10)
                    next_level = 1
                else:
                    l.append(l1[i] + l2[i] + 1)
                    next_level = 0
            else:
                if l1[i] + l2[i] > 9:
                    l.append(l1[i] + l2[i] - 10)
                    next_level = 1
                else:
                    l.append(l1[i] + l2[i])
                    next_level = 0
        if next_level == 1:
            l.append(1)
        l.reverse()
        return l

obj = Solution()
res = obj.addTwoNumbers([2,4,3],[5,6,3])
print(res)