#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_LEN 1000


bool is_palindrome(char *s){
    int n = strlen(s);

    for(int i=0;i<n/2;i++){
        if(s[i] != s[n-i-1]){
            return false;
        }
    }
    return true;
}


int main() {
    printf("Palindrome\n");
    printf("====================================\n");
    printf("[Case 1]\n");
    char s1[] = "zzazz";
    int expected1 = 1;
    int res1 = is_palindrome(s1);
    printf("Input   : s = \"%s\"\n", s1);
    printf("Output  : %d\n", res1);
    printf("Check   : %s\n", expected1==res1? "true":"false");
    printf("====================================\n");

    printf("[Case 2]\n");
    char s2[] = "mbadm";
    int expected2 = 0;
    int res2 = is_palindrome(s2);
    printf("Input   : s = \"%s\"\n", s2);
    printf("Output  : %d\n", res2);
    printf("Check   : %s\n", expected2==res2? "true":"false");
    printf("====================================\n");

    printf("[Case 3]\n");
    char s3[] = "leetcode";
    int expected3 = 0;
    int res3 = is_palindrome(s3);
    printf("Input   : s = \"%s\"\n", s3);
    printf("Output  : %d\n", res3);
    printf("Check   : %s\n", expected3==res3? "true":"false");
    printf("====================================\n");
}

/*
BJ version
#include <string.h>
#include <stdbool.h>

int main() {

  char s[101];
	scanf("%s", s);
    
  int n = strlen(s);
  for(int i = 0; i <= n / 2; i++) {
    if(s[i] != s[n - i - 1]) {
      printf("0");
      return 0;
    }
  }

  printf("1");

  return 0;
}
*/