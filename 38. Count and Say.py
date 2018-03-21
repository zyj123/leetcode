class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for _ in range(n-1):
            res = [0, s[:1]]
            for i in s:
                res_l = len(res)
                if i == res[res_l - 1]:
                    res[res_l - 2] += 1
                else:
                    res.append(1)
                    res.append(i)
            s = ''.join(map(str, res))
        return s

obj = Solution()
res = obj.countAndSay(6)
print(res)