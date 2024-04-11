// void sort_list(LLNode *head){
//     struct LLNode *new_head = (struct LLNode *)malloc(sizeof(struct LLNode));
//     // memset(new_head, 0, sizeof(head));
//     struct LLNode *current = head;
//     struct LLNode *tmp = NULL;
//     while(current != NULL){
//         // sortedInsert(new_head, current);
//         if (new_head == NULL || (new_head)->val >= current->val){
//             current->next = new_head;
//             new_head = current;
//         }
//         else{
//             tmp = new_head;
//             while (tmp->next != NULL && tmp->next->val < current->val){
//                 tmp = tmp->next;
//             }
//             current->next = tmp->next;
//             tmp->next = current;
//         }  
//     }
//     head = new_head;
//     // return head;
// }


// void swap(LLNode *tmp1, LLNode *tmp2){
//     struct LLNode *tmp;
//     tmp = tmp2;
//     tmp2 = tmp1;
//     tmp1 = tmp;
// }

// void sort_list(LLNode *head){
//     bool swapped = true;
//     struct LLNode *current = head;

//     while(swapped){
//         swapped = false;

//         while(current->next){
//             if(current->val > current->next->val){
//                 swap(current, current->next);
//                 swapped = true;
//             }
//             current = current -> next;
//         }
//     }
//     head = current;
// }


// Function to add a list of integers to a linked list -> change to value
// struct LLNode* addList(int *lst, int size) {
//     if (!lst || size == 0) {
//         return NULL;
//     }

//     struct LLNode *head = (struct LLNode *)malloc(sizeof(struct LLNode));
//     head->val = lst[0];
//     head->next = NULL;
//     struct LLNode *current = head;

//     for (int i = 1; i < size; i++) {
//         current->next = (struct LLNode *)malloc(sizeof(struct LLNode));
//         current->next->val = lst[i];
//         current->next->next = NULL;
//         current = current->next;
//     }

//     return head;
// }