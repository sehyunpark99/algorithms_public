#include <stdlib.h>
#include <limits.h>

struct Node {
    int dest;
    int price;
    struct Node* next;
};

struct Graph {
    int V;
    struct Node** adjList;
};

struct Node* createNode(int dest, int price) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->dest = dest;
    newNode->price = price;
    newNode->next = NULL;
    return newNode;
}

struct Graph* createGraph(int V) {
    struct Graph* graph = (struct Graph*)malloc(sizeof(struct Graph));
    graph->V = V;
    graph->adjList = (struct Node**)malloc(V * sizeof(struct Node*));
    for (int i = 0; i < V; ++i)
        graph->adjList[i] = NULL;
    return graph;
}

void addEdge(struct Graph* graph, int src, int dest, int price) {
    struct Node* newNode = createNode(dest, price);
    newNode->next = graph->adjList[src];
    graph->adjList[src] = newNode;
}

int findCheapestPrice(int n, int** flights, int flightsSize, int* flightsColSize, int src, int dst, int k) {
    struct Graph* graph = createGraph(n);
    int* visited = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; ++i)
        visited[i] = INT_MAX;
    visited[src] = 0;
    
    for (int i = 0; i < flightsSize; ++i)
        addEdge(graph, flights[i][0], flights[i][1], flights[i][2]);
    
    struct Node* queue = createNode(src, 0);
    k++;
    
    while (queue && k--) {
        int count = 0;
        struct Node* tempQueue = createNode(-1, -1);
        while (queue) {
            struct Node* curr = queue;
            queue = queue->next;
            int currNode = curr->dest;
            int currPrice = curr->price;
            struct Node* adjNode = graph->adjList[currNode];
            while (adjNode) {
                int newPrice = currPrice + adjNode->price;
                if (newPrice < visited[adjNode->dest]) {
                    visited[adjNode->dest] = newPrice;
                    struct Node* newNode = createNode(adjNode->dest, newPrice);
                    newNode->next = tempQueue->next;
                    tempQueue->next = newNode;
                }
                adjNode = adjNode->next;
            }
            free(curr);
            count++;
        }
        free(queue);
        queue = tempQueue->next;
    }
    
    return visited[dst] == INT_MAX ? -1 : visited[dst];
}