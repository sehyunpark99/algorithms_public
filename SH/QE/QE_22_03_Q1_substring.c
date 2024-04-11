// In this problem, given a string s, you will finally implement a function max palindromes(s)
// that returns a list of substrings of s that are maximal palindromes. That is, the list contains palindromes
// that are not a substring of another palindrome. A string of characters is a palindrome if it is identical to
// its reversion. A substring is a contiguous sequence of characters within a string. The characters used in a
// string are only lower-case alphabets and a space character. You may not use any built-in functions
// in Python.
// For example,
// • For s = "k abccba dzd efgfe da",
// max palindromes(s) should return ["k", "abccba", "dzd", "defgfed"].
// • For s = "kabccba dzabccbaza",
// max palindromes(s) should return ["k", " ", "d", "zabccbaz", "aza"].
// (a) [10 pts] Write a function palindrome(s) that checks if the string s is a palindrome.
// (b) [10 pts] Write a function substring(s, t) that checks if the string t is a substring of the string
// s.
// (c) [30 pts] Write the function max palindromes(s) that uses palindrome(s) and substring(s, t).
// The submission file QE prob1.py should only contain the implementations of the three functions
// palindrome(s), substring(s, t), and max palindromes(s). You will likely get a lower score if
// there is any print or debugging code in your submission.


// #include <string.h>
// #include <stdbool.h>
// #include <stdio.h>

// // (a) whether the letter is a palidrome or not
// bool palindrome(char *s){
//     // always get the length of the string with strlen in C
//     int length = strlen(s);
//     for(int i=0; i> length/2; i++){
//         if(s[i] != s[length-i-1]){
//             return false;
//         }
//     }
//     return true;
// }


// // (b) write a function substring(S, t) for checking the substring of the string => prepare subsequence as well
// bool substring(const char *s, const char *t){
//     if(strstr(s,t) != NULL){
//         return true;
//     }
//     else{
//         return false;
//     }
// }

// // (c) max_palindromes using palindrome and substring 
// // For substring, better use pointer. 
// // But for this qn, since we need to use (b) just try brute force
// // Helper function to add a substring to the list of max palindromes
// void add_max_palindrome(const char *s, int start, int end, char **max_palindromes, int *count) {
//     int length = end - start + 1;
//     max_palindromes[*count] = (char *)malloc(length + 1);
//     strncpy(max_palindromes[*count], s + start, length);
//     max_palindromes[*count][length] = '\0';
//     (*count)++;
// }

// void max_palindromes(char *s){
//     int n = strlen(s);
//     int *count = 0;
//     char **max_palindromes[];
//     for(int i=0; i<n; i++){
//         for(int j=0; j<n; j++){
//             char *sub = (char *)malloc(j - i + 2); // better to allocate memory when we are assigning
//             strncpy(sub, s2+i, j-i+1);
//             sub[j - i + 1] = '\0'; // should always add on nulll character
//             if(palindrome(s1)){
//                 bool maximal = true;
//                 if 
//                 add_list(s1);
//             }
//         }
//     }
// }

// // GPT Version
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool palindrome(const char *s) {
    int length = strlen(s);
    for (int i = 0; i < length / 2; i++) {
        if (s[i] != s[length - i - 1]) {
            return false;
        }
    }
    return true;
}

// bool substring(const char *s, const char *t) {
//     return strstr(s, t) != NULL;
// }

// Function to check if string t is a substring of string s
bool substring(const char *s, const char *t) {
    int s_len = strlen(s);
    int t_len = strlen(t);
    
    // Iterate through each character in s
    for (int i = 0; i <= s_len - t_len; i++) {
        bool match = true;
        
        // Check if the substring of s starting from index i matches t
        for (int j = 0; j < t_len; j++) {
            if (s[i + j] != t[j]) {
                match = false;
                break;
            }
        }
        
        // If match is true, return true
        if (match) {
            return true;
        }
    }
    
    // If no match is found, return false
    return false;
}


// bool is_palindrome(const char *s, int start, int end) {
//     while (start < end) {
//         if (s[start] != s[end]) {
//             return false;
//         }
//         start++;
//         end--;
//     }
//     return true;
// }

void add_max_palindrome(const char *s, int start, int end, char **max_palindromes, int *count) {
    int length = end - start + 1;
    max_palindromes[*count] = (char *)malloc(length + 1);
    strncpy(max_palindromes[*count], s + start, length);
    max_palindromes[*count][length] = '\0';
    (*count)++;
}

