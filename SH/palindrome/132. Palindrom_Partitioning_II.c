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

int minCut(char *s) {
    int len = strlen(s);
    int dp[len][len];
    memset(dp, 0, sizeof(dp)); // Since C randomly initialize the numbers in the table, we should set the memory

    // Step 1: Preprocess the string to determine which substrings are palindrome
    for(int i=0; i<len; i++){dp[i][i] = 1;}
    for(int i=0; i<len-1; i++){
        if(s[i]==s[i+1]){
            dp[i][i+1]=1;
        }
    }
    for (int length = 3; length <= len+1; length++) {
        for (int j = 0; j < len-length+1; j++) {
            if (s[j] == s[j-length+1] && dp[j+1][j+length-1] == 1) {
                dp[j][j+length-1] = 1;
            }
        }
        // printDP(len, dp);
    }
    // printDP(len, dp);
    int cuts[len];
    memset(cuts, 0, sizeof(cuts));
    for(int i=0; i<len; i++){
        cuts[i] = i;
    }
    for(int i=1; i<len; i++){
        if(dp[0][i]){
            cuts[i] = 0;
        }
        else{
            for(int j=0; j<i; j++){
                if(dp[j+1][i]){
                    cuts[i] = min(cuts[i], cuts[j]+1);
                }
            }
        }
    }
    return cuts[len-1];
}

int main() {
    printf("132 Palindrome_Partitioning\n");
    printf("====================================\n");
    printf("[Case 1]\n");
    char s1[] = "aab";
    int expected1 = 1;
    int res1 = minCut(s1);
    printf("Input   : s = \"%s\"\n", s1);
    printf("Output  : %d\n", res1);
    printf("Check   : %s\n", expected1==res1? "true":"false");
    printf("====================================\n");

    printf("[Case 2]\n");
    char s2[] = "a";
    int expected2 = 0;
    int res2 = minCut(s2);
    printf("Input   : s = \"%s\"\n", s2);
    printf("Output  : %d\n", res2);
    printf("Check   : %s\n", expected2==res2? "true":"false");
    printf("====================================\n");

    printf("[Case 3]\n");
    char s3[] = "leet";
    int expected3 = 2;
    int res3 = minCut(s3);
    printf("Input   : s = \"%s\"\n", s3);
    printf("Output  : %d\n", res3);
    printf("Check   : %s\n", expected3==res3? "true":"false");
    printf("====================================\n");
}

/*
'''
132. Palindrome Partitioning II
Hard
Topics
Companies
Given a string s, partition s such that every 
substring of the partition is a 
palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
'''
*/