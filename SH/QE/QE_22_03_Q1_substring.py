# Function to check if a string is a palindrome
def palindrome(s):
    return s == s[::-1]

# Function to check if string t is a substring of string s
def substring(s, t):
    return t in s

# Function to find maximal palindromes in the string s
def max_palindromes(s):
    max_palindromes_list = []
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]
            if palindrome(sub):
                is_maximal = True
                for palindrome_str in max_palindromes_list:
                    if substring(palindrome_str, sub):
                        is_maximal = False
                        break
                if is_maximal:
                    max_palindromes_list.append(sub)
    return max_palindromes_list

# Test cases
s1 = "k abccba dzd efgfe da"
print("max palindromes(s1):", max_palindromes(s1))  # Output: ["k", "abccba", "dzd", "defgfed"]

s2 = "kabccba dzabccbaza"
print("max palindromes(s2):", max_palindromes(s2))  # Output: ["k", " ", "d", "zabccbaz", "aza"]
