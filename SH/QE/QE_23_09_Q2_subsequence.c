// Given a string `s`, return the minimum number of characters that need to be deleted to obtain the 
// longest palindromic subsequence and the resulting subsequence itself. 
// **Constraints**:
// - The length of `s` is between 1 and 10. char s[11] // malloc(sizeof(char)*11)
// - `s` consists only of lowercase English letters.
// **Example 1**:
// Input -> s = "unique"
// 3
// unu
// **Example 2**:
// Input -> s = "radar"
// 0
// radar

// **Note**:
// - In the first example, by deleting three characters "iqe" from "unique", we can form the 
// palindromic subsequence "unu".
// - In the second example, "radar" is already a palindrome, so no deletions are necessary.
// **Approach**:
// 1. Determine the length of the given string. strlen(s)
// 2. Initialize a 2D dynamic programming table.
// 3. Compute the length of the longest palindromic subsequence.
// 4. Determine the number of characters to be deleted as `length of s - length of the longest 
// palindromic subsequence`.
// 5. Backtrack to retrieve the actual subsequence.
// 6. Print the results.

// **Requirements**:
// - Use `scanf` to get the input string.
// - Use `printf` to print the results.
// - The entire program should work correctly with the provided `main` function.
// The problem now focuses on the number of deletions to achieve the longest palindromic 
// subsequence and provides the desired subsequence


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// int min_deletion(char *s){
//     int n = strlen(s);
//     int dp[n][n];
//     memset(dp, 0, sizeof(dp)); // initialize all elements

//     for(int i=0; i < n; i++){
//         dp[i][i] = 1; // diagonal elements to 1
//     }

//     for(int i=n-1; i >= 0; i--){
//         for(int j=i-1; j<n; j++){
//             if s[i] == s[j]
//         }

//     }

// }


// int main() {
//     printf("QE_23_09_Q2\n");
//     printf("====================================\n");
//     printf("[Case 1]\n");
//     char s1[] = "radar";
//     int expected1 = 0;
//     int res1 = min_deletion(s1);
//     printf("Input   : s = \"%s\"\n", s1);
//     printf("Output  : %d\n", res1);
//     printf("Check   : %s\n", expected1==res1? "true":"false");
//     printf("====================================\n");

//     printf("[Case 2]\n");
//     char s2[] = "unique";
//     int expected2 = 3;
//     int res2 = min_deletion(s2);
//     printf("Input   : s = \"%s\"\n", s2);
//     printf("Output  : %d\n", res2);
//     printf("Check   : %s\n", expected2==res2? "true":"false");
//     printf("====================================\n");
// }

// // For implementing scanf
// int main() {
//     int num;
//     printf("Enter an integer: ");
//     scanf("%d", &num); // Reads an integer from the user and stores it in the variable num
//     printf("You entered: %d\n", num);
//     return 0;
// }

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to compute the length of the longest palindromic subsequence
int longestPalindromicSubsequence(char *s, int n) {
    // Initialize a 2D dynamic programming table
    int dp[n][n];
    memset(dp, 0, sizeof(dp)); // Initialize with zeros

    // Base case: single character is always a palindrome of length 1
    for (int i = 0; i < n; i++) {
        dp[i][i] = 1;
    }

    // Traverse for all possible lengths of substrings
    for (int len = 2; len <= n; len++) {
        for (int i = 0; i < n - len + 1; i++) {
            int j = i + len - 1; // Set ending index

            // If the ends of the string are equal
            if (s[i] == s[j]) {
                dp[i][j] = dp[i + 1][j - 1] + 2;
            } else {
                dp[i][j] = (dp[i][j - 1] > dp[i + 1][j]) ? dp[i][j - 1] : dp[i + 1][j];
            }
        }
    }

    // Return the length of the longest palindromic subsequence
    return dp[0][n - 1];
}

