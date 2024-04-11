'''
516. Longest Palindromic Subsequence
Solved
Medium
Topics
Companies
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
'''

def longestPalindromeSubseq(self, s: str) -> int:
    
    dp = [([0] * len(s)) for _ in range(len(s))]

    for left in range(len(s) - 1, -1, -1): 

        dp[left][left] = 1

        for right in range(left + 1, len(s)):

            if s[left] == s[right]:
                dp[left][right] = 2 + dp[left + 1][right - 1]
            else:
                dp[left][right] = max(dp[left + 1][right], dp[left][right - 1])

    return dp[0][len(s) - 1]