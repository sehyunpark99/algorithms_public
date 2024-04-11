# Linked List Palindrome
from typing import List

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

# (a) print_list(node): print the value of linked nodes
def print_list(node: Node) -> List:
    ans = [node.data]
    while node.next:
        ans.append(node.next.data)
        node = node.next
    print(ans)

    # not necessary
    # strings = "["
    # for i in range(len(ans) - 1):
    #     strings = strings + str(ans[i]) + ", "
    # strings = strings + str(ans[-1]) + "]"
    # print(strings)
    # return strings


# (b) sub_list(s, t) to see if t is a substring of s
def sub_lists(s, t):
    # put single characters into the list
    s_list = [s.data]
    t_list = [t.data]
    while s.next and s:
        s_list.append(s.next.data)
        s = s.next
    while t.next and t:
        t_list.append(t.next.data)
        t = t.next
    # print("s_list: ", s_list)
    # print("t_list: ", t_list)

    n = len(t_list)
    for i in range(len(s_list)-n+1):
        # print("s: ", s_list[i:i+n])
        # print("t: ", t_list[:])
        if s_list[i:i+n] == t_list[:]:
            return True
    return False


# For string
# def sub_list(s, t):
#     ptr = 0
#     n = len(t)
#     while ptr < (len(s)-n+1):
#         if s[ptr:n+1] == t:
#             return True
#     return False


# (c) palindrome(s) to see if the string is a palindrome
def palindromes(s: Node):
    if not s or not s.next:
        return True
    first = second = s
    rev = None
    while first and first.next:
        first = first.next.next
        rev, rev.next, second = second, rev, second.next
    if first:
        second = second.next
    while rev.next:
        if rev != second:
            return False
        rev, second = rev.next, second.next
    return True

# (d) max_palindromes(s) to get the maximum length of palindromic substring 
def max_palindromes(s: Node):
    def palindromes(a):
        return a == a[::-1]
    
    def sublists(s, t):
        n = len(s)
        m = len(t)
        if m > n: 
            return False

        for i in range(n-m+1):
            if s[i:i+m] == t:
                return True
        return False
    
    # should go over all the substrings
    sub_list = [s.data]
    while s.next and s:
        sub_list.append(s.next.data)
        s = s.next

    ans = []
    # from the longest length (i) starting from index j
    for i in range(len(sub_list), -1, -1):
        for j in range(len(sub_list)):
            # any: 하나라고 true인 게 있으면 true
            # since we are looking through from the longest parts, we don't need to care about
            # the length in this stage
            sub = sub_list[j:j+i]
            if palindromes(sub) and not any(sublists(i, sub) for i in ans):
                print("ans: ", ans)
                ans.append(sub)                
    print(ans)

# The other version
# def max_palindromes(s):
#     n = len(s)
#     palindromes = []

#     for i in range(n):
#         for j in range(i, n):
#             substr = s[i:j+1]
#             if palindrome(substr):
#                 is_maximal = True
#                 for p in palindromes:
#                     if substring(p,substr):
#                         is_maximal = False
#                         break
#                 if is_maximal:
#                     palindromes.append(substr)

#     dup_list=[]
#     for i in range(len(palindromes)-1):
#         for j in range(i+1,len(palindromes)):
#             if palindromes[i] in palindromes[j]:
#                 dup_list.append(palindromes[i])
                
#     #print(dup_list)
#     return [x for x in palindromes if x not in dup_list]

        
if __name__ == "__main__":
    s = Node(3,Node(7,Node(7, Node(3, None)))) #3->7->7->3->None
    t = Node(3,Node(7,Node(7, None))) #3->7->7->None
    print_list(s) # print(print_list(s)) 로 하고 싶으면 function에서 return 아니면 print
    print_list(t)
    print("if t is in s : ", sub_lists(s,t)) # if t is in s

    a = Node(3,Node(7,Node(3, None))) #3->7->3->None
    print("if a is palindrome", palindromes(a))
    print_list(a)
    print("if a is in s : ", sub_lists(s,a)) # if a in s

    s = Node(1,Node(2,Node(1, Node(3, None)))) #1->2->1->3->None
    # print_list(s)
    max_palindromes(s)

    # s: 8->1->2->3->3->2->1->4->9->4->5->6->7->...
    s = Node(8,Node(1,Node(2,Node(3,Node(3,Node(2,Node(1,Node(4,Node(9,Node(4,Node(5,Node(6,Node(7,Node(6,Node(5,Node(4,Node(1,None)))))))))))))))))
    # print_list(s)
    max_palindromes(s)

    s = Node(2,Node(8,Node(1,Node(2,Node(1, Node(3, None))))))
    # print_list(s)
    max_palindromes(s) # [ [ 1 , 2 , 1 ] , [ 8 ] , [ 3 ] ]