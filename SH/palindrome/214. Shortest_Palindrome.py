def is_palindrome(s: str) -> bool:
    n = len(s)
    return s[:n//2] == s[-1:-n//2-1:-1]

def shortest_palindrome(s: str) -> str:
    n = len(s)
    for i in range(n - 1, -1, -1):
        if s[:i + 1] == s[i::-1]:
            return s[i + 1:][::-1] + s
    return s[::-1] + s

def shortestPalindrome(self, s: str) -> str:
    i = 0
    n = len(s)
    for j in range(n):
        if s[i] == s[n-j-1]:
            i += 1
    if i==n:
        return s
    p = s[i:n][::-1]
    return p + self.shortestPalindrome(s[:i]) + s[i:]

# Test the function
s = "aacecaaa"
print(shortest_palindrome(s))  # Output: "aaacecaaa"


# invalid
# def shortestPalindrome(s: str) -> str:
#     n = len(s)
#     flag = 0
#     for i in range(n, -1, -1):
#         if is_palindrome(s[:i]) and flag == 0:
#             if i == 0:
#                 ans = s[:i:-1] + s
#                 flag = 1
#             else:
#                 print(s[:i:-1])
#                 ans = s[:i:-1] + s
#                 flag = 1
#             break
#     return ans
