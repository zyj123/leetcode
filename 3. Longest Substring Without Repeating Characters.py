class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub = []
        length = tmp_length = 0
        for i in s:
            if i in sub:
                tmp_length = len(sub)
                sub = sub[sub.index(i) + 1:]
                sub.append(i)
                length = max(length, tmp_length)
            else:
                sub.append(i)
        length = max(length, len(sub))
        return length



obj = Solution()
res = obj.lengthOfLongestSubstring('abababc')
print(res)

sub = []
if 3 in sub:
    print(2)