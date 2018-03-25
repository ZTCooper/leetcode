class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        result = ""
        for i in range(len(strs[0])):
            prefix = strs[0][i]
            result += strs[0][i]
            for j in range(1, len(strs)):
                try:
                    if strs[j][i:].index(prefix) != 0:
                        return result[:i]
                except ValueError:
                    return result[:i]
        return result
