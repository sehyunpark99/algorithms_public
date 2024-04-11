'''
647. Palindromic Substrings
Medium
Topics
Companies
Hint
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''

# Expand from center
class Solution:
    def countSubstrings(self, s: str) -> int:
        n, ans = len(s), 0
        def expand_from_center(left, right):
            count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return count
        
        for i in range(n):
            even = expand_from_center(i, i+1)
            odd = expand_from_center(i, i)
            
            ans += odd+even
        return ans

# DP Table
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        palindrome = [[False] * n for _ in range(n)]
        ans = 0

        for i in range(n):
            palindrome[i][i] = True
            ans += 1

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                palindrome[i][i + 1] = True
                ans += 1

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                if s[i] == s[i + length - 1] and palindrome[i + 1][i + length - 2]:
                    palindrome[i][i + length - 1] = True
                    ans += 1
        print(palindrome)
        return ans

# DP Table Solution
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         n = len(s)
#         ans = 0

#         if n <= 0:
#             return 0

#         dp = [[False] * n for _ in range(n)]

#         for i in range(n):
#             dp[i][i] = True
#             ans += 1

#         for i in range(n - 1):
#             dp[i][i + 1] = (s[i] == s[i + 1])
#             ans += 1 if dp[i][i + 1] else 0

#         for length in range(3, n + 1):
#             for i in range(n - length + 1):
#                 j = i + length - 1
#                 dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
#                 ans += 1 if dp[i][j] else 0

#         return ans


if __name__ == "__main__":
    print("647. Palindromic_Substring.py")

    solution = Solution()
    print("\nCase 1")
    chars = "abc"
    res = solution.countSubstrings(chars)  
    ans = 3
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 2")
    chars = "aaa"
    res = solution.countSubstrings(chars)  
    ans = 6
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 3")
    chars = "aa"
    res = solution.countSubstrings(chars)  
    ans = 3
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 4")
    chars = "aaaaa"
    res = solution.countSubstrings(chars)  
    ans = 15
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 5")
    chars = "babaa"
    res = solution.countSubstrings(chars)  
    ans = 8
    print(res, "\n  ==> check: ", res==ans)

'''
# could get all the cases
class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palindrome(s:str):
            n = len(s)
            if(n%2):
                return s[:n//2] == s[n:n//2:-1]
            else:
                return s[:n//2] == s[n:n//2-1:-1]
            
        def expand_from_center(left, right):
            count = 0
            if left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            return s[left+1:right]
        
        # Base case
        if len(s) <= 1:
            return 1
        
        count = 0
        if is_palindrome(s):
            count += 1

        for i in range(len(s)):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i+1)

            if odd and is_palindrome(odd) and odd != s:
                count += 1
                print(f'odd: {odd}, count: {count}')
            if even and is_palindrome(even) and even != s:
                count += 1
                print(f'even: {even}, count: {count}')
        return count
'''