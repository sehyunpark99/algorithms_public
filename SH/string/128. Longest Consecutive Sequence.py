class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp=defaultdict(list)
        bl=defaultdict(bool)
        mx=0
        for i in nums:
            if bl[i]:
                continue 
            bl[i]=True
            l,r=i,i
            if mp[i+1]:
                r=mp[i+1][0]
            if mp[i-1]:
                l=mp[i-1][1]
            mp[r]=[r,l]
            mp[l]=[r,l]
            mx=max(mx,r-l+1)
        return mx
    
# Version 2 - C
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0:
            return 0

        nums.sort()

        cnt = 1
        maxi = 0

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    cnt += 1
                else:
                    maxi = max(maxi, cnt)
                    cnt = 1

        return max(maxi, cnt)