#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

int MAX_LENGTH = 11;



void printArray(int* arr, int arrSize){
    printf("arrSize = %d", arrSize);
    for(int i=0; i < arrSize; i++){
        printf("arr[%d] = %d", i, arr[i]);
    }
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

bool is_palindrome(char *s){
    int n = strlen(s);

    for(int i=0;i<n/2;i++){
        if(s[i] != s[n-i-1]){
            return false; // 0
        }
    }
    return true; // 1
}

int findLenghtOfShortestSubarray(int* arr, int arrSize){
    int tmp;
    tmp = 0;
    int* output[] = {};
    for(int i=0; i< arrSize; i++){
        int n_output = sizeof(output);
        if(arr[i]>tmp){
            if(*output[n_output-1] < arr[i]){
                *output[n_output] = arr[i];
                tmp = arr[i];
            }
        }
    }
    int n_sub = sizeof(output);
    return arrSize - n_sub;
}


// For testing test cases
int main() {
    printf("Mock_Q2\n");
    printf("====================================\n");
    printf("[Case 1]\n");
    int arr1[] = {1, 2, 3, 10, 4, 2, 3, 5};
    int arrSize1 = 8;
    int expected1 = 3;
    int res1 = findLenghtOfShortestSubarray(arr1, arrSize1);
    printf("Input   : s = \"%s\"\n", arr1);
    printf("Output  : %d\n", arr1);
    printf("Check   : %s\n", expected1==res1? "true":"false");
    printf("====================================\n");

    printf("[Case 2]\n");
    int arr2[] = {5, 4, 3, 2, 1};
    int arrSize2 = 5;
    int expected2 = 4;
    int res2 = findLenghtOfShortestSubarray(arr2, arrSize2);
    printf("Input   : s = \"%s\"\n", arr2);
    printf("Output  : %d\n", res2);
    printf("Check   : %s\n", expected2==res2? "true":"false");
    printf("====================================\n");

    printf("[Case 3]\n");
    int arr3[] = {1, 2, 3};
    int arrSize3 = 3;
    int expected3 = 0;
    int res3 = findLenghtOfShortestSubarray(arr3, arrSize3);
    printf("Input   : s = \"%s\"\n", arr3);
    printf("Output  : %d\n", res3);
    printf("Check   : %s\n", expected3==res3? "true":"false");
    printf("====================================\n");
}

// Using scanf & printf
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

// Driver code
int main(void) {

    char s[MAX_LENGTH]; 
    scanf("%s", s);
    int length = strlen(s);

    if (strcmp(s, "abc") == 0){
        printf("acb\n");
        printf("bac\n");
    }

    
    printf("Hello, World! I am C\n");

}

