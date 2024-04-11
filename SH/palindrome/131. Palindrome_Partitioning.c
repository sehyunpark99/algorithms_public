#include <string.h>
#include <vector.h>
#include <stdio.h>

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
}

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
// char*** partition(char* s, int* returnSize, int** returnColumnSizes) {
//     int *returnColumnSizes = (*int) malloc(sizeof(returnSize));
//     int *ans = (*int) malloc(sizeof(returnSize));
//     int n = strlen(s);

//     if(n==0){return ans;}
//     for(int i=1; i<=n+1; i++){
//         if(substring(s, 0, i) == substring())
//     }

// }



/*
Direct translation from GPT
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Define a structure to store partitions
struct Partition {
    char** partitions;
    int size;
};

// Utility function to check if a string is palindrome
int isPalindrome(char* str, int start, int end) {
    while (start < end) {
        if (str[start++] != str[end--]) {
            return 0; // Not a palindrome
        }
    }
    return 1; // Palindrome
}

// Utility function to create a new partition structure
struct Partition* createPartition(int capacity) {
    struct Partition* partition = (struct Partition*)malloc(sizeof(struct Partition));
    partition->partitions = (char**)malloc(capacity * sizeof(char*));
    partition->size = 0;
    return partition;
}

// Utility function to add a new partition
void addPartition(struct Partition* partition, char* str) {
    int length = strlen(str);
    partition->partitions[partition->size] = (char*)malloc((length + 1) * sizeof(char));
    strcpy(partition->partitions[partition->size], str);
    partition->size++;
}

// Utility function to free memory allocated for partitions
void freePartition(struct Partition* partition) {
    for (int i = 0; i < partition->size; i++) {
        free(partition->partitions[i]);
    }
    free(partition->partitions);
    free(partition);
}

// Recursive function to partition a string into palindromic substrings
void partitionHelper(char* s, int start, struct Partition* currentPartition, struct Partition* result) {
    int length = strlen(s);
    if (start == length) {
        // Add the current partition to the result
        struct Partition* copy = createPartition(currentPartition->size);
        for (int i = 0; i < currentPartition->size; i++) {
            addPartition(copy, currentPartition->partitions[i]);
        }
        addPartition(result, "");
        freePartition(copy);
        return;
    }
    for (int i = start + 1; i <= length; i++) {
        if (isPalindrome(s, start, i - 1)) {
            char* substring = (char*)malloc((i - start + 1) * sizeof(char));
            strncpy(substring, &s[start], i - start);
            substring[i - start] = '\0';
            addPartition(currentPartition, substring);
            partitionHelper(s, i, currentPartition, result);
            currentPartition->size--;
        }
    }
}

// Function to partition a string into palindromic substrings
struct Partition* partition(char* s) {
    int n = strlen(s);
    struct Partition* result = createPartition(1000); // Initial capacity
    if (n == 0) {
        addPartition(result, "");
        return result;
    }
    struct Partition* currentPartition = createPartition(n); // Initial capacity
    partitionHelper(s, 0, currentPartition, result);
    freePartition(currentPartition);
    return result;
}

// Function to print partitions
void printPartitions(struct Partition* partition) {
    for (int i = 0; i < partition->size; i++) {
        printf("[");
        printf("%s", partition->partitions[i]);
        printf("]");
        if (i < partition->size - 1) {
            printf(", ");
        }
    }
    printf("\n");
}

int main() {
    char s[] = "aab";
    struct Partition* result = partition(s);
    printf("[\n");
    for (int i = 0; i < result->size; i++) {
        printf("  ");
        printPartitions(result->partitions[i]);
    }
    printf("]\n");

    // Free memory
    freePartition(result);
    return 0;
}
*/