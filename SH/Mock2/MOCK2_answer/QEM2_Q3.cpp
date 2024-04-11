/*
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [a_i\ ,\ b_i] indicates that there is an edge between a_i\ and b_i\  in the graph.
Return the number of connected components in the graph.

Constraints:
	1 <= n <= 2000
	1 <= edges.length <= 5000
	edges[i].length == 2
	0 <= ai <= bi < n
	ai != bi
	There are no repeated edges.

Example 1
	Input	: n = 5, vector<vector<int>> edges1 = {{0, 1}, {1, 2}, {3, 4}}
	Output	: 2
Example 2
	Input	: n = 5, vector<vector<int>> edges1 = {{0, 1}, {1, 2}, {2, 3}, {3, 4}};
	Output	: 1
*/
#include <iostream>
#include <vector>
#include <string>

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

int countComponents(int n, const vector<vector<int>>& edges) {
    vector<GNode*> nodes;

    // 노드 초기화
    for (int i = 0; i < n; ++i) {
        nodes.push_back(new GNode(i));
    }

    // 에지로부터 그래프 구성
    for (size_t i = 0; i < edges.size(); ++i) {
        nodes[edges[i][0]]->addNeighbor(nodes[edges[i][1]]);
        nodes[edges[i][1]]->addNeighbor(nodes[edges[i][0]]);
    }

    int connectedComponents = 0;
    for (size_t i = 0; i < nodes.size(); ++i) {
        if (nodes[i]->color == "W") { // 방문하지 않은 노드
            dfs(nodes[i]);
            ++connectedComponents; // 새로운 연결 요소 발견
        }
    }

    // 메모리 정리
    for (size_t i = 0; i < nodes.size(); ++i) {
        delete nodes[i];
    }

    return connectedComponents;
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