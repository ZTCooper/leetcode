'''
find the logest palindrome from the beginning then add the rest[::-1] to the beginning
'''


class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        rest = s[1:]
        for i in range(len(s), 1, -1):
            if s[:i] == s[:i][::-1]:
                rest = s[i:]
                break
        return rest[::-1] + s
