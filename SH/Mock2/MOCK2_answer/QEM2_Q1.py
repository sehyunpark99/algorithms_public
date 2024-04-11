'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.
Constraints:
-	k == lists.length
-	0 <= k <= 104
-	0 <= lists[i].length <= 500
-	-10^4 <= lists[i][j] <= 10^4
-	lists[i] is sorted in ascending order.
-	The sum of lists[i].length will not exceed 10^4.

Example 1
-	Input	: lists = [ [1,4,5], [1,3,4], [2,6] ]
-	Output	: [1,1,2,3,4,4,5,6]
Example 2
-	Input	: lists = []
-	Output	: []
Example 3
-	Input	: lists = [[]]
-	Output	: []

'''

#### JP for debugging ####
TEST_Q1_FLAG = True
#### JP for debugging ####


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## Q1 createListNodeFromList
def createListNodeFromList(list_tmp):
    lists = []  # 결과를 저장할 리스트
    for sublist in list_tmp:
        # 서브 리스트가 비어있으면 다음으로
        if not sublist:
            continue
        head = ListNode(1000000000000000)  # 더미 헤드 
        current = head
        for value in sublist:
            current.next = ListNode(value)
            current = current.next
        lists.append(head.next)  # 더미 헤드 노드를 제외한 연결 리스트를 추가
    return lists

## Q2 printList
def printList(node):
    elements = []
    while node:
        elements.append(node.val)
        node = node.next
    print(elements)

## Q3 Divide and Conquer
def merge2Lists(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val < l2.val:
        l1.next = merge2Lists(l1.next, l2)
        return l1
    else:
        l2.next = merge2Lists(l1, l2.next)
        return l2
    
def mergeKLists(lists):
    k = len(lists)
    if k == 0: 
        printList(lists)
        return None
    if k == 1: 
        printList(lists[0])
        return lists[0]

    curList = lists[0]
    for i in range(1, k):
        curList = merge2Lists(curList, lists[i])

    printList(curList)
    return curList


## Test Q1 function
def test_Q1(lists_in, lists):
    Q1_res = createListNodeFromList(lists_in)
    list01 = []
    list02 = []
    for node in lists:
        node_tmp = []
        while (node):
            node_tmp.append(node.val)
            node = node.next
        list01.append(node_tmp)

    for node in Q1_res:
        node_tmp = []
        while (node):
            node_tmp.append(node.val)
            node = node.next
        list02.append(node_tmp)

    # print(list01)
    # print(list02)

    return list01 == list02


if __name__ == "__main__":
    print("[PY] 23. Merge k sorted linked lists")

    print("Case 1")
    lists_in = [ [1, 4, 5], [1, 3, 4], [2, 6] ]
    lists = createListNodeFromList(lists_in)
    print("Input: ")
    for l in lists:
        printList(l)

    print("Output: ")
    mergeKLists(lists)
    print()

    ## Test Q1
    if TEST_Q1_FLAG:
        l1 = ListNode(1, ListNode(4, ListNode(5)))
        l2 = ListNode(1, ListNode(3, ListNode(4)))
        l3 = ListNode(2, ListNode(6))
        lists_legacy = [l1, l2, l3]
        print("### Testing Q1 function... -> ", test_Q1(lists_in, lists_legacy))
        print()

    print("Case 2")
    lists_in = []
    lists = createListNodeFromList(lists_in)
    print("Input: ")
    print(lists)
    print("Output: ")
    mergeKLists(lists)
    print()

    print("Case 3")
    lists_in = [[]]
    lists = createListNodeFromList(lists_in)
    print("Input: ")
    print(lists)
    print("Output: ")
    mergeKLists(lists)
    print()

    print("Case 4")
    lists_in = [ [1, 4, 5] ]
    lists = createListNodeFromList(lists_in)
    print("Input: ")
    for l in lists:
        printList(l)
    print("Output: ")
    mergeKLists(lists)
    print()

    ## Test Q1
    if TEST_Q1_FLAG:
        l1 = ListNode(1, ListNode(4, ListNode(5)))
        lists_legacy = [l1]
        print("### Testing Q1 function... -> ", test_Q1(lists_in, lists_legacy))
        print()


    print("Case 5")
    lists_in = [ [1, 4, 5, 7, 8, 9], [1, 3, 4] ]
    lists = createListNodeFromList(lists_in)
    print("Input: ")
    for l in lists:
        printList(l)
    print("Output: ")
    mergeKLists(lists)
    print()

    ## Test Q1
    if TEST_Q1_FLAG:
        l1 = ListNode(1, ListNode(4, ListNode(5, ListNode(7, ListNode(8, ListNode(9))))))
        l2 = ListNode(1, ListNode(3, ListNode(4)))
        lists_legacy= [l1, l2]
        print("### Testing Q1 function... -> ", test_Q1(lists_in, lists_legacy))
        print()



    


