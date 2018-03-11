'''
用嵌套列表
从字符串首依次遍历其后元素，若不在之前的子字符串中，则加入嵌套列表
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        targets = []
        for i in range(len(s)):
            targets.append([])
            targets[i].append(s[i])
            for j in range(i + 1, len(s)):
                if s[j] not in s[i:j]:
                    targets[i].append(s[j])
                else:
                    break

        lengths = [len(target) for target in targets]
        return max(lengths)
