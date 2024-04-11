'''
1315. Sum of Nodes with Even-Valued Grandparent
Medium
Topics
Companies
Hint
Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

A grandparent of a node is the parent of its parent if it exists.

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
'''


def sumEvenGrandparent(self, root, p=1, gp=1):
    return self.sumEvenGrandparent(root.left, root.val, p) \
        + self.sumEvenGrandparent(root.right, root.val, p) \
        + root.val * (1 - gp % 2) if root else 0    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(root,dad,gp):
            if not root:
                return 0
            x=0
            if(gp%2==0):
                x=root.val
            x+=dfs(root.left,root.val,dad)
            x+=dfs(root.right,root.val,dad)
            return x

        return dfs(root,1,1)