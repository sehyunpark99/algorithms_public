class Solution:
    def deleteString(self, S):
        N = len(S)
        if S.count(S[0]) == N: return N
        P = [0] * (N + 1)
        dp = [1] * N
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                P[j] = P[j + 1] + 1 if S[i] == S[j] else 0
                if P[j] >= j - i:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[0]
    
'''
2430. Maximum Deletions on a String
Hard
Topics
Companies
Hint
You are given a string s consisting of only lowercase English letters. In one operation, you can:

Delete the entire string s, or
Delete the first i letters of s if the first i letters of s are equal to the following i letters in s, for any i in the range 1 <= i <= s.length / 2.
For example, if s = "ababc", then in one operation, you could delete the first two letters of s to get "abc", since the first two letters of s and the following two letters of s are both equal to "ab".

Return the maximum number of operations needed to delete all of s.

 

Example 1:

Input: s = "abcabcdabc"
Output: 2
Explanation:
- Delete the first 3 letters ("abc") since the next 3 letters are equal. Now, s = "abcdabc".
- Delete all the letters.
We used 2 operations so return 2. It can be proven that 2 is the maximum number of operations needed.
Note that in the second operation we cannot delete "abc" again because the next occurrence of "abc" does not happen in the next 3 letters.
'''