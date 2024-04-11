from collections import defaultdict, deque
from typing import List

class TNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# (a) returns True if the binary tree satisfies the max-heap property
# max heap if the value is smaller or equal tot he value of parent
def is_max_heap(T):
    if not T:
        return True
    q = deque([T])
    while q:
        node = q.popleft()
        if node is None:
            continue
        if node.left is not None:
            if node.val < node.left.val:
                return False
        if node.right is not None:   
            if node.val < node.right.val:
                return False
        q.append(node.left)
        q.append(node.right)

    return True


# (b) array representation of a binary max-heap 
## Heapify first
# def maxHeapify(pos):
#     # If the node is a non-leaf node and smaller
#     # than any of its child
#     if not pos:
#         if (Heap[pos] < Heap[leftChild(pos)] or
#             Heap[pos] < Heap[rightChild(pos)]):

#             # Swap with the left child and heapify
#             # the left child
#             if (Heap[leftChild(pos)] >
#                 Heap[rightChild(pos)]):
#                 swap(pos, leftChild(pos))
#                 maxHeapify(leftChild(pos))

#             # Swap with the right child and heapify
#             # the right child
#             else:
#                 swap(pos, rightChild(pos))
#                 maxHeapify(rightChild(pos))


def binary_tree_to_heap_array(T):
    ans = []
    if not T:
        return ans
    
    q = deque([T])
    # In-order Traversal O(1)
    while q:
        tmp = []
        n = len(q) # number of node in the level of tree
        
        for i in range(n):
            curr = q.popleft()
            ans.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return ans

# Main Function
if __name__ == "__main__":
    print("QE_Qn1.py")
    print("\nCase 1")
    # Example
    T7, T8, T9, T10 = TNode(4), TNode(6), TNode(5), TNode(5)
    T3, T4 = TNode(3), TNode(6, T7, T8)
    T5, T6 = TNode(1, None, T9), TNode(4, T10, None)
    T1, T2 = TNode(5, T3, T4), TNode(7, T5, T6)
    T0 = TNode(8, T1, T2)

    print(is_max_heap(T0)) # False

    print(binary_tree_to_heap_array(T0)) # [8, 6, 7, 6, 4, 5, 5, 4, 5, 1, 3]

    print("\nCase 2")
    # Example
    T7, T8, T9, T10 = TNode(4), TNode(5), TNode(1), TNode(4)
    T3, T4 = TNode(3), TNode(6, T7, T8)
    T5, T6 = TNode(5, None, T9), TNode(5, T10, None)
    T1, T2 = TNode(6, T3, T4), TNode(7, T5, T6)
    T0 = TNode(8, T1, T2)

    print(is_max_heap(T0)) # False

    print(binary_tree_to_heap_array(T0)) # [8, 6, 7, 6, 4, 5, 5, 4, 5, 1, 3]




