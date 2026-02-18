class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dici = {}
        ans = 0
        for i in stones:
            if i in dici:
                dici[i] += 1
            else:
                dici[i] = 1
        for J in jewels:
            if J in dici:
                ans += dici[J]
        return ans
        