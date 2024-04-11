# A permutation, also called an "arrangement number" or "order", is a rearrangement of 
# the elements of an ordered list S into a one-to-one correspondence with S itself.
# Treating a string as an order list, we may have a permutation of the string. 
# For example, when the string is "abc", a permutation of the string is "bca".
# Thus, a string of length n has n! permutations. In this problem, given a string s, you will
# implement a function str_perm(s) that returns a list of all permuataions of s. 
# However, the list contains no identical permutations. The list should contain the 
# permutations in lexicographical order (a.k.a alphabetical order). The characters used in a 
# string are only lower-case alphabets


def permute(s, left, right):
    if left == right:
        print("".join(s))  # Print the permutation
    else:
        for i in range(left, right + 1):
            # Swap characters at positions left and i
            s[left], s[i] = s[i], s[left]
            permute(s, left + 1, right)  # Recur for the next position
            # Backtrack: undo the swap
            s[left], s[i] = s[i], s[left]

def str_perm(s):
    permute(list(s), 0, len(s) - 1)



def str_perm(s):
    result = []
    def perm_help(s, left, right):
        if left == right:
            result.append("".join(s)) # join to make it as a string not the list
        else:
            for i in range(left, right+1):
                s[left], s[i] = s[i], s[left]
                perm_help(s, left+1, right) # for the next position
                # Backtracking to undo swap
                s[left], s[i] = s[i], s[left]
    perm_help(list(s), 0, len(s)-1)
    return result


if __name__ == "__main__":
    print("QE_22_09_Q1.py")
    print("\nCase 1")
    # Example usage:
    s = "abc"
    result = str_perm(s) # Output: ["abc", "acb", "bac", "bca", "cab", "cba"]
    print(result)

    print("\nCase 2")
    s = "abb"
    result = str_perm(s) # Output: ["abb", "bab", "bba"]
    print(result)
