from typing import List

def longestPalindrome(self, s: str) -> int:
        hm = Counter(s)
        even = [value for value in hm.values() if value % 2 == 0]
        odd = [value for value in hm.values() if value % 2 != 0]
        if odd: 
            use_odds = sum(odd) - (len(odd) - 1) 
            return sum(even) + use_odds
        else: 
            return sum(even)

               
if __name__ == "__main__":
    print("409. Longest_Palindrome.py")
    print("\nCase 1")
    s1 = "abccccdd"
    expected1 = 7
    res1 = longestPalindrome(s1) 
    print("Input   : s = ", s1)
    print("\nOutput  : ", res1)
    correct = (expected1==res1)
    print("\nCheck   : ", correct)
    print("\n====================================\n")

    print("\nCase 2")
    s2 = "a"
    expected2 = 1
    res2 = longestPalindrome(s2) 
    print("Input   : s = ", s2)
    print("\nOutput  : ", res2)
    correct = (expected2==res2)
    print("\nCheck   : ", correct)
    print("\n====================================\n")

    print("\nCase 1")
    s1 = "abb"
    expected1 = 3
    res1 = longestPalindrome(s1) 
    print("Input   : s = ", s1)
    print("\nOutput  : ", res1)
    correct = (expected1==res1)
    print("\nCheck   : ", correct)
    print("\n====================================\n")


'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = Counter(s)
        even = [value for value in hm.values() if value % 2 == 0]
        odd = [value for value in hm.values() if value % 2 != 0]
        if odd: 
            use_odds = sum(odd) - (len(odd) - 1) 
            return sum(even) + use_odds
        else: 
            return sum(even)


# When given the order of characters follows original order
def is_palindrome(s):
    return s == s[::-1]

def longestPalindrome(s: str) -> int:
    n = len(s)
    ans = 0
    if is_palindrome(s):
        return n
    # for all possible substrings [greedy]
    for i in range(n):
        for j in range(i+1, n+1):
            if is_palindrome(s[i:j]):
                ans = max(ans, j)
    return ans
'''