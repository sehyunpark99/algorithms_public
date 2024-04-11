#include <string.h>

void reverse(char *w){
    int l = 0;
    int r = strlen(w)-1;
    while( l < r ){
        w[l] ^= w[r]; // Bitwise XOR
        w[r] ^= w[l];
        w[l++] ^= w[r--];
    }
}
char * reverseWords(char * s){
    int size = strlen(s);

    char temp[50] = "";
    int temp_size = 0;
    char res[10001] = "";
    int res_size = 0;
    for(int i = size-1; i >= 0; i--){
        // First storing all the possible characters
        if ( s[i] != ' ' ){
            temp[temp_size++] = s[i];
            temp[temp_size] = '\0';
        }
        // If it reaches the end, or if one of them are whitespace
        if ( (s[i] == ' ' && i != size-1 && s[i+1] != ' ') || (s[i] != ' ' && i == 0) ){
            reverse(temp);
            
            // Concatenating with space 
            strcat(res, temp);
            strcat(res, " ");
            
            res_size += temp_size + 1; 
            
            temp_size = 0;
        }
    }
    res[res_size-1] = '\0'; // whitespace
    // copy the contents of res into string s
    strcpy(s, res);
    return s;
}

// Version 2
 string reverseWords(string s) {
        //Removing all extra spaces
        for(int i=1;i<s.length();i++){
            if(s[i]==s[i-1]&&s[i]==' '){
                s.erase(s.begin()+i-1);
                i--;
            }
        }
        //removing the space in first pos
        if(s[0]==' ')
            s.erase(s.begin());
        
        int n=s.length();
        //removing the space of last pos
        if(s[n-1]==' '){
             s.erase(s.begin()+n-1);
            n--;
        }
        
        //Reverseing the whole string
        for(int i=0;i<n/2;i++){
           swap(s[i],s[n-i-1]);
        }
        
        //finding words and reversing them
        //if if it not last word than word will end in ' '(space)
        //st-> starting position of the word
        int st=0;
        for(int i=0;i<n;i++){
            if(s[i]==' '){
                //we have found a word starting from st and ending in i-1
                //reveresing each word
                for(int j=i-1;j>st;j--){
                    swap(s[j],s[st]);
                    st++;
                }
                //updating st to the start pos of next word 
                st=i+1;
            }
        }
        //reversing the last word as it will not have space in the end
        //we need to reverse it separately
        for(int j=n-1;j>st;j--){
            swap(s[j],s[st]);
            st++;
        }
        
        return s;
    }

// Version 3
class Solution {
public:
    string reverseWords(string s) {
        stringstream ss(s);
        string word;
        
        stack<string> st;
        while(ss >> word) {
            st.push(word);
        }
        
        string ans = "";
        while(!st.empty()) {
            ans += st.top() + " ";
            st.pop();
        }
        ans.pop_back(); // removes the trailing whitespace (1 character)
        
        return ans;
    }
};


/* For C++
#include <sstream>

char* reverseWords(char* s) {
    stringstream ss(s);
    string word;
    stack<string> st;
    while(ss>>word){
        std
    }
    int i = 0;
    char *iter = strtok(s, " ");
    while(iter){
        arr[i] = token;
        i++;
        iter = strtok(NULL, " ");
    }
    for(int j=strlen(s)-1;j>=0;j--){
        printf(arr[j]);
    }
    return 0;
}

// AddressError
char* reverseWords(char* s) {
    int arr[strlen(s)];
    int i = 0;
    char *iter = strtok(s, " ");
    while(iter){
        arr[i] = iter;
        i++;
        iter = strtok(NULL, " ");
    }
    for(int j=strlen(s)-1;j>=0;j--){
        printf(arr[j]);
    }
    return 0;
}
*/

/*
// To check whether the string is a Palindrome or not
#include <stdio.h>  
#include <string.h>  
int main ()  
{     
    // declare variables  
    char str1[30];  
    int i, len, flag = 0;  
      
    printf (" Enter a string: ");  
    scanf ("%s", str1);  
    len = strlen( str1 ); // get the string length  
      
      
    for ( i = 0; i < len; i++)  
    {     
        // str1[i] is not equal to str1[len-i-1]  
        if (str1[i] != str1[len - i - 1])  
        {  
            flag = 1;   
            break; // exit from if statement  
        }  
    }  
    if (flag)  
    {  
        printf (" %s is not a palindrome string", str1);  
    }  
    else  
    {  
        printf (" %s is a palindrome", str1);  
    }  
    return 0;  
}  
*/