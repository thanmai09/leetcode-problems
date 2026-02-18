class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        dici= {}
        for i in nums:
            if i in dici:
                dici[i] += 1
            else:
                dici[i] = 1
        for j in dici:
            n = dici[j]
            ans += (n*(n-1))//2
        return ans
        