// Function to retrieve the longest palindromic subsequence
// this does not work properly
void getLongestPalindromicSubsequence(char *s, int n, char *result) {
    int i = 0, j = n - 1, index = 0;
    char lps[n]; // To store the longest palindromic subsequence
  
    // Construct the longest palindromic subsequence
    while (i < n && j >= 0) {
        if (s[i] == s[j]) {
            lps[index++] = s[i];
            i++;
            j--;
        } else if (i + 1 < n && j - 1 >= 0 && s[i + 1] == s[j] && s[i] != s[j - 1]) {
            i++;
        } else {
            j--;
        }
    }

    // Add the middle character if the length is odd
    if (i == j) {
        lps[index++] = s[i];
    }

    // Copy the longest palindromic subsequence to the result array
    for (int k = 0; k < index; k++) {
        result[k] = lps[k];
    }

    result[index] = '\0'; // Add null terminator to make it a valid string
}

char* getPalindrome(char* s, int k){
    if(k == 0){
        return s;
    }
    int palindromeLen = strlen(s) - k;
    int count[26], count2[26]; // alphabets
    for(int i=0;i<26;i++){
        // initialize
        count[i] = 0;
        count2[i] = 0;
    }
    for(int i=0;i<strlen(s);i++){
        int idx = s[i] - 'a';
        count[idx]++; // count the number of instance for each alphabets
    }
    char *answer = (char*)malloc((palindromeLen)*sizeof(char));
    int aIdx = 0;
    int sIdx = 0;
    while(aIdx < palindromeLen / 2){
        int idx = s[sIdx] - 'a';
        // 2번째 조건 들어가는 이유는 nnniin 이런 경우를 막으려고
        if(count[idx] >= 2 && count2[idx] < count[idx]/2){
            answer[aIdx++] = s[sIdx];
            count2[idx]++;
        }
        sIdx++;
    }
    // Odd length
    if(palindromeLen % 2 == 1){
        answer[aIdx++] = s[sIdx];
    }
    // 뒷 부분 이어 붙어주기
    while(aIdx < palindromeLen){
        answer[aIdx] = answer[palindromeLen - aIdx - 1];
        aIdx++;
    }
    answer[palindromeLen] = '\0';
    return answer;
}

int main() {
    // Input string
    char s[11];
    printf("Enter the string: ");
    scanf("%s", s);

    int n = strlen(s); // Length of the string

    // Compute the length of the longest palindromic subsequence
    int longestLength = longestPalindromicSubsequence(s, n);

    // Number of characters to be deleted
    int deletions = n - longestLength;

    // Retrieve the longest palindromic subsequence
    char result[n];
    getLongestPalindromicSubsequence(s, n, result);


    // Print the results
    printf("%d\n", deletions);
    printf("%s\n", result);

    printf("%s\n", getPalindrome(s, deletions));

    return 0;
}


/*
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stddef.h>
#include <string.h>


int main(){
    char s[10], t[110]; 
    scanf("%s", s);

    int slen = strlen(s);
    int delete = 0;
    char * answer = malloc((10)*sizeof(char));
    char * finalanswer = malloc((10)*sizeof(char));
    int odd = 0;
    int mindelete = 10;

    for (int i=0; i<slen;i++){
        int l=i, r=slen-1;
        int j=0;

        while(l<r){
            while(l<r && (s[l]!=s[r])){
                r--;
                delete++;
                }
            if (s[l]==s[r] && l<r){
                answer[j]=s[l];
                l++;
                r--;
                j++;
            }
        }
        if(l==r){
            answer[j] = s[l];
            odd = 1;
        }
        if(mindelete>delete){
            mindelete = delete;
            for (int i=0; i<strlen(answer);i++){
                finalanswer[i] = answer[i];
            }
        }
    }
    
    printf("%d\n", mindelete);

    printf("%s", finalanswer);
    int tmp = strlen(finalanswer);
    if (odd){
        for(int j=tmp-2;j>=0;j--){
            printf("%c",finalanswer[j]);
        }
    } else {
         for(int j=tmp-1;j>=0;j--){
            printf("%c",finalanswer[j]);
        }
    }
    return 0;
}
*/