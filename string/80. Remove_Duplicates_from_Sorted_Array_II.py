def removeDuplicates(nums: List[int])->int:
    memo = {}
    idx = len(nums)
    count = 0
    for i in range(idx):
        if nums[i] not in memo: # Dictionary key should be the number
            nums[count] = nums[i]
            memo[nums[i]] = 1
            count += 1
        elif memo[nums[i]] == 1:
            nums[count] = nums[i]
            memo[nums[i]] = 2
            count += 1
    return count


# Version 2 - direct translation of C 
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize an integer k that updates the kth index of the array...
        # only when the current element does not match either of the two previous indexes. ...
        k = 0
        # Traverse all elements through loop...
        for i in nums:
            # If the index does not match elements, count that element and update it...
            if k < 2 or i != nums[k - 2]:
                nums[k] = i
                k += 1
        return k       # Return k after placing the final result in the first k slots of nums...