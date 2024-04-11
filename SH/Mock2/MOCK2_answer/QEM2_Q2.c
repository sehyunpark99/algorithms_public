/*
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.
Return the length of the shortest subarray to remove.
A subarray is a contiguous subsequence of the array.

Constraints:
-	1 <= arr.length <= 10^5
-	0 <= arr[i] <= 10^9


Example 1
-	Input	: arr []= {1,2,3,10,4,2,3,5}
-	Output	: 3 
-	Explanation: [10,4,2] or [3,10,4] should be removed
Example 2
-	Input	: arr[] = {5,4,3,2,1}
-	Output	: 4
Example 3
-	Input 	: arr[] = {1,2,3}
-	Output	: 0

Requirements:
-	Use `scanf` to get the input array.
-	Use `printf` to print the results.
-	The entire program should work correctly with the provided `main` function.

*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Q1 printArray
void printArray(int* arr, int arrSize){
    printf("arr[] = {");
    for (int i = 0; i < arrSize; i++) {
        if (i < arrSize-1){
            printf("%d, ", arr[i]);
        }
        else {
            printf("%d}\n", arr[i]);
        }
    }
}

// Q2 findLengthOfShortestSubarray
// int findLengthOfShortestSubarray(int* arr, int arrSize) {
//     int left = 0;
//     int right = arrSize - 1;
    
//     // 왼쪽에서 시작하여 감소하지 않는 부분을 찾음
//     while (left + 1 < arrSize && arr[left] <= arr[left + 1]) {
//         left++;
//     }
//     if (left == arrSize - 1) return 0; // 전체 배열이 이미 비감소하면 0 반환
    
//     // 오른쪽에서 시작하여 감소하지 않는 부분을 찾음
//     while (right > left && arr[right - 1] <= arr[right]) {
//         right--;
//     }
    
//     // 최소로 삭제해야 하는 부분 배열의 길이를 계산
//     int result = (arrSize - left - 1 < right) ? arrSize - left - 1 : right;
//     for (int i = 0, j = right; i <= left && j < arrSize;) {
//         if (arr[j] >= arr[i]) {
//             result = (result < j - i - 1) ? result : j - i - 1;
//             i++;
//         } 
//         else {
//             j++;
//         }
//     }
//     return result;
// }

// FOR JP only - get_array_size
int get_array_size(int* arr){
    int cnt = 0;
    while (arr[cnt] != '\0'){
        cnt++;
    }
    return cnt;
}

#include<stdio.h>

int find_shortest(int *arr, int size)
{
    for(int i=size-1;i>=0;i--){
        if(arr[i]>arr[i+1]){
            arr[i]=arr[i+1];
        }
    }
    int min = 0,max = 0;
    for(int i=size-2;i>=0;i--){
        if(arr[i]>arr[i+1]){
            min = i+1;
            break;
        }else {
            max = i+1;
        }
    }
    return max-min+1;
}

int main() {
    printf("[C] 1574. Find the length of the shortest subarray to remove\n");
    int cnt = 0;
    while(true){
        cnt++;
        printf("\n[%d] trial\n", cnt);

        // Get the input array
        int n;
        printf("  arrSize = ");
        scanf("%d", &n);

        int* arr = (int*)malloc( (n+1) * sizeof(int));
        for (int i = 0; i < n; i++) {
            printf("  arr[%d] = ", i);
            scanf("%d", &arr[i]);
        }
        arr[n] = '\0';

        // Print the input array(Q1 printArray)
        printf("  Input is...\n");
        printf("    arrSize = %d\n", n);
        printf("    "), printArray(arr, n);

        // Call the target function (Q2 findLengthOfShortestSubarray)
        int shortestSubarrayLength = findLengthOfShortestSubarray(arr, n);
        printf("\n=> Answer: %d\n", findLengthOfShortestSubarray(arr, n));
        printf("\n=> Answer: %d\n", find_shortest(arr, n));
        free(arr);
    }
    return 0;
}