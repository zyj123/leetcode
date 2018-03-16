class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        po = [0, 0]
        for i in moves:
            if i == 'R':
                po[0] += 1
            if i == 'L':
                po[0] -= 1
            if i == 'U':
                po[1] += 1
            if i == 'D':
                po[1] -= 1
        if po == [0, 0]:
            return True
        return False

# obj = Solution()
# res = obj.judgeCircle('UD')
#
# print(res)

