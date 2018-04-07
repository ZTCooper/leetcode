class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        j = len(s) - 1
        for i in range(len(s) // 2):
            if s[i] != s[j]:
                check = s[:i] + s[i + 1:]
                if check == check[::-1]:
                    return True
                check = s[:j] + s[j + 1:]
                if check == check[::-1]:
                    return True
                return False
            j -= 1
        return True
