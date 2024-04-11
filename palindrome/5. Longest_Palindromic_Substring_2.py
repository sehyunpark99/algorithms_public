'''
5. Longest Palindromic Substring
Medium

Given a string s, return the longest 
palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
'''

# My answer; couldn't get all edge cases
class Solution:
    def is_palindrome(self, s: str):
        str_num = str(s)
        n = len(str_num)
        if(n%2): # if x has odd size
            if str_num[0:n//2] == str_num[n:n//2:-1]:
                return True
        else:
            if str_num[0:n//2] == str_num[n:n//2-1:-1]:
                return True
        return False
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        d = [[0 for _ in range(n)] for _ in range(n)] # to store whether it is palidrome or not
        for i in range(n):
            for j in range(i, n):
                if self.is_palindrome(s[i:j+1]):
                    d[i][j] = d[i][j-1] + 1
                else:
                    d[i][j] = d[i][j-1]

        max_value = float('-inf')  # Initialize max_value to negative infinity
        max_row_index = -1  # Initialize max_row_index to -1

        for i, row in enumerate(d):
            row_max = max(row)  # Find the maximum value in the current row
            if row_max > max_value:  # If the maximum value in the current row is greater than the overall maximum value
                max_value = row_max  # Update the overall maximum value
                max_row_index = i  # Update the row index where the maximum value is located

        list_ = d[max_row_index]
        min_index, max_index = n, n
        for i in range(len(list_)):
            if list_[i] == 1 and i < min_index:
                min_index = i
            if list_[i] == max_value and i < max_index:
                max_index = i

        return s[min_index:max_index+1]

# Answer 
# We initialize a boolean table dp and mark all the values as false.
# We will use a variable max_len to keep track of the maximum length of the palindrome.
# We will iterate over the string and mark the diagonal elements as true as every single character is a palindrome.
# Now, we will iterate over the string and for every character we will expand around its center.
# For odd length palindrome, we will consider the current character as the center and expand around it.
# For even length palindrome, we will consider the current character and the next character as the center and expand around it.
# We will keep track of the maximum length and the maximum substring.
# Print the maximum substring.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]): # condition for palindrome
                    dp[j][i] = True
                    if i-j+1 > Max_Len:
                        Max_Len = i-j+1
                        Max_Str = s[j:i+1]
        return Max_Str

if __name__ == "__main__":
    print("5. Longest_Palindromic_Substring.py")

    solution = Solution()
    print("\nCase 1")
    chars = "babad"
    res = solution.longestPalindrome(chars)  
    ans = "bab"
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 2")
    chars = "cbbd"
    res = solution.longestPalindrome(chars)  
    ans = "bb"
    print(res, "\n  ==> check: ", res==ans)


'''
# Wrong
def longestPalindrome(s: str) -> str:
    idx_length = len(s)
    memo = [0] * (idx_length+1) # make memoization space for all characters
    inverse = s[::-1]
    for i in range(1, idx_length+1):
        prev = [0] * (idx_length+1)
        for j in range(1, idx_length+1):
            if s[i-1] == inverse[j-1]:
                memo[j] = 1+prev[j-1]
            else:
                memo[j] = max(prev[j], memo[j-1])
        prev = memo[:]
       
    return prev[idx_length]

'''