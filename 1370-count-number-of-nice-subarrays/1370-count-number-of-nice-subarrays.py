class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMostk(arr,k):
            l = 0
            ans = 0 
            temp = 0
            n = len(arr)
            for r in range(n):
                if arr[r]%2 == 1:
                    temp += 1
                while temp > k:
                    if arr[l]%2 == 1:
                        temp -= 1
                    l+= 1
                ans += r-l+1
            return ans
        a = atMostk(nums,k)
        b = atMostk(nums,k-1)
        ans = a-b
        return ans
                    