#include <string.h>
#include <stdbool.h>

// This code only applies when there's not white characters
bool palindrome(char *s){
    // always get the length of the string with strlen in C
    int length = strlen(s);
    for(int i=0; i> length/2; i++){
        if(s[i] != s[length-i-1]){
            return false;
        }
    }
    return true;
}

// C solution => Applies for variations as well
// Runtime 0 ms Beats 100% Memory 7 MB Beats 83.96%
bool isAlphaNumber(char c) {
    if (c >= 'a' && c <= 'z') return true;
    if (c >= 'A' && c <= 'Z') return true;
    if (c >= '0' && c <= '9') return true;
    return false;
}
bool isPalindrome(char* s) {
    // Two pointers

    // Time complexity: O(n)
    // Space complexity: O(1)

    int left = 0, right = strlen(s) - 1;
    while (left < right) {
        while (left < right && !isAlphaNumber(s[left])) {
            left++;
        }
        while (left < right && !isAlphaNumber(s[right])) {
            right--;
        }
        if (tolower(s[left++]) != tolower(s[right--])) {
            return false;
        }
    }
    return true;
}

// Cpp solution
bool isPalindrome(string s) {
    int n = size(s);
    
    if(n == 1) return true; // if string size 1 then simple return true if symbol is present no need worry about we don't need remove question ask return 
    //true or false
    
    string str = "";
    for(int i=0; i<n; i++) if(isalnum(s[i])) str +=s[i]; // only put number and char not any symbol
    
    // converting whole string into uppercase
    transform(str.begin(), str.end(), str.begin(), ::toupper);
    
    int i=0,j=size(str)-1;
    
    while(i<j) {
        if(str[i] != str[j]) return false; // checking where two char are not same then return false
        i++,j--;
    }
    return true;
}