void max_palindromes(const char *s, char **max_palindromes, int *count) {
    int length = strlen(s);
    *count = 0;
    for (int i = 0; i < length; i++) {
        for (int j = i; j < length; j++) {
            char *sub = (char *)malloc(j - i + 2);
            strncpy(sub, s + i, j - i + 1);
            sub[j - i + 1] = '\0';
            if (palindrome(sub)) {
                bool is_maximal = true;
                for (int k = 0; k < *count; k++) {
                    if (substring(max_palindromes[k], sub)) {
                        is_maximal = false;
                        break;
                    }
                }
                if (is_maximal) {
                    add_max_palindrome(s, i, j, max_palindromes, count);
                }
            }
            free(sub);
        }
    }
}


int main() {
    printf("QE_22_03_Q1\n");
    printf("====================================\n");
    printf("[Case 1]\n");
    char s1[] = "kabccbadzdefgfeda";
    int count1;
    char *max_palindromes1[100]; // Allocate memory for max_palindromes array
    max_palindromes(s1, max_palindromes1, &count1);
    printf("Input   : s = \"%s\"\n", s1);
    printf("Output  : ");
    for (int i = 0; i < count1; i++) {
        printf("%s ", max_palindromes1[i]);
        free(max_palindromes1[i]); // Free allocated memory
    }
    printf("\n");
    printf("====================================\n");

    printf("[Case 2]\n");
    char s2[] = "kabccba dzabccbaza";
    int count2;
    char *max_palindromes2[100]; // Allocate memory for max_palindromes array
    max_palindromes(s2, max_palindromes2, &count2);
    printf("Input   : s = \"%s\"\n", s2);
    printf("Output  : ");
    for (int i = 0; i < count2; i++) {
        printf("%s ", max_palindromes2[i]);
        free(max_palindromes2[i]); // Free allocated memory
    }
    printf("\n");
    printf("====================================\n");

    return 0;
}


// Result
// QE_22_03_Q1
// ====================================
// [Case 1]
// Input   : s = "kabccbadzdefgfeda"
// Output  : k a abccba d dzd defgfed
// ====================================
// [Case 2]
// Input   : s = "kabccba dzabccbaza"
// Output  : k a abccba   d z zabccbaz aza
// ====================================

// Main Function
// int main() {
//     printf("Enter a string: ");
//     char input[100];
//     scanf("%s", input);

//     int count;
//     char *max_palindromes[100]; // Allocate memory for max_palindromes array
//     max_palindromes(input, max_palindromes, &count);

//     printf("Input   : s = \"%s\"\n", input);
//     printf("Output  : ");
//     for (int i = 0; i < count; i++) {
//         printf("%s ", max_palindromes[i]);
//         free(max_palindromes[i]); // Free allocated memory
//     }
//     printf("\n");

//     return 0;
// }



// For subsequence not the substring
// #include <stdio.h>
// #include <stdlib.h>
// #include <stdbool.h>
// #include <string.h>

// bool palindrome(const char *s) {
//     int length = strlen(s);
//     for (int i = 0; i < length / 2; i++) {
//         if (s[i] != s[length - i - 1]) {
//             return false;
//         }
//     }
//     return true;
// }

// void add_max_palindrome(const char *s, int start, int end, char **max_palindromes, int *count) {
//     int length = end - start + 1;
//     max_palindromes[*count] = (char *)malloc(length + 1);
//     strncpy(max_palindromes[*count], s + start, length);
//     max_palindromes[*count][length] = '\0';
//     (*count)++;
// }

// void max_palindromes(const char *s, char **max_palindromes, int *count) {
//     int length = strlen(s);
//     *count = 0;
//     for (int i = 0; i < length; i++) {
//         for (int j = i; j < length; j++) {
//             char *sub = (char *)malloc(j - i + 2);
//             int k = 0;
//             for (int l = i; l <= j; l++) {
//                 sub[k++] = s[l];
//             }
//             sub[k] = '\0';
//             if (palindrome(sub)) {
//                 bool is_maximal = true;
//                 for (int m = 0; m < *count; m++) {
//                     if (strstr(max_palindromes[m], sub) != NULL) {
//                         is_maximal = false;
//                         break;
//                     }
//                 }
//                 if (is_maximal) {
//                     add_max_palindrome(s, i, j, max_palindromes, count);
//                 }
//             }
//             free(sub);
//         }
//     }
// }

// int main() {
//     printf("Enter a string: ");
//     char input[100];
//     scanf("%s", input);

//     int count;
//     char *max_palindromes[100]; // Allocate memory for max_palindromes array
//     max_palindromes(input, max_palindromes, &count);

//     printf("Input   : s = \"%s\"\n", input);
//     printf("Output  : ");
//     for (int i = 0; i < count; i++) {
//         printf("%s ", max_palindromes[i]);
//         free(max_palindromes[i]); // Free allocated memory
//     }
//     printf("\n");

//     return 0;
// }

