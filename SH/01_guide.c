#include <math.h>
#include <stdio.h>
#include <string.h>

char* s1;
char* s2;

// 길이
int strlen(s1);

// 복사, 슬라이싱 (destination, source)
void strcpy(s1, s2);
void strncpy(s1, s2, n);

// python
s1 = s2 [3:10];
// C
strncpy(s1, s2 + 3, 7);

// concat
void strcat(s1, s2);  // s1 = s1 + s2
void strncat(s1, s2, n);

// 뒤집기
void strrev(s1);  // 리턴 없이 s1이 뒤집힘

// index i인 문자 제거 -> for subsequence
void iErase(char* result, char* str, int i) {
    int len = strlen(str);
    if (i < 0 || i >= len) {
        strcpy(result, str);
        return;
    }
    strncpy(result, str, i);
    result[i] = '\0';
    strcat(result, str + i + 1);
};

// 비교 식, {-1, 0, 1} 리턴)
int strcmp(s1, s2);
int strncmp(s1, s2, n);

// 스트링(또는 문자) 찾기
char* strstr(s1, s2);  //(s1에서 s2를 찾아서 있으면 해당 포인터 반환)

/////////////////////////////////////////////////////////////////////////////////////////////////
// 길이 10인 string 에서 5개를 뽑아보자.
int fact(int n) {
    if (n == 1)
        return 1;
    else
        return n * fact(n - 1);
}
int n_combi(int n, int r) { return fact(n) / (fact(r) * fact(n - r)); };

int n = 10;
int r = 5;

int is_palin(char* s) {  // 0 no / 1 yes
    int slen = strlen(s);
    for (int i = 0; i < slen / 2; ++i) {
        if (s[i] != s[slen - 1 - i]) {
            return 0;
        }
    }
    return 1;
}

// a부터 끝까지 index의 string이 palindrome인지 아닌지 알려주는 함수
// is_n_palin(s+3, 5): 3번째 인덱스부터 크기 5까지의 string이 palindrome인지 아닌지 확인
int is_n_palin(char* s, int n) {  // 0 no / 1 yes
    for (int i = 0; i < n / 2; ++i) {
        if (s[i] != s[n - 1 - i]) {
            return 0;
        }
    }
    return 1;
}

int getLen(int i) {  // 이진수 i의 1 개수 리턴
    int count = 0;
    while (i) {
        count += i & 1;
        i >>= 1;
    }
    return count;
}

// i에 해당하는 string 뽑아내기
char* getString(char* in, char* out, int i, int len_out) {
    /*
    i: substring 번호
    len_out: 뽑은 이진수의 길이
    */
    int j = 0;
    int k = 0;
    int slen = strlen(in);
    while (i) {
        if (i & 1) {
            out[len_out - j - 1] = in[slen - k - 1];
            ++j;
        }
        i >>= 1;
        ++k;
    }
    out[len_out] = '\0';
};

int main() {
    char s[10] = "abcesdffg";
    char s2[10];
    int n = 3;

    int i = getLen(n);
    printf("%d\n", i);

    getString(s, s2, n, i);
    printf("%s\n", s2);

    return 0;
}

