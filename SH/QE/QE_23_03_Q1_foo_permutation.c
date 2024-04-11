#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void dfs(const char *sub, char *cur, char **res, int *res_size, int length) {
    if (strlen(cur) == length) {
        strcpy(res[(*res_size)++], cur);
        return;
    }
    for (int i = 0; i < strlen(sub); i++) {
        char *new_str = (char *)malloc((strlen(cur) + 2) * sizeof(char));
        strcpy(new_str, cur);
        new_str[strlen(cur)] = sub[i];
        new_str[strlen(cur) + 1] = '\0';
        if (strlen(new_str) == 1 || abs((int)sub[i] - (int)new_str[strlen(new_str) - 1]) > 1) {
            char *sub_copy = strdup(sub + i + 1);
            dfs(sub_copy, new_str, res, res_size, length);
            free(sub_copy);
        }
        free(new_str);
    }
}

char *foo(const char *s, char **res, int *res_size) {
    printf("Inside foo with input: %s\n", s); 
    int length = strlen(s);
    dfs(s, "", res, res_size, length);
    if (*res_size == 0) {
        res[0][0] = '\0';
    }
    return res[*res_size - 1];
}

char *bar(const char *s, char **res, int *res_size) {
    int length = strlen(s);
    char *unique_s = (char *)malloc((length + 1) * sizeof(char));
    strcpy(unique_s, s);
    
    for (int i = 0; i < length; i++) {
        for (int j = i + 1; j < length; j++) {
            if (unique_s[i] == unique_s[j]) {
                unique_s[j] = ' ';
            }
        }
    }
    dfs(unique_s, "", res, res_size, length);
    free(unique_s);
    if (*res_size == 0) {
        res[0][0] = '\0';
    }
    return res[*res_size - 1];
}

int main() {
    const char *input[] = {"abcde", "abc", "", "abccde", "abcdcef"};

    char **res_a = (char **)malloc(100 * sizeof(char *));
    int res_size_a = 0;
    printf("Q1_a\n");
    for (int i = 0; i < sizeof(input) / sizeof(input[0]); i++) {
        const char *result = foo(input[i], res_a, &res_size_a);
        printf("  input: %s | output: %s\n", input[i], result);
    }

    char **res_b = (char **)malloc(100 * sizeof(char *));
    int res_size_b = 0;
    printf("\nQ1_b\n");
    for (int i = 0; i < sizeof(input) / sizeof(input[0]); i++) {
        const char *result = bar(input[i], res_b, &res_size_b);
        printf("  input: %s | output: %s\n", input[i], result);
    }

    for (int i = 0; i < res_size_a; i++) {
        free(res_a[i]);
    }
    free(res_a);
    
    for (int i = 0; i < res_size_b; i++) {
        free(res_b[i]);
    }
    free(res_b);

    return 0;
}
