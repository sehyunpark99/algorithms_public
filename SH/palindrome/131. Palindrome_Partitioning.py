'''
131. Palindrome Partitioning
Medium
Topics
Companies
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
'''
from typing import List

def partition(s: str) -> List[List[str]]:
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
            


if __name__ == "__main__":
    print("131. Palindrome_Partitioning.py")
    print("\nCase 1")
    s = "a"
    result = partition(s) 
    print(result)  # Output: [["a"]]
    print("\nCase 2")
    s = "aab"
    result = partition(s) 
    print(result)  # Output: [["a","a","b"],["aa","b"]]

'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ans = []
        if n == 0:
            return [[]]
        for i in range(1, n + 1):
            if s[:i] != s[:i][::-1]:
                continue
            cur = self.partition(s[i:])
            for j in range(len(cur)):
                ans.append([s[:i]] + cur[j])
        return ans


# greedy, slow & requires quite a lot of memory
class Solution(object):
    @cache  # the memory trick can save some time
    def partition(self, s):
        if not s: return [[]]
        ans = []
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:  # prefix is a palindrome
                for suf in self.partition(s[i:]):  # process suffix recursively
                    ans.append([s[:i]] + suf)
        return ans
'''