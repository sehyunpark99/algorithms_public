
# Bubble Sort
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
def swap(ptr1, ptr2):
    tmp = ptr2.data
    ptr2.data = ptr1.data
    ptr1.data = tmp
 
def bubbleSort(head):
    swapped = True
 
    while swapped:
        swapped = False
        current = head
 
        while current.next:
            if current.data > current.next.data:
                swap(current, current.next)
                swapped = True
            current = current.next
 
def printList(n):
    while n:
        print(n.data, "->", end=" ")
        n = n.next
    print()
 
def insertAtTheBegin(start_ref, data):
    ptr1 = Node(data)
    ptr1.next = start_ref
    return ptr1
 
# Driver Code
if __name__ == "__main__":
    arr = [0,1,0,1,0,1]
    list_size = len(arr)
 
    start = None
 
    # Create linked list from the array arr[]
    for i in range(list_size - 1, -1, -1):
        start = insertAtTheBegin(start, arr[i])
 
    print("Linked list before sorting")
    printList(start)
 
    bubbleSort(start)
 
    print("Linked list after sorting")
    printList(start)


# Insertion Sort
# Python implementation of above algorithm
 
# Node class
class Node:
 
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
# function to sort a singly linked list using insertion sort
 
 
def insertionSort(head_ref):
 
    # Initialize sorted linked list
    sorted = None
 
    # Traverse the given linked list and insert every
    # node to sorted
    current = head_ref
    while (current != None):
 
        # Store next for next iteration
        next = current.next
 
        # insert current in sorted linked list
        sorted = sortedInsert(sorted, current)
 
        # Update current
        current = next
 
    # Update head_ref to point to sorted linked list
    head_ref = sorted
    return head_ref
 
# function to insert a new_node in a list. Note that this
# function expects a pointer to head_ref as this can modify the
# head of the input linked list (similar to push())
 
 
def sortedInsert(head_ref, new_node):
 
    current = None
 
    # Special case for the head end */
    if (head_ref == None or (head_ref).data >= new_node.data):
 
        new_node.next = head_ref
        head_ref = new_node
 
    else:
 
        # Locate the node before the point of insertion
        current = head_ref
        while (current.next != None and
                current.next.data < new_node.data):
 
            current = current.next
 
        new_node.next = current.next
        current.next = new_node
 
    return head_ref
 
# BELOW FUNCTIONS ARE JUST UTILITY TO TEST sortedInsert
 
# Function to print linked list */
 
 
def printList(head):
 
    temp = head
    while(temp != None):
 
        print(temp.data, end=" ")
        temp = temp.next
 
# A utility function to insert a node
# at the beginning of linked list
 
 
def push(head_ref, new_data):
 
    # allocate node
    new_node = Node(0)
 
    # put in the data
    new_node.data = new_data
 
    # link the old list of the new node
    new_node.next = (head_ref)
 
    # move the head to point to the new node
    (head_ref) = new_node
    return head_ref
 
# Driver program to test above functions
 
 
a = None
a = push(a, 5)
a = push(a, 20)
a = push(a, 4)
a = push(a, 3)
a = push(a, 30)
 
print("Linked List before sorting ")
printList(a)
 
a = insertionSort(a)
 
print("\nLinked List after sorting ")
printList(a)


# Merge Sort
# Python3 program to merge sort of linked list
 
# create Node using class Node.
 
 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    # push new value to linked list
    # using append method
    def append(self, new_value):
 
        # Allocate new node
        new_node = Node(new_value)
 
        # if head is None, initialize it to new node
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
 
        # Append the new node at the end
        # of the linked list
        curr_node.next = new_node
 
    def sortedMerge(self, a, b):
        result = None
 
        # Base cases
        if a == None:
            return b
        if b == None:
            return a
 
        # pick either a or b and recur..
        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result
 
    def mergeSort(self, h):
 
        # Base case if head is None
        if h == None or h.next == None:
            return h
 
        # get the middle of the list
        middle = self.getMiddle(h)
        nexttomiddle = middle.next
 
        # set the next of middle node to None
        middle.next = None
 
        # Apply mergeSort on left list
        left = self.mergeSort(h)
 
        # Apply mergeSort on right list
        right = self.mergeSort(nexttomiddle)
 
        # Merge the left and right lists
        sortedlist = self.sortedMerge(left, right)
        return sortedlist
 
    # Utility function to get the middle
    # of the linked list
    def getMiddle(self, head):
        if (head == None):
            return head
 
        slow = head
        fast = head
 
        while (fast.next != None and
                fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
 
        return slow
 
# Utility function to print the linked list
 
 
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print(' ')
 
 
# Driver Code
if __name__ == '__main__':
    li = LinkedList()
 
    # Let us create a unsorted linked list
    # to test the functions created.
    # The list shall be a: 2->3->20->5->10->15
    li.append(15)
    li.append(10)
    li.append(5)
    li.append(20)
    li.append(3)
    li.append(2)
 
    # Apply merge Sort
    li.head = li.mergeSort(li.head)
    print("Sorted Linked List is:")
    printList(li.head)