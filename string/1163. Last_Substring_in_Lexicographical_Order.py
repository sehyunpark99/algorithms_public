# 1163. Last Substring in Lexicographical Order
# Hard
# Topics
# Companies
# Hint
# Given a string s, return the last substring of s in lexicographical order.

 

# Example 1:

# Input: s = "abab"
# Output: "bab"
# Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
# Example 2:

# Input: s = "leetcode"
# Output: "tcode"
 

# Constraints:

# 1 <= s.length <= 4 * 105
# s contains only lowercase English letters.

class Solution:
    def lastSubstring(self, s: str) -> str:
        i,j,k=0,1,0
        n=len(s)
        while j+k<n:
            
            if s[i+k]==s[j+k]:
                k+=1
                continue
            elif s[i+k]>s[j+k]:
                j=j+k+1
            else:
                i=max(j,i+k+1)
                j=i+1
            k=0
        return s[i:]
    
class Solution:
    def lastSubstring(self, s: str) -> str:
        S, L, a = [ord(i) for i in s] + [0], len(s), 1
        M = max(S)
        I = [i for i in range(L) if S[i] == M]
        if len(I) == L: return s
        while len(I) != 1:
            b = [S[i + a] for i in I]
            M, a = max(b), a + 1
            I = [I[i] for i, j in enumerate(b) if j == M]
        return s[I[0]:]
		
		