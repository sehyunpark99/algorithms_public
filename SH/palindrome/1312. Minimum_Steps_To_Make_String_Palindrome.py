def minInsertions(s: str) -> int:
    dp = [[0 for _ in range(len(s))]for _ in range(len(s))]
    for left in range(len(s) - 1, -1, -1): 

            dp[left][left] = 1

            for right in range(left + 1, len(s)):

                if s[left] == s[right]:
                    dp[left][right] = 2 + dp[left + 1][right - 1]
                else:
                    dp[left][right] = max(dp[left + 1][right], dp[left][right - 1])

    return len(s) - dp[0][len(s) - 1]

if __name__ == "__main__":
    print("1312. Minimum_Steps_To_Make_String_Palindrome.py")
    print("\nCase 1")
    s = "leetcode"
    result = minInsertions(s) 
    print(result)  # Output: 5

