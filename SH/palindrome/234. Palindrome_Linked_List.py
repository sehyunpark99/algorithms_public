# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def addList(cls, lst):
        if not lst:
            return None

        head = ListNode(lst[0])
        current = head

        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next

        return head

    def reset(self):
        self.val = 0
        self.next = None

def isPalindrome(head: ListNode) -> bool:
    # Edge Case
    if not head or not head.next:
        return True
    rev = None # for reverse SSL
    first = second = head

    # get the middle point of the SSL
    while first and first.next:
        first = first.next.next
        rev, rev.next, second = second, rev, second.next
    
    # for SSL with odd length -> exclude the middle component
    if first:
        second = second.next # so like go onto the next componet to compare it with reverse
    
    while rev:
        if rev.val != second.val:
            return False
        rev, second = rev.next, second.next
    return True
    

def PrintLinkedList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
        if head.next is None:
            print(head.val)
            break
    print("\n")

if __name__ == "__main__":

    print("234_PalindromeLinkedList.py")
    print("\nCase 1")

    input_list = [1,2,2,1]
    nums = ListNode.addList(input_list)
    PrintLinkedList(nums)
    ans = True
    res = isPalindrome(head=nums)
    print(res, "\n==> check: ", res==ans)
    nums.reset()


    print("\nCase 2")
    input_list = [1,2]
    nums = ListNode.addList(input_list)
    PrintLinkedList(nums)
    ans = False
    res = isPalindrome(head=nums)
    print(res, "\n==> check: ", res==ans)
    nums.reset()


    print("\nCase 3")
    input_list = [1,2,3,2,1]
    nums = ListNode.addList(input_list)
    PrintLinkedList(nums)
    ans = True
    res = isPalindrome(head=nums)
    print(res, "\n==> check: ", res==ans)
    nums.reset()


    print("\nCase 4")
    input_list = [1,2,3,4,2,1]
    nums = ListNode.addList(input_list)
    PrintLinkedList(nums)
    ans = False
    res = isPalindrome(head=nums)
    print(res, "\n==> check: ", res==ans)
    nums.reset()

    print("\nCase 5")
    input_list = [0,2,2,1]
    nums = ListNode.addList(input_list)
    PrintLinkedList(nums)
    ans = False
    res = isPalindrome(head=nums)
    print(res, "\n==> check: ", res==ans)
    nums.reset()

