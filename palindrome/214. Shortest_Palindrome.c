#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define MAX_LEN 1000

int max(int a, int b) {
    return a > b ? a : b;
}

void printDP(int len, int dp[len][len]) {
    printf("  DP Array Status:\n");
    for (int i = 0; i < len; i++) {
        for (int j = 0; j < len; j++) {
            if (j==0) {printf("\n    [%d] : %d", i, dp[i][j]);}
            else if (j==len-1) {printf("  %d\n", dp[i][j]);}
            else {printf("  %d", dp[i][j]);}
        }
    }
    printf("====================================\n");
}

int is_palindrome_i(char *s, int start, int end) {
    while (start < end) {
        if (s[start] != s[end])
            return 0;
        start++;
        end--;
    }
    return 1;
}

int is_palindrome(char *s){
    int n = strlen(s);
    for(int i=0;i<n/2;i++){
        if(s[i] != s[n-i-1]){
            return 0; // 0, false
        }
    }
    return 1; // 1, true
}

char *concat(const char *s1, const char *s2) {
    char *result = malloc(strlen(s1) + strlen(s2) + 1);
    if (result == NULL) {
        return NULL; // Memory allocation failed
    }
    strcpy(result, s1);
    strcat(result, s2);
    return result;
}

char *reverse(const char *s) {
    int len = strlen(s);
    char *reversed = malloc(len + 1);
    if (reversed == NULL) {
        return NULL; // Memory allocation failed
    }
    for (int i = 0; i < len; i++) {
        reversed[i] = s[len - i - 1];
    }
    reversed[len] = '\0';
    return reversed;
}

// // Function to reverse a string
// void strrev(char *s) {
//     int i, j;
//     char temp;
//     for (i = 0, j = strlen(s) - 1; i < j; i++, j--) {
//         temp = s[i];
//         s[i] = s[j];
//         s[j] = temp;
//     }
// }

// char shortestPalindrome(const char *s){
//     int ptr = 0;
//     int n = strlen(s);
//     // Allocate memory for ans
//     char ans = malloc(sizeof(char)*2*n);

//     int flag = 0;
//     for(int i=0; i<=n; i++){
//         char *prefix = malloc(i + 1);
//         strncpy(prefix, s, i); // copying string until i
//         prefix[i] = '\0'; // Null-terminate the string
//         if(is_palindrome(prefix) == 1 && flag == 0){// to get the point where it matches

//             char *suffix = malloc(n - i + 1);
//             strncpy(suffix, s+i, n);
//             reverse(suffix);
//             strcat(suffix, ans);
//             strcat(s, ans);
//             flag = 1;
//         } 
//         free(prefix);
//     }
//     return ans;
// }

char *shortestPalindrome(char *s) {
    int n = strlen(s);
    int i;

    // Iterate from the end towards the beginning of the string
    for (i = n - 1; i >= 0; i--) {
        // Check if the substring from index 0 to i is a palindrome
        if (is_palindrome_i(s, 0, i)) {
            // Allocate memory for the result string
            char *result = (char *)malloc(sizeof(char) * (n - i + n + 1));

            // Copy the reverse of the substring after the palindrome to the result string
            strcpy(result, s + i + 1);
            strrev(result);

            // Concatenate the result string with the original string and return
            strcat(result, s);
            return result;
        }
    }

    // If no palindrome is found, prepend the reverse of the entire string to the original string
    char *result = (char *)malloc(sizeof(char) * (n + n + 1));
    strcpy(result, s);
    strrev(result);
    strcat(result, s);
    // need to add null pointer at the end
    result[n] = '\0';
    return result;
}

int main() {
    printf("Palindrome\n");
    printf("====================================\n");
    printf("[Case 1]\n");
    char s1[] = "aacecaaa";
    char expected1[] = "aaacecaaa";
    char *res1 = shortestPalindrome(s1);
    printf("Input   : s = \"%s\"\n", s1);
    printf("Output  : %s\n", res1);
    printf("Check   : %s\n", strcmp(expected1, res1) == 0 ? "true" : "false");
    printf("====================================\n");

    printf("[Case 2]\n");
    char s2[] = "abcd";
    char expected2[] = "dcbabcd";
    char *res2 = shortestPalindrome(s2);
    printf("Input   : s = \"%s\"\n", s2);
    printf("Output  : %s\n", res2);
    printf("Check   : %s\n", strcmp(expected2, res2) == 0 ? "true" : "false");
    printf("====================================\n");

    // Free allocated memory
    free(res1);
    free(res2);

    // printf("[Case 3]\n");
    // char s3[] = "summuus";
    // int expected3 = 6;
    // int res3 = longestPalindromeSubseq(s3);
    // printf("Input   : s = \"%s\"\n", s3);
    // printf("Output  : %d\n", res3);
    // printf("Check   : %s\n", expected3==res3? "true":"false");
    // printf("====================================\n");

    // printf("[Case 4]\n");
    // char s4[] = "comcom";
    // int expected4 = 3;
    // int res4 = longestPalindromeSubseq(s4);
    // // int min_ins4 = min_Insertions(s4);
    // printf("Input   : s = \"%s\"\n", s4);
    // printf("Output  : %d\n", res4);
    // printf("Check   : %s\n", expected4==res4? "true":"false");
    // printf("====================================\n");
}


/*
// Version 1
void substring(char *source, int start, int end, char *target) {
    int length = end - start + 1;
    strncpy(target, source + start, length);
    target[length] = '\0'; // Null-terminate the target string
}

// Version 2
void substring(char *source, int start, int end) {
    int length = strlen(source);
    if (start < 0 || start >= length || end < start || end >= length) {
        printf("Invalid indices\n");
        return;
    }

    int i;
    for (i = start; i <= end; i++) {
        putchar(source[i]);
    }
    putchar('\n');
}*/