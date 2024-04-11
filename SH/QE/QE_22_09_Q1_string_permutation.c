#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void swap(char *a, char *b) {
    if (a != NULL && b != NULL) {
        char temp = *a;
        *a = *b;
        *b = temp;
    } else {
        printf("Error: Invalid pointers for swap\n");
    }
}


void permute(char *s, int left, int right, char **result, int *count) {
    if (left == right) {
        result[*count] = (char *)malloc((strlen(s) + 1) * sizeof(char));
        if (result[*count] == NULL) {
            printf("Memory allocation failed\n");
            exit(1);
        }
        strcpy(result[*count], s);
        (*count)++;
    } else {
        for (int i = left; i <= right; i++) {
            swap(&s[left], &s[i]);
            permute(s, left + 1, right, result, count);
            swap(&s[left], &s[i]); // Backtrack: undo the swap
        }
    }
}

char **generate_permutations(const char *s, int *num_permutations) {
    int n = strlen(s);
    char **result = (char **)malloc(10000 * sizeof(char *)); // Allocate space for 10000 pointers
    if (result == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    *num_permutations = 0;
    permute((char *)s, 0, n - 1, result, num_permutations);
    return result;
}

void free_permutations(char **permutations, int num_permutations) {
    for (int i = 0; i < num_permutations; i++) {
        free(permutations[i]);
    }
    free(permutations);
}

int main() {
    const char *input_str = "ABC";
    int num_permutations;
    char **permutations = generate_permutations(input_str, &num_permutations);

    printf("Permutations of '%s':\n", input_str);
    for (int i = 0; i < num_permutations; i++) {
        printf("%s\n", permutations[i]);
    }

    // Free allocated memory
    free_permutations(permutations, num_permutations);

    return 0;
}

/*
string 주어지면 그에 대한 permutation을 오름차순(alphabetical order)으로 반환하는 문제

ex)
s = "abc"
str_perm(s) -> ['abc', 'abc', 'bac'...]

s = "abb"
str_perm(s) -> ['abb', 'bab', 'bba']
*/

// #include <stdio.h> 
// #include <string.h> 
  
// /* Function to swap values at 
//    two pointers */
// void swap(char *x, char *y) 
// { 
//     char temp; 
//     temp = *x; 
//     *x = *y; 
//     *y = temp; 
// } 
  
// /* Function to print permutations 
//    of string 
//    This function takes three parameters: 
//    1. String 
//    2. Starting index of the string 
//    3. Ending index of the string. */

// //중복값 제거는 따로 안되지만..일단 붙여둠 [abb,abb,bab,bab] 이런식으로 여러개 나옴
// void permute(char *a, int l, int r) 
// { 
//     int i; 
//     if (l == r) 
//         printf("%s\n", a); 
//     else
//     { 
//         for (i = l; i <= r; i++) 
//         { 
//             swap((a + l), (a + i)); 
//             permute(a, l + 1, r);  //l+1에서 다시 swap(=permute) 시작
  
//             //backtrack 
//             swap((a + l), (a + i)); 
//         } 
//     } 
// } 
  
// // Driver code
// int main() 
// { 
//     char str[] = "abb"; 
//     int n = strlen(str); 
//     permute(str, 0, n-1); 
//     return 0; 
// } 

