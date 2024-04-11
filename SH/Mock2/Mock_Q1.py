
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(self, head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1

    result = ListNode(0)
    p = result

    while head1 and head2:
        if head1.val <= head2.val:
            p.next = ListNode(head1.val)
            head1 = head1.next
            p = p.next
        else:
            p.next = ListNode(head2.val)
            head2 = head2.next
            p = p.next

    if head1:
        p.next = head1
    if head2:
        p.next = head2
    return result.next

def sortList(head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head

        slow, fast = head, head.next

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        head1, head2 = head, slow.next
        slow.next = None
        head1 = sortList(head1)
        head2 = sortList(head2)
        head = merge(head1, head2)
        return head

# During test-time
# def createListNodeFromList(list_in: List[List]) -> list:
#     output = []

#     for list in list_in:
#         tmp = []
#         tmp_node = None
#         for i in range(len(list)-1, -1, -1):
#             new = ListNode(list[i])
#             new.next = tmp_node 
#             tmp.append(new)
#         for i in range(len(tmp)-1, -1, -1):
#             output.append(tmp[i])        
#     return output

def createListNodeFromList(list_in: List[List]) -> list:
    output = []

    for list in list_in:
        head = ListNode(0)
        curr = head # ptr
        for i in range(len(list)):
            curr.next = ListNode(list[i])
            curr = curr.next
        output.append(head.next)        
    return output


def printList(node) -> ListNode:
    output = []
    while node:
        output.append(node.val)
        print(node.val, end=" -> ")
        node = node.next
        if node.next is None:
            print("None")
            break
    return output

def mergeTwoLists(list1, list2):
    first = second = list1
    i, j = 0,0
    
    # For reaching ath node
    while i!=a-1:
        first = first.next
        i += 1

    # For reaching bth node
    while j!=b:
        second = second.next
        j += 1
        
    # Connecting the first runner with second list
    first.next = list2

    # Until we reach the end of list2 we are connecting first and list2
    while list2.next:
        list2 = list2.next

    # Connecting the remaining part of list1
    list2.next = second.next

    return list1

def mergeTwoLists(list1, list2):
    if not list1 or not list2:
        return list1 or list2
    if list1.val < list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2

def mergeKlist(lists):
    if not lists:
        return None

    list_ = [lists[0]]
    for i in range(len(lists)-1):
        x = mergeTwoLists(list_[i], lists[i+1])
        list_.append(x)
    
    return list_[-1]


if __name__ == "__main__":
    print("Mock_Q1.py")
    
    print("\nCase 1")
    edges = [[1, 4, 5],[1, 3, 4],[2, 6]]
    res = createListNodeFromList(edges) 
    ans = [1, 1, 2, 3, 4, 4, 5, 6]
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 2")
    times = [[]]
    res = createListNodeFromList(edges)  
    ans = []
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 3")
    edges = [[1, 4, 5, 7, 8, 9],[1, 3, 4]]
    res = createListNodeFromList(edges) 
    ans = [1, 1, 3, 4, 4, 5, 7, 8, 9]
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 4")
    times = []
    res = createListNodeFromList(edges)  
    ans = []
    print(res, "\n  ==> check: ", res==ans)

