#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// Define Node structure for linked list
typedef struct Node {
    int data;
    struct Node *next;
} Node;

// Function to print the linked list
void print_list(Node *node) {
    printf("[");
    while (node != NULL) {
        printf("%d", node->data);
        node = node->next;
        if (node != NULL) {
            printf(", ");
        }
    }
    printf("]\n");
}

// Function to check if t is a substring of s
bool sub_lists(Node *s, Node *t) {
    Node *s_ptr = s;
    Node *t_ptr = t;

    while (s_ptr != NULL && t_ptr != NULL) {
        if (s_ptr->data != t_ptr->data) {
            return false;
        }
        s_ptr = s_ptr->next;
        t_ptr = t_ptr->next;
    }

    // If t has been completely matched in s
    if (t_ptr == NULL) {
        return true;
    }

    return false;
}

// Function to check if a linked list is a palindrome
bool palindromes(Node *s) {
    if (s == NULL || s->next == NULL) {
        return true;
    }

    // Initialize pointers for slow and fast traversal
    Node *slow = s;
    Node *fast = s;

    // Traverse to find the middle of the linked list
    while (fast->next != NULL && fast->next->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
    }

    // Reverse the second half of the linked list
    Node *prev = NULL;
    Node *curr = slow->next;
    Node *next = NULL;

    while (curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    // Compare the first half and the reversed second half of the linked list
    Node *p1 = s;
    Node *p2 = prev;

    while (p2 != NULL) {
        if (p1->data != p2->data) {
            return false;
        }
        p1 = p1->next;
        p2 = p2->next;
    }

    return true;
}

// Function to find the maximum length of palindromic substrings in a linked list
void max_palindromes(Node *s) {
    if (s == NULL) {
        return;
    }

    Node *curr = s;

    // Iterate through each node in the linked list
    while (curr != NULL) {
        Node *start = curr;
        Node *end = curr;

        // Move end pointer to the end of the linked list
        while (end->next != NULL) {
            end = end->next;
        }

        // Check if the current subarray is a palindrome
        while (start != NULL) {
            if (palindromes(start)) {
                print_list(start);
            }
            start = start->next;
        }

        curr = curr->next;
    }
}

int main() {
    Node *s1 = (Node *)malloc(sizeof(Node));
    s1->data = 3;
    s1->next = (Node *)malloc(sizeof(Node));
    s1->next->data = 7;
    s1->next->next = (Node *)malloc(sizeof(Node));
    s1->next->next->data = 7;
    s1->next->next->next = (Node *)malloc(sizeof(Node));
    s1->next->next->next->data = 3;
    s1->next->next->next->next = NULL;

    Node *t = (Node *)malloc(sizeof(Node));
    t->data = 3;
    t->next = (Node *)malloc(sizeof(Node));
    t->next->data = 7;
    t->next->next = (Node *)malloc(sizeof(Node));
    t->next->next->data = 7;
    t->next->next->next = NULL;

    printf("List s1: ");
    print_list(s1);

    printf("List t: ");
    print_list(t);

    printf("If t is a substring of s1: %s\n", sub_lists(s1, t) ? "true" : "false");

    printf("If list s1 is a palindrome: %s\n", palindromes(s1) ? "true" : "false");

    printf("Max palindromes in list s1:\n");
    max_palindromes(s1);

    free(s1);
    free(t);

    return 0;
}
