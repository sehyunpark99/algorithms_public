#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_LEN 1000

int min(int a, int b) {
    return a < b ? a : b;
}

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

int minInsertions(char *s) {
    int len = strlen(s);
    int dp[len][len];
    memset(dp, 0, sizeof(dp)); // Since C randomly initialize the numbers in the table, we should set the memory

    for (int left = len - 1; left >= 0; left--) {
        dp[left][left] = 1;
        for (int right = left + 1; right < len; right++) {
            if (s[left] == s[right]) {
                dp[left][right] = 2 + dp[left + 1][right - 1];
            } else {
                dp[left][right] = max(dp[left + 1][right], dp[left][right - 1]);
            }
        }
        // printDP(len, dp);
    }
    return len - dp[0][len - 1];
}

int main() {
    printf("1312_Minimum Insertion Steps to Make a String Palindrome\n");
    printf("====================================\n");
    printf("[Case 1]\n");
    char s1[] = "zzazz";
    int expected1 = 0;
    int res1 = minInsertions(s1);
    printf("Input   : s = \"%s\"\n", s1);
    printf("Output  : %d\n", res1);
    printf("Check   : %s\n", expected1==res1? "true":"false");
    printf("====================================\n");

    printf("[Case 2]\n");
    char s2[] = "mbadm";
    int expected2 = 2;
    int res2 = minInsertions(s2);
    printf("Input   : s = \"%s\"\n", s2);
    printf("Output  : %d\n", res2);
    printf("Check   : %s\n", expected2==res2? "true":"false");
    printf("====================================\n");

    printf("[Case 3]\n");
    char s3[] = "leetcode";
    int expected3 = 5;
    int res3 = minInsertions(s3);
    printf("Input   : s = \"%s\"\n", s3);
    printf("Output  : %d\n", res3);
    printf("Check   : %s\n", expected3==res3? "true":"false");
    printf("====================================\n");
}

/*
Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
*/