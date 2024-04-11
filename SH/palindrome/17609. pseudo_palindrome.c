/*
회문(回文) 또는 팰린드롬(palindrome)은 앞 뒤 방향으로 볼 때 같은 순서의 문자로 구성된 문자열을 말한다. 예를 들어 ‘abba’ ‘kayak’, ‘reviver’, ‘madam’은 모두 회문이다. 만일 그 자체는 회문이 아니지만 한 문자를 삭제하여 회문으로 만들 수 있는 문자열이라면 우리는 이런 문자열을 “유사회문”(pseudo palindrome)이라고 부른다. 예를 들어 ‘summuus’는 5번째나 혹은 6번째 문자 ‘u’를 제거하여 ‘summus’인 회문이 되므로 유사회문이다.

여러분은 제시된 문자열을 분석하여 그것이 그 자체로 회문인지, 또는 한 문자를 삭제하면 회문이 되는 “유사회문”인지, 아니면 회문이나 유사회문도 아닌 일반 문자열인지를 판단해야 한다. 만일 문자열 그 자체로 회문이면 0, 유사회문이면 1, 그 외는 2를 출력해야 한다. 
*/



#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_LEN 1000

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

int min_Insertions(char *s){
    int n = strlen(s);
    int dp[n][n];
    memset(dp, 0, sizeof(dp)); // To avoid random numbers

    for(int i=n-1;i>=0;i--){
        dp[i][i] = 1; // set diagonal as 1
        for(int j=i+1;j<n;j++){
            if(s[i]==s[j]){ // towards right diagonal
                dp[i][j] == 2 + dp[i+1][j-1]; // diagonal element
            }
            else{
                dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
            }
        }
    }
    printDP(n, dp);
    return n - dp[0][n-1];
}


int function(char *s){
    int n = strlen(s);
    int min_ins = min_Insertions(s);
    if(strlen(s)%2==1){
        if(is_palindrome(s)==1){
            return 0; // palindrome itself
        }
        if(min_ins==1){return 1;}
        else{return 2;}
    }
    else{
        if(min_ins==1){return 1;}
        else{return 2;}
    }
}


int main() {
    printf("Palindrome\n");
    printf("====================================\n");
    printf("[Case 1]\n");
    char s1[] = "7";
    int expected1 = 0;
    int res1 = function(s1);
    printf("Input   : s = \"%s\"\n", s1);
    printf("Output  : %d\n", res1);
    printf("Check   : %s\n", expected1==res1? "true":"false");
    printf("====================================\n");

    printf("[Case 2]\n");
    char s2[] = "abba";
    int expected2 = 1;
    int res2 = function(s2);
    printf("Input   : s = \"%s\"\n", s2);
    printf("Output  : %d\n", res2);
    printf("Check   : %s\n", expected2==res2? "true":"false");
    printf("====================================\n");

    printf("[Case 3]\n");
    char s3[] = "summuus";
    int expected3 = 1;
    int res3 = function(s3);
    printf("Input   : s = \"%s\"\n", s3);
    printf("Output  : %d\n", res3);
    printf("Check   : %s\n", expected3==res3? "true":"false");
    printf("====================================\n");

    printf("[Case 4]\n");
    char s4[] = "comcom";
    int expected4 = 2;
    int res4 = function(s4);
    // int min_ins4 = min_Insertions(s4);
    printf("Input   : s = \"%s\"\n", s4);
    printf("Output  : %d\n", res4);
    printf("Min_Insertion  : %d\n", min_ins4);
    printf("Check   : %s\n", expected4==res4? "true":"false");
    printf("====================================\n");
}

/*
#include <iostream>
#include <string>
using namespace std;

string s;
int l = 0;
int r;
int flag = 0;
int tmp_l, tmp_r;

int check(int l, int r) {
    flag = 0;
    while (l < r) {
        if (s[l] == s[r]) {
            l++;
            r--;
            continue;
        }
        else {
            if(flag == 0 && s[l+1] == s[r]){
                tmp_l = l;
                tmp_r = r;
                l++;
                flag = 3;
                continue;
            }
            else if(flag == 0 && s[l] == s[r-1]){
                r--;
                flag = 1;
                continue;
            }
            else{
                if(flag == 3){
                    l=tmp_l;
                    r = tmp_r-1;
                    flag=1;
                }
                else{
                    flag = 2;
                    break;
                }
            }
        }
    }
    if(flag == 1 || flag == 3){
        return 1;
    }
    else if(flag == 2){
        return 2;
    }
    return 0;
}

int main() {
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> s;
        cout << check(0, s.size()-1) << endl;
        
    }
}*/