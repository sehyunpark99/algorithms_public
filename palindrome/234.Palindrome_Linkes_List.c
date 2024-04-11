#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

// Function to add a list of integers to a linked list
struct ListNode* addList(int *lst, int size) {
    if (!lst || size == 0) {
        return NULL;
    }

    struct ListNode *head = (struct ListNode *)malloc(sizeof(struct ListNode));
    head->val = lst[0];
    head->next = NULL;
    struct ListNode *current = head;

    for (int i = 1; i < size; i++) {
        current->next = (struct ListNode *)malloc(sizeof(struct ListNode));
        current->next->val = lst[i];
        current->next->next = NULL;
        current = current->next;
    }

    return head;
}

// Function to reset the values of the linked list
void reset(struct ListNode *head) {
    while (head) {
        head->val = 0;
        struct ListNode *tmp = head;
        head = head->next;
        free(tmp);
    }
}

int isPalindrome(struct ListNode* head) {
    // Edge Case
    if (!head || !head->next) {
        return 1;
    }

    struct ListNode *rev = NULL;
    struct ListNode *first = head;
    struct ListNode *second = head;

    while(first && first->next){
        first = first->next->next;
        struct ListNode *tmp = rev;
        rev = second;
        // cannot simply use rev as the pointer shitfed
        second = second->next;
        rev->next = tmp;
    }

    if(first){
        second = second->next;
    }

    while(rev){
        if(rev->val != second->val){return 0;}
        rev = rev->next;
        second = second->next;
    }
    return 1;
}


// GPT
// int isPalindrome(struct ListNode *head) {
//     // Edge Case
//     if (!head || !head->next) {
//         return 1;
//     }

//     struct ListNode *rev = NULL; // for reverse SSL
//     struct ListNode *first = head;
//     struct ListNode *second = head;

//     // get the middle point of the SSL
//     while (first && first->next) {
//         first = first->next->next;
//         struct ListNode *temp = rev;
//         rev = second;
//         second = second->next;
//         rev->next = temp;
//     }

//     // for SSL with odd length -> exclude the middle component
//     if (first) {
//         second = second->next; // so like go onto the next componet to compare it with reverse
//     }

//     while (rev) {
//         if (rev->val != second->val) {
//             return 0;
//         }
//         rev = rev->next;
//         second = second->next;
//     }

//     return 1;
// }

// Function to print the linked list
void printLinkedList(struct ListNode *head) {
    while (head) {
        printf("%d -> ", head->val);
        head = head->next;
    }
    printf("NULL\n");
}

int main() {
    printf("234_PalindromeLinkedList.c\n");
    printf("\nCase 1\n");

    int input_list1[] = {1, 2, 2, 1};
    int size1 = sizeof(input_list1) / sizeof(input_list1[0]);
    struct ListNode *nums1 = addList(input_list1, size1);
    printLinkedList(nums1);
    int ans1 = 1;
    int res1 = isPalindrome(nums1);
    printf("%d \n==> check: %s\n", res1, res1 == ans1 ? "true" : "false");
    reset(nums1);

    printf("\nCase 2\n");
    int input_list2[] = {1, 2};
    int size2 = sizeof(input_list2) / sizeof(input_list2[0]);
    struct ListNode *nums2 = addList(input_list2, size2);
    printLinkedList(nums2);
    int ans2 = 0;
    int res2 = isPalindrome(nums2);
    printf("%d \n==> check: %s\n", res2, res2 == ans2 ? "true" : "false");
    reset(nums2);

    printf("\nCase 3\n");
    int input_list3[] = {1, 2, 3, 2, 1};
    int size3 = sizeof(input_list3) / sizeof(input_list3[0]);
    struct ListNode *nums3 = addList(input_list3, size3);
    printLinkedList(nums3);
    int ans3 = 1;
    int res3 = isPalindrome(nums3);
    printf("%d \n==> check: %s\n", res3, res3 == ans3 ? "true" : "false");
    reset(nums3);

    printf("\nCase 4\n");
    int input_list4[] = {1, 2, 3, 4, 2, 1};
    int size4 = sizeof(input_list4) / sizeof(input_list4[0]);
    struct ListNode *nums4 = addList(input_list4, size4);
    printLinkedList(nums4);
    int ans4 = 0;
    int res4 = isPalindrome(nums4);
    printf("%d \n==> check: %s\n", res4, res4 == ans4 ? "true" : "false");
    reset(nums4);
}