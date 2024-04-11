class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        #1 always comes first, and we fill in all the ones that exist,
        #if it gets greater than n, then we finish
        ans = []
        
        def recursive(value):
            if len(ans) >= n:
                return
            ans.append(value)
            if (value * 10) <= n:
                recursive(value * 10)
            if value + 1 <= n and int(str(value)[-1]) < 9:
                recursive(value + 1)
        recursive(1)

        return ans
    
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        cur = 1
        for i in range(n):
            # Add the current number to the result
            res.append(cur)
            # If the current number times 10 is less than or equal to n, move to the next level
            if cur * 10 <= n:
                cur *= 10
            # Otherwise, move to the next number at the current level
            else:
                # If we've reached the end of a level, divide by 10 to go back up one level
                if cur >= n:
                    cur //= 10
                cur += 1
                # Skip over any trailing zeroes (e.g. if cur = 19, skip over 190, 191, 192, etc.)
                while cur % 10 == 0:
                    cur //= 10
        return res