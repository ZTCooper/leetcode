class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i in bracket.values():
                stack.append(i)
            elif i in bracket.keys():
                if (not stack) or stack[-1] != bracket[i]:
                    return False
                else:
                    stack.pop()
        return not stack


s = Solution()
print(s.isValid("()"))
