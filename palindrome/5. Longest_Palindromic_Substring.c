class Solution {
public:
    int dp[1000][1000];
    int f(int l, int r, string &s) {
        if(l == r) return 1;
        if(l > r) return 0;
        if(dp[l][r] != -1) return dp[l][r];
        return dp[l][r] = s[l] == s[r] ? 2 + f(l+1, r-1, s) : max(f(l+1, r, s),f(l, r-1, s));  
    }
        int longestPalindromeSubseq(string s) { 
        memset(dp, -1, sizeof(dp));
        return f(0, s.size()-1, s); 
    }
};

// DP
class Solution {
	public:
   	string longestPalindrome(string s) {   
	    int n = s.size();
    	int dp[n][n];
    	
	    memset(dp,0,sizeof(dp));
    	int end=1;
    	int strt=0;
	
	    for(int i=0;i<n;i++){
	        dp[i][i] = 1;
    	}
	    for(int i=0;i<n-1;i++){
	        if(s[i]==s[i+1]){
    	    	dp[i][i+1]=1;
        		strt=i;end=2;
       		}
	    }
    	for(int j=2;j<n;j++){
	        for(int i=0;i< n-j;i++){  
           		int lft=i;
            	int rght = i+j;
        	    
    	        if(dp[lft+1][rght-1]==1 && s[lft]==s[rght]) 
	            {
                	dp[lft][rght]=1; strt=i; end=j+1; 
            	}        
        	}
    	}
    return s.substr(strt, end);
	}
};


// Brute Force
string longestPalindrome(string s) {

        int n=s.size();
        int res=1, start=0;
        string ans;
        
        for(int i=0; i<n; i++)
        {
            int l=i-1;
            int r=i+1;
            
            while(l>=0 && s[i]==s[l])
            {
                l--;
            }
            while(r<n && s[i]==s[r])
            {
                r++;
            }
            while(l>=0 && r<n && s[l]==s[r])
            {
                l--;
                r++;
            }
            int length=(r-1)-(l+1)+1;  
            if(length>res)
            {
                res=length;
                start=l+1;
            }
        }
        ans=s.substr(start,res);
        return ans;
}

