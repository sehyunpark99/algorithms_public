#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

typedef struct LLNode {
    int val;
    struct LLNode *prev, *next;
} LLNode;

void print_linked_list(LLNode *head){
    LLNode *cur=head;
    while (cur != NULL){
        printf("%d", cur-> val);
        cur = cur -> next;
    }
    printf("\n");
}

// (a) sort list in increasing order [Insertion sort]
void sort_list(LLNode* head){
    if (!head || !head->next){
        head = head; // No changes
    }
    
    //dummy
    LLNode *dummy = (LLNode*)malloc(sizeof(LLNode));
    dummy->val = -5000;
    dummy->next = head;
    
    LLNode* sorted = head;
    LLNode* unsorted = head->next;
    
    while (unsorted) {
        if (unsorted->val >= sorted->val){
            sorted = sorted->next; //  Search for next 
        }
        else {
            LLNode* prev = dummy;
            while (prev->next->val <= unsorted->val){
                prev = prev->next; // next until insert
            }
            sorted->next = unsorted->next;
            unsorted->next = prev->next;
            prev->next = unsorted;
        }
        unsorted = sorted->next;
    }
    head = dummy->next;
    print_linked_list(head);
}

// (b) sort each list
void sort_each_list(LLNode *head[100], int N){
    for(int i=0; i<N; i++){
        sort_list(head[i]);
    }
}


// (c) Mergesort
void *sort_list_des(LLNode* head){
    if (!head || !head->next){
        head = head; // No changes
    }
    
    //dummy
    LLNode* dummy = (LLNode*)malloc(sizeof(LLNode));
    dummy->val = -5000;
    dummy->next = head;
    
    LLNode* sorted = head;
    LLNode* unsorted = head->next;
    
    while (unsorted) {
        if (unsorted->val <= sorted->val){
            sorted = sorted->next; //  Search for next 
        }
        else {
            LLNode* prev = dummy;
            while (prev->next->val >= unsorted->val){
                prev = prev->next; // next until insert
            }
            sorted->next = unsorted->next;
            unsorted->next = prev->next;
            prev->next = unsorted;
        }
        unsorted = sorted->next;
    }
    head = dummy->next;
}

LLNode *mergeTwoSortedLists(LLNode* l1, LLNode* l2)
{
    if (l1 == NULL && l2 == NULL) return NULL;
    if (l1 == NULL) return l2;
    if (l2 == NULL) return l1;
    
    LLNode* prev = NULL;
    LLNode* head = l1->val <= l2->val ? l2 : l1; //head=l1 for larger l1, else head=l2
    
    while (l1 != NULL && l2 != NULL) {
        if (l2->val <= l1->val) {
            if (prev != NULL)
                prev->next = l1; // connect next
            prev = l1; 
            l1 = l1->next;
        } else {
            if (prev != NULL)
                prev->next = l2;
            prev = l2;
            l2 = l2->next;
        }
    }
    
    if (l1)
        prev->next = l1;
    if (l2)
        prev->next = l2;
    
    return head;
}

LLNode* merge_sorted_lists(LLNode *head[100], int N){
    if (N == 0) {
        return NULL;
    }

    for(int i=0; i<N; i++){
        sort_list_des(head[i]);
    }

    LLNode** ans = (LLNode**)malloc(N*sizeof(LLNode*));
    for(int i=0; i<N; i++){
        ans[i] = head[i];
    }
    for (int i = 1; i < N; ++i) {
        LLNode* x = mergeTwoSortedLists(ans[i - 1], ans[i]);
        ans[i] = x;
    }
    LLNode* result = ans[N - 1];
    free(ans);
    return result;
}


// For testing test cases
int main() {
    printf("Q2\n");
    printf("====================================\n");
    // 3->1->5
    printf("[Case 1]\n");
    LLNode *node11 = (LLNode *) malloc (sizeof(LLNode));
    LLNode *node12 = (LLNode *) malloc (sizeof(LLNode));
    LLNode *node13 = (LLNode *) malloc (sizeof(LLNode));
    node11->val = 3, node11->next = node12, node11->prev = NULL;
    node12->val = 1, node12->next = node13, node12->prev = node11;
    node13->val = 5, node13->next = NULL, node13->prev = node12;
    LLNode *list1 = node11;

    print_linked_list(list1);
    sort_list(list1);
    print_linked_list(list1);

    printf("====================================\n");
    printf("[Case 2]\n");
    LLNode *node21 = (LLNode *) malloc (sizeof(LLNode));
    LLNode *node22 = (LLNode *) malloc (sizeof(LLNode));
    LLNode *node23 = (LLNode *) malloc (sizeof(LLNode));
    LLNode *node24 = (LLNode *) malloc (sizeof(LLNode));
    LLNode *node25 = (LLNode *) malloc (sizeof(LLNode));
    node21->val = 2, node21->next = node22, node21->prev = NULL;
    node22->val = 8, node22->next = node23, node22->prev = node21;
    node23->val = 6, node23->next = node24, node23->prev = node22;
    node24->val = 1, node24->next = node25, node24->prev = node23;
    node25->val = 1, node25->next = NULL, node25->prev = node24;
    LLNode *list2 = node21;
    print_linked_list(list2);
    sort_list(list2);
    print_linked_list(list2);

    printf("====================================\n");
    printf("[Sort Lists]\n");
    LLNode *lists[100];
    lists[0] = list1;
    lists[1] = list2;
    sort_each_list(lists, 2);

    printf("====================================\n");
    printf("[Merge Sort Lists]\n");
    LLNode *merged = merge_sorted_lists(lists, 2);
    print_linked_list(merged);
}

