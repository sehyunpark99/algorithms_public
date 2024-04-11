'''
680. Valid Palindrome II
Easy
Topics
Companies
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
'''

class Solution:
    # def is_palindrome(self, s: str):
    #     n = len(s)
    #     if(n%2):
    #         return s[:n//2] == s[n:n//2:-1]
    #     else:
    #         return s[:n//2] == s[n:n//2-1:-1]
    def validPalindrome(self, s: str) -> bool:        
        start, end = 0, len(s)-1
        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return s[start:end] == s[start:end][::-1] or s[start+1:end+1] == s[start+1:end+1][::-1]
        return True
        
        

if __name__ == "__main__":
    print("680. Valid_Palindrome.py")

    solution = Solution()
    print("\nCase 1")
    chars = "aba"
    res = solution.validPalindrome(chars)  
    ans = True
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 2")
    chars = "abc"
    res = solution.validPalindrome(chars)  
    ans = False
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 3")
    chars = "abca"
    res = solution.validPalindrome(chars)  
    ans = True
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 4")
    chars = "deeee"
    res = solution.validPalindrome(chars)  
    ans = True
    print(res, "\n  ==> check: ", res==ans)