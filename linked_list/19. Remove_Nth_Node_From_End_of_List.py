'''
19. Remove Nth Node From End of List


Given the head of a linked list, 
remove the nth node from the end of the list and return its head.
'''


# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Node, n: int) -> Node:
        ptr = 0
        dummy = first = second = Node(0)
        dummy.next = head
        while ptr != n:
            first = first.next
            ptr += 1

        while first.next:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next
    

s = Node(1,Node(2,Node(3, Node(4, Node(5))))) #3->7->7->3->None
n = 2
Solution().removeNthFromEnd(s, n)