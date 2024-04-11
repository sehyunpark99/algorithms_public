'''
443. String Compression
Medium
Topics
Companies
Hint
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
'''
from collections import defaultdict
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        s = '' # start with an empty array
        history = defaultdict(int)
        for char in chars:
            if char not in history.keys():
                history[char] = 1
            else:
                history[char] += 1
        for key, value in history.items():
            if value == 1:
                s = s + str(key)
            else:
                s = s + str(key) + str(value)
        array = [char for char in s]
        return len(array)
        

if __name__ == "__main__":
    print("GNode_2360_Longest_Cycle_in_a_Graph.py")

    solution = Solution()
    print("\nCase 1")
    chars = ["a","a","b","b","c","c","c"]
    res = solution.compress(chars)  # Output: 6
    ans = 6
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 2")
    chars = ["a"]
    res = solution.compress(chars)  # Output: 1
    ans = 1
    print(res, "\n  ==> check: ", res==ans)

    print("\nCase 3")
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    res = solution.compress(chars)  # Output: 4
    ans = 4
    print(res, "\n  ==> check: ", res==ans)

'''
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars) == 1:
            return len(chars)

        left, right = 0, 0
        num = 0
        while right < len(chars):
            if (chars[left] != chars[right]):
                ## insert the num right next to the alphabet
                if num == 1:
                    left = right
                else:
                    num_str = str(num)
                    chars[left + 1] = num_str[0]
                    if len(num_str) > 1:
                        for i in range(1, len(num_str)):
                            chars.insert(left + 1 + i, num_str[i])
                        ## erase other alphabet in between (left+ lenstr +1 < idx < right)
                        del chars[left + len(num_str) + 1:right+len(num_str)-1]
                        right = left = left + len(num_str) + 1
                    else:
                        if num > 2:
                            del chars[left + 2:right]
                            right = left = left + 2
                        else:
                            left = right
                num = 0
            else:
                num += 1
                right += 1

        # 마지막 후처리
        if right == len(chars):
            num_str = str(num)
            if num > 1:
                chars[left + 1] = num_str[0]
                if len(num_str) > 1:
                    for i in range(1, len(num_str)):
                        chars.insert(left + 1 + i, num_str[i])
                    del chars[left + len(num_str) + 1:right+len(num_str)-1]
                else:
                    if num > 2:
                        del chars[left + 2:right]
        

        return len(chars)
        '''