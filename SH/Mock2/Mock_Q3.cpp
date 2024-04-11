#include <vector>
#include <iostream>
#include <string>
#include <bits/stdc++.h>
using namespace std;

class GNode {
    /*
    * colors spec
    * W: not visited
    * G: visited but its neighbors are not visited 
    * B: visited and all the neighbors are visited
    */
public:
    int id;
    string color;
    vector<GNode*> neighbors;
    GNode* parent;

    GNode(int id, string color = "W", GNode* parent = nullptr) : id(id), color(color), parent(parent) {}

    void addNeighbor(GNode* neighbor) {
        neighbors.push_back(neighbor);
    }
};


void dfs(GNode* node, GNode* parent = nullptr) {
    node->color = "G"; // 방문 시작 (Gray)
    node->parent = parent; // 부모 노드 설정

    for (size_t i = 0; i < node->neighbors.size(); ++i) {
        GNode* neighbor = node->neighbors[i];
        if (neighbor->color == "W") { // 방문하지 않은 이웃
            dfs(neighbor, node); // 현재 노드를 부모로 설정하여 dfs 호출
        }
    }    
    node->color = "B"; // 방문 완료 (Black)
}

int countComponents(int n, vector<vector<int>>& edges){
    vector<GNode*> adj_list;

    // Initialize Node
    for (int i = 0; i < n; ++i) {
        adj_list.push_back(new GNode(i));
    }
    // Construct adjacency list
    // using auto
    // for(auto edge:edges){
    //     auto edge1 = edge[0];
    //     auto edge2 = edge[1];
    //     adj_list[edge2].push_back(edge1);
    // }
    int n_edge = edges.size();
    // Simple
    for (int i = 0; i<n_edge; i++){
        adj_list[edges[i][0]]->addNeighbor(adj_list[edges[i][1]]);
        adj_list[edges[i][1]]->addNeighbor(adj_list[edges[i][0]]);
    }

    int count = 0;
    // Should go over all the adj_list
    for(int i=0; i<adj_list.size(); i++){
        if(adj_list[i]->color == "W"){
            dfs(adj_list[i]);
            count++;
        }
    }
    
    // Clear Memory
    for (size_t i = 0; i < adj_list.size(); ++i) {
        delete adj_list[i];
    }

    return count;
}



int main() {
    printf("[CPP] 323. Number of Connected Components in an Undirected Graph\n");

    // using printf
    printf("\nCase 1");
    {
        int n = 5;
        vector<vector<int>> edges = {{0, 1}, {1, 2}, {3, 4}};
        int ans = 2;
        int res = countComponents(5, edges);
        printf("\nResult    : %d", res);
        printf("\nAnwser    : %d", ans);
        printf("\n-> CHECK  : %s", ans == res ? "PASSED" : "FAILED");
        printf("\n");
    }

    // using cout
    cout << "\nCase 2" << endl;
    {
        int n = 5;
        vector<vector<int>> edges = {{0, 1}, {1, 2}, {2, 3}, {3, 4}};
        int ans = 1;
        int res = countComponents(5, edges);
        cout << "Result    : " << res << endl;
        cout << "Anwser    : " << ans << endl;
        cout << "-> CHECK  : " << (ans == res ? "PASSED" : "FAILED") << endl;
    }
    return 0;
}