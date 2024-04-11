#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

void printArray(int* arr, int arrSize){
    printf("arrSize = %d", arrSize);
    for(int i=0; i < arrSize; i++){
        printf("arr[%d] = %d \n", i, arr[i]);
    }
}

// Invalid due to memory allocation
// int findLenghtOfShortestSubarray(int* arr, int arrSize){
//     int* tmp = 0;
//     int* output[];
//     for(int i=0; i< arrSize; i++){
//         int n_output = sizeof(output);
//         if(arr[i]>tmp){
//             if(output)
//             output[i] = arr[i];
//         }
//     }
//     int n_sub = sizeof(output);
//     return arrSize - n_sub;
// }



// Improved by GPT
// int findLengthOfShortestSubarray(int* arr, int arrSize){
//     int* output = (int*)malloc(sizeof(int) * arrSize);
//     if (output == NULL) {
//         printf("Memory allocation failed\n");
//         return -1; // Return -1 to indicate failure
//     }

//     output[0] = arr[0]; // Store the first element of arr in output
//     int n_sub = 1; // Initialize the number of elements in the subarray to 1

//     for(int i=0; i< arrSize; i++){
//         if(arr[i]>output[n_sub-1]){
//             output[n_sub++] = arr[i];
//         }
//     }
//      // Calculate the length of the shortest subarray
//     int shortestSubarrayLength = arrSize - n_sub;
//     free(output);

//     return shortestSubarrayLength;
// }

int findLengthOfShortestSubarray(int* arr, int arrSize) {
    int left = 0;
    int right = arrSize-1;

    // From left, spot non-decreasing point (should be adjacent ones)
    while(left<right && arr[left] <= arr[left+1]){
        left++;
    }

    // Edge case
    if(left == arrSize-1){return 0;}

    // From right, spot the non-decreasing point
    while(right>left && arr[right]>=arr[right-1]){
        right--;
    }
    printf("Left %d, Right %d \n", left, right);

    // (condition) ? (value_if_true) : (value_if_false)
    int result = (arrSize - left + 1 < right) ? (arrSize-left+1) : right;
    // For all the remaining decreasing parts
    // Just need to scan till right since it is sincerely decreasing 
    for(int i=0, j = right; i <= left && j < arrSize;){
        if(arr[j] >= arr[i]){
            result = (result < j-i-1) ? result: j-i-1;
            i++;
        }
        else{
            j++;
        }

    }
    return result;
} 


// // For debugging - invalid
// int findLengthOfShortestSubarray(int* arr, int arrSize) {
//     int* output = (int*)malloc(sizeof(int) * arrSize);
//     if (output == NULL) {
//         printf("Memory allocation failed\n");
//         return -1; // Return -1 to indicate failure
//     }

//     output[0] = arr[0]; // Store the first element of arr in output
//     int n_sub = 1; // Initialize the number of elements in the subarray to 1
//     int tmp = 0;

//     for(int i = 0; i < arrSize; i++) {
//         printf("Current element: %d\n", arr[i]);
//         printf("Current output: ");
//         for (int j = 0; j < n_sub; j++) {
//             printf("%d ", output[j]);
//         }
//         printf("\n");

//         if (arr[i] > output[n_sub - 1] && arr[i] > tmp) {
//             output[n_sub] = arr[i];
//             tmp = arr[i];          
//             printf("Current tmp: %d\n", tmp);
//             n_sub++; // Increment the size of the subarray
//         }
//     }

//     // Calculate the length of the shortest subarray
//     int shortestSubarrayLength = arrSize - n_sub;
    
//     printf("Shortest subarray length: %d\n", shortestSubarrayLength);

//     free(output);
    
//     return shortestSubarrayLength;
// }

int main() {
    printf("Mock_Q2\n");
    printf("====================================\n");
    printf("[Case 1]\n");
    int arr[] = {1, 2, 3, 10, 4, 2, 3, 5};
    int arrSize1 = 8;
    int expected1 = 3;
    int res1 = findLengthOfShortestSubarray(arr, arrSize1);
    printf("Input   : s = \"%d\"\n", arr);
    printf("Output  : %d\n", res1);
    printf("Check   : %s\n", expected1==res1? "true":"false");
    printf("====================================\n");

    printf("[Case 2]\n");
    int arr2[] = {5, 4, 3, 2, 1};
    int arrSize2 = 5;
    int expected2 = 4;
    int res2 = findLengthOfShortestSubarray(arr2, arrSize2);
    printf("Input   : s = \"%s\"\n", arr2);
    printf("Output  : %d\n", res2);
    printf("Check   : %s\n", expected2==res2? "true":"false");
    printf("====================================\n");

    printf("[Case 3]\n");
    int arr3[] = {1, 2, 3};
    int arrSize3 = 3;
    int expected3 = 0;
    int res3 = findLengthOfShortestSubarray(arr3, arrSize3);
    printf("Input   : s = \"%s\"\n", arr3);
    printf("Output  : %d\n", res3);
    printf("Check   : %s\n", expected3==res3? "true":"false");
    printf("====================================\n");
}

// Result
// Mock_Q2
// ====================================
// [Case 1]
// Left 3, Right 5
// Input   : s = "6421968"
// Output  : 3
// Check   : true
// ====================================
// [Case 2]
// Left 0, Right 4
// Input   : s = ""
// Output  : 4
// Check   : true
// ====================================
// [Case 3]
// Input   : s = ""
// Output  : 0
// Check   : true
// ====================================

// int main() {
//     int arr[] = {1, 2, 3, 10, 4, 2, 3, 5};
//     int arrSize = sizeof(arr) / sizeof(arr[0]);
//     int shortestSubarrayLength = findLengthOfShortestSubarray(arr, arrSize);
//     printf("Length of shortest subarray: %d\n", shortestSubarrayLength);
//     return 0;
// }


// Python
// class Solution:
//     def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
//         s=0
//         e=len(arr)-1
//         n=len(arr)
//         while s<n-1 and arr[s]<=arr[s+1]:
//             s+=1
//         if s==n-1:
//             return 0
//         while e>=s and arr[e]>=arr[e-1]:
//             e-=1
//         if e==0:
//             return n-1
//         res=min(e,n-s-1)
//         i=0
//         j=e
//         while i<=s and j<n:
//             if arr[j]>=arr[i]:
//                 res=min(res,j-i-1)
//                 i+=1
//             else:
//                 j+=1
//         return res
        
        