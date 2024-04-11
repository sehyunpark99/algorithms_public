#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

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

bool is_palindrome(char *s){
    int n = strlen(s);

    for(int i=0;i<n/2;i++){
        if(s[i] != s[n-i-1]){
            return false; // 0
        }
    }
    return true; // 1
}

int longestPalindromeSubseq(const char *s) {
    int n = strlen(s);
    int dp[n][n];
    memset(dp, 0, sizeof(dp)); // Initialize all elements to 0

    for (int left = n - 1; left >= 0; --left) {
        dp[left][left] = 1;

        for (int right = left + 1; right < n; ++right) {
            if (s[left] == s[right]) {
                dp[left][right] = 2 + dp[left + 1][right - 1];
            } else {
                dp[left][right] = max(dp[left + 1][right], dp[left][right - 1]);
            }
        }
    }
    printDP(n, dp);
    return dp[0][n - 1];
}


int main() {
    printf("Palindrome\n");
    printf("====================================\n");
    printf("[Case 1]\n");
    char s1[] = "bbbab";
    int expected1 = 4;
    int res1 = longestPalindromeSubseq(s1);
    printf("Input   : s = \"%s\"\n", s1);
    printf("Output  : %d\n", res1);
    printf("Check   : %s\n", expected1==res1? "true":"false");
    printf("====================================\n");

    printf("[Case 2]\n");
    char s2[] = "cbbd";
    int expected2 = 2;
    int res2 = longestPalindromeSubseq(s2);
    printf("Input   : s = \"%s\"\n", s2);
    printf("Output  : %d\n", res2);
    printf("Check   : %s\n", expected2==res2? "true":"false");
    printf("====================================\n");

    printf("[Case 3]\n");
    char s3[] = "summuus";
    int expected3 = 6;
    int res3 = longestPalindromeSubseq(s3);
    printf("Input   : s = \"%s\"\n", s3);
    printf("Output  : %d\n", res3);
    printf("Check   : %s\n", expected3==res3? "true":"false");
    printf("====================================\n");

    printf("[Case 4]\n");
    char s4[] = "comcom";
    int expected4 = 3;
    int res4 = longestPalindromeSubseq(s4);
    // int min_ins4 = min_Insertions(s4);
    printf("Input   : s = \"%s\"\n", s4);
    printf("Output  : %d\n", res4);
    printf("Check   : %s\n", expected4==res4? "true":"false");
    printf("====================================\n");
}








/*
#include <stdio.h>
#include <string.h>

int max(int a, int b) {
    return (a > b) ? a : b;
}

int longestPalindromeSubseq(const char *s) {
    int n = strlen(s);
    int dp[n][n];
    memset(dp, 0, sizeof(dp)); // Initialize all elements to 0

    for (int left = n - 1; left >= 0; --left) {
        dp[left][left] = 1;

        for (int right = left + 1; right < n; ++right) {
            if (s[left] == s[right]) {
                dp[left][right] = 2 + dp[left + 1][right - 1];
            } else {
                dp[left][right] = max(dp[left + 1][right], dp[left][right - 1]);
            }
        }
    }

    return dp[0][n - 1];
}

int main() {
    char s[] = "your_sample_string_here";
    printf("Length of longest palindromic subsequence: %d\n", longestPalindromeSubseq(s));
    return 0;
}
*/