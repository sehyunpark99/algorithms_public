'''
132. Palindrome Partitioning II
Hard
Topics
Companies
Given a string s, partition s such that every 
substring of the partition is a 
palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
'''
inf = 1e10
# Use of palindrome partition I, passed 24/32
class Solution:
    def minCut(self, s: str) -> int:
        def partition(s):
            n = len(s)
            ans = []
            # Base case
            if n == 0:
                return [[]]
            # From single characters to full word
            for i in range(1, n+1): 
                if s[:i] == s[i-1::-1]: # if prefix is the palindrome
                    next = partition(s[i:]) # go over suffix
                    for suf in next:
                        ans.append([s[:i]]+suf)
            return ans
        lists = partition(s)
        min_length = inf
        for sub in lists:
            min_length = min(min_length, len(sub))
        return min_length-1
            
# DP
class Solution:    
    def minCut(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)] # initialization [to inf cuz we want min. cuts]

        # Step 1: Preprocess the string to determine which substrings are palindromes
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                if s[i] == s[i+length-1] and dp[i+1][i+length-1] == 1:
                    dp[i][i+length-1] = 1
        # print(dp)
        # Step 2: Use dynamic programming to determine the minimum cuts needed
        cuts = list(range(n)) #[0, 1, 2, 3, 4, ...]
        # print(f'initialization: {cuts}')
        for i in range(1, n):
            if dp[0][i]:
                cuts[i] = 0 # if palindrome, cut to be 0
            else:
                for j in range(i): # going through column
                    if dp[j+1][i]:
                        cuts[i] = min(cuts[i], cuts[j]+1)
                        # print(cuts, i, j)
        # print(cuts)
        return cuts[-1]

# class Solution:
#     def minCut(self, s: str) -> int:
#         n = len(s)
        
#         # Step 1: Preprocess the string to determine which substrings are palindromes
#         dp = [[False]*n for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = True
#         for i in range(n-1):
#             if s[i] == s[i+1]:
#                 dp[i][i+1] = True
#         for l in range(3, n+1):
#             for i in range(n-l+1):
#                 j = i+l-1
#                 if s[i] == s[j] and dp[i+1][j-1]:
#                     dp[i][j] = True
        
#         # Step 2: Use dynamic programming to determine the minimum cuts needed
#         cuts = list(range(n))
#         for i in range(1, n):
#             if dp[0][i]:
#                 cuts[i] = 0
#             else:
#                 for j in range(i):
#                     if dp[j+1][i]:
#                         cuts[i] = min(cuts[i], cuts[j]+1)
        
#         # Step 3: Return the final answer
#         return cuts[-1]


if __name__ == "__main__":
    print("132. Palidrome_Partitioning_II.py")

    solution = Solution()
    print("\nCase 1")
    chars = "aab"
    res = solution.minCut(chars)  
    ans = 1
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 2")
    chars = "a"
    res = solution.minCut(chars)  
    ans = 0
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 3")
    chars = "aa"
    res = solution.minCut(chars)  
    ans = 0
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 4")
    chars = "leet"
    res = solution.minCut(chars)  
    ans = 2
    print(res, "\n  ==> check: ", res==ans)

