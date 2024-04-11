class Solution {
public:
    string longestPalindrome(string s) {
        int maxStart = 0;       
        // Initialize starting index of the longest palindrome
        int maxLength = 1;      
        // Initialize length of the longest palindrome
        
        // Iterate through each character in the string
        for (int i = 0; i < s.size() - 1; i++) {
            // Expand around the current character and its next character (for even-length palindromes)
            middleOut(s, i, i, maxStart, maxLength);       
            // Check odd-length palindromes
            middleOut(s, i, i + 1, maxStart, maxLength);   
            // Check even-length palindromes
        }
        
        return s.substr(maxStart, maxLength);     
        // Return the longest palindromic substring
    }
private:
    // Function to expand around the middle and update maxStart and maxLength if a longer palindrome is found
    void middleOut(string s, int i, int j, int& maxStart, int& maxLength) {
        // Expand around the middle while characters match
        while (i >= 0 && j <= s.size() - 1 && s[i] == s[j]) {
            i--;        
            // Move left pointer to the left
            j++;        
            // Move right pointer to the right
        }
        // Check if the current palindrome is longer than the previous longest palindrome
        if (j - i - 1 > maxLength) {
            maxStart = i + 1;       
            // Update starting index of the longest palindrome
            maxLength = j - i - 1;  
            // Update length of the longest palindrome
        }
    }
};