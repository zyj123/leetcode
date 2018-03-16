class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0
        cmap = {}
        for i, p1 in enumerate(points):
            for p2 in points:
                distance = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
                if distance != 0:
                    cmap[distance] =cmap.get(distance,0) + 1
            for key in cmap:
                if cmap[key] >=2:
                    res += cmap[key] * (cmap[key] -1)
            cmap = {}
        return res

obj = Solution()
res = obj.numberOfBoomerangs([[0,0],[1,0],[2,0]])
print(res)