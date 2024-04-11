#include <stdio.h>
#include <stdlib.h>

// doubly linked list
typedef struct LLNode {
    int val;
    struct LLNode *prv, *nxt;
} LLNode;

void print_linked_list(LLNode *head) {
    LLNode *cur = head;
    while (cur != NULL) {
        printf("%d ", cur->val);
        cur = cur->nxt;
    }
    printf("\n");
}

LLNode *go_tail(LLNode *head) {
    LLNode *curNode = head;
    while (curNode->nxt != NULL) {
        curNode = curNode->nxt;
    }
    return curNode;
}

LLNode *findMax(LLNode *head) {
    LLNode *curNode = head;
    LLNode *maxNode = head;
    int min = head->val;
    while (curNode->nxt != NULL) {
        if (curNode->val < min) {
            maxNode = curNode;
            min = curNode->val;
        }
        curNode = curNode->nxt;
    }
    if (curNode->val < min) {
        maxNode = curNode;
        min = curNode->val;
    }
    return maxNode;
}

LLNode *findMin(LLNode *head) {
    LLNode *curNode = head;
    LLNode *maxNode = head;
    int min = head->val;
    while (curNode->nxt != NULL) {
        if (curNode->val > min) {
            maxNode = curNode;
            min = curNode->val;
        }
        curNode = curNode->nxt;
    }
    if (curNode->val > min) {
        maxNode = curNode;
        min = curNode->val;
    }
    return maxNode;
}

LLNode *swapValue(LLNode *n1, LLNode *n2) {
    int temp;
    temp = n1->val;
    n1->val = n2->val;
    n2->val = temp;
}

void sort_list(LLNode *head) {
    LLNode *tail = go_tail(head);
    LLNode *new_head;
    LLNode *curNode = head;
    LLNode *maxNode = head;
    LLNode *temp;
    int max = head->val;

    maxNode = findMax(curNode);
    swapValue(curNode, maxNode);
    new_head = maxNode;
    curNode = curNode->nxt;

    while (curNode != tail) {
        maxNode = findMax(curNode);
        swapValue(curNode, maxNode);
        curNode = curNode->nxt;
    }
}

void sort_list_desc(LLNode *head) {
    LLNode *tail = go_tail(head);
    LLNode *new_head;
    LLNode *curNode = head;
    LLNode *maxNode = head;
    LLNode *temp;
    int max = head->val;

    maxNode = findMin(curNode);
    swapValue(curNode, maxNode);
    new_head = maxNode;
    curNode = curNode->nxt;

    while (curNode != tail) {
        maxNode = findMin(curNode);
        swapValue(curNode, maxNode);
        curNode = curNode->nxt;
    }
}

void sort_each_list(LLNode *head[100], int N) {
    for (int i = 0; i < N; ++i) {
        sort_list(head[i]);
    }
    sort_list(head[0]);
}

LLNode *merge_sorted_lists(LLNode *head[100], int N) {
    LLNode *tail;
    for (int i = 0; i < N - 1; ++i) {
        tail = go_tail(head[i]);
        tail->nxt = head[i + 1];
        head[i + 1]->prv = tail;
    }
    sort_list_desc(head[0]);
    return head[0];
}

int main() {
    // Linked list 3 -> 1 -> 5
    LLNode *node11 = (LLNode *)malloc(sizeof(LLNode));
    LLNode *node12 = (LLNode *)malloc(sizeof(LLNode));
    LLNode *node13 = (LLNode *)malloc(sizeof(LLNode));
    node11->val = 3, node11->nxt = node12, node11->prv = NULL;
    node12->val = 1, node12->nxt = node13, node12->prv = node11;
    node13->val = 5, node13->nxt = NULL, node13->prv = node12;
    LLNode *list1 = node11;

    // Linked list 2 8 6 1 1
    LLNode *node21 = (LLNode *)malloc(sizeof(LLNode));
    LLNode *node22 = (LLNode *)malloc(sizeof(LLNode));
    LLNode *node23 = (LLNode *)malloc(sizeof(LLNode));
    LLNode *node24 = (LLNode *)malloc(sizeof(LLNode));
    LLNode *node25 = (LLNode *)malloc(sizeof(LLNode));
    node21->val = 2, node21->nxt = node22, node21->prv = NULL;
    node22->val = 8, node22->nxt = node23, node22->prv = node21;
    node23->val = 6, node23->nxt = node24, node23->prv = node22;
    node24->val = 1, node24->nxt = node25, node24->prv = node23;
    node25->val = 1, node25->nxt = NULL, node25->prv = node24;
    LLNode *list2 = node21;

    // Linked list 7 2 7 4
    LLNode *node31 = (LLNode *)malloc(sizeof(LLNode));
    LLNode *node32 = (LLNode *)malloc(sizeof(LLNode));
    LLNode *node33 = (LLNode *)malloc(sizeof(LLNode));
    LLNode *node34 = (LLNode *)malloc(sizeof(LLNode));
    node31->val = 7, node31->nxt = node32, node31->prv = NULL;
    node32->val = 2, node32->nxt = node33, node32->prv = node31;
    node33->val = 7, node33->nxt = node34, node33->prv = node32;
    node34->val = 4, node34->nxt = NULL, node34->prv = node33;
    LLNode *list3 = node31;

    print_linked_list(list1);
    print_linked_list(list2);
    print_linked_list(list3);

    sort_list(list1);
    print_linked_list(list1);

    LLNode *lists[100];
    lists[0] = list1;
    lists[1] = list2;
    lists[2] = list3;
    sort_each_list(lists, 3);
    print_linked_list(list1);
    print_linked_list(list2);
    print_linked_list(list3);

    LLNode *merged = merge_sorted_lists(lists, 3);
    print_linked_list(merged);
}
