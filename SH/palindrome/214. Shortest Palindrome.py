# You are given a string s. You can convert s to a 
# palindrome
#  by adding characters in front of it.

# Return the shortest palindrome you can find by performing this transformation.

# Example 1:

# Input: s = "aacecaaa"
# Output: "aaacecaaa"
# Example 2:

# Input: s = "abcd"
# Output: "dcbabcd"
# Should use KMP Algorithm: https://blog.naver.com/kks227/220917078260


def shortestPalindrome(self, s: str) -> str:
    dp = [([0]*len(s)) for _ in range(len(s))]

    for left in range(len(s)-1, -1, -1):
        dp[left][left] = 1
        for right in range(left+1, len(s)):
            if s[left] == s[right]:
                dp[left][right] = 2+dp[left+1][right-1]
            else:
                dp[left][right] = max(dp[left+1][right], dp[left][right-1])

    return dp[0][len(s)-1]


# Reference
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def build_failure_table(s):
            l = 0
            table = [0] * len(s)

            for r in range(1, len(s)):
                if s[l] == s[r]:
                    l += 1
                    table[r] = table[r - 1] + 1
                else:
                    # we don't wanna start the pattern over again, so we try to see
                    # if the current character is the same as the pattern's end
                    l = table[r - 1]

                    while l > 0:
                        if s[l] == s[r]:
                            table[r] = l + 1
                            l += 1
                            break
                        else:
                            l = table[l - 1]
                    else:
                        if s[l] == s[r]:
                            table[r] = 1
                            l += 1
            
            return table

        if s == "": return ""
        table = build_failure_table(s + "#" + s[::-1])
        longest_palindromic_substring_len = table[-1]

        return s[longest_palindromic_substring_len:][::-1] + s
                    
