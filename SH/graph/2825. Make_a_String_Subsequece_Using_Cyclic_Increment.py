'''

2825. Make String a Subsequence Using Cyclic Increments
Medium
Topics
Companies
Hint
You are given two 0-indexed strings str1 and str2.

In an operation, you select a set of indices in str1, and for each index i in the set, increment str1[i] to the next character cyclically. That is 'a' becomes 'b', 'b' becomes 'c', and so on, and 'z' becomes 'a'.

Return true if it is possible to make str2 a subsequence of str1 by performing the operation at most once, and false otherwise.

Note: A subsequence of a string is a new string that is formed from the original string by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.
'''

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0 # variable to store the i
        j = 0 # variable to store the j
        n = len(str1) # variable to store the size of the str1
        m = len(str2) # variable to store the size of the str2
        while(i<n and j<m): # loop until i is less than n and j is less than m
              if str2[j] in {str1[i], chr(ord(str1[i]) + 1), chr(ord(str1[i]) - 25)}:  # if str1[i] is equal to str2[j] or str1[i]+1 is equal to str2[j] or str1[i] - 25 is equal to str2[j]
                j += 1 # increment the j
            i += 1 # increment the i
        return j == m # return true if j is equal to m else return false
    
# C
# bool canMakeSubsequence(char * str1, char * str2){
#     int i = 0; // variable to store the i
#     int j = 0; // variable to store the j
#     int n = strlen(str1); // variable to store the size of the str1
#     int m = strlen(str2); // variable to store the size of the str2
#     while(i<n && j<m){ // loop until i is less than n and j is less than m
#         if(str1[i] == str2[j] || str1[i]+1 == str2[j] || str1[i] - 25 == str2[j]){  // if str1[i] is equal to str2[j] or str1[i]+1 is equal to str2[j] or str1[i] - 25 is equal to str2[j]
#             j++; // increment the j
#         }
#         i++; // increment the i
#     }
#     return j == m; // return true if j is equal to m else return false
# }