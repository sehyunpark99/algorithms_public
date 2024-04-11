#include <vector>
#include <iostream>
using namespace std;

// cpp -> should use '' for strings
// OOP
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()) return 0;
        int row = grid.size();
        int col = grid[0].size();
        int ans = 0;
        for(int i=0; i<row; ++i){
            for(int j=0; j<col; ++j){
                if(grid[i][j] == '1'){
                    dfs(grid, i, j);
                    ++ans;
                }
            }
        }
        return ans;
    }
private:
    void dfs(vector<vector<char>>& grid, int i, int j){
        int row = grid.size();
        int col = grid[0].size();
        if(i>=0 && i<row && j>=0 && j<col && grid[i][j] == '1'){
            grid[i][j] = '0'; // make it invalid
            dfs(grid, i+1, j);
            dfs(grid, i, j+1);
            dfs(grid, i-1, j);
            dfs(grid, i, j-1);
        }
    }
};



int main() {
    cout << "200. Number of Islands.cpp\n";

    Solution solution;
    cout << "\nCase 1\n";

    vector<vector<char>> grid1 = {
        {'1', '1', '1', '1', '0'},
        {'1', '1', '0', '1', '0'},
        {'1', '1', '0', '0', '0'},
        {'0', '0', '0', '0', '0'}
    };

    int res1 = solution.numIslands(grid1);
    int ans1 = 1;
    cout << res1 << "\n  ==> check: " << (res1 == ans1) << "\n";

    cout << "\nCase 2\n";
    vector<vector<char>> grid2 = {
        {'1', '1', '0', '0', '0'},
        {'1', '1', '0', '0', '0'},
        {'0', '0', '1', '0', '0'},
        {'0', '0', '0', '1', '1'}
    };

    int res2 = solution.numIslands(grid2);
    int ans2 = 3;
    cout << res2 << "\n  ==> check: " << (res2 == ans2) << "\n";

    return 0;
}
