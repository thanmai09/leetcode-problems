from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        val = colors[0]
        n = len(colors)
        for i in range(1,n):
            if colors[i] != val:
                ans = max(ans,i)
        for i in range(n-1):
            if colors[i] != colors[n-1]:
                ans = max(ans,n-1-i)
        return ans
        