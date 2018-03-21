class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return ""
        if numRows == 1:
            return s
        container = []
        for n in range(numRows):
            container.append([])
        n = 0
        for i in range(len(s)):
            container[n].append(s[i])
            if (i // (numRows - 1)) % 2 == 0:
                n += 1
            else:
                n -= 1
        for i in range(1, numRows):
            container[0].extend(container[i])
        result = ""
        for i in container[0]:
            result += i
        return result
