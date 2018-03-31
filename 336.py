# https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation


class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def is_palindrome(s):
            return s == s[::-1]
        # Creat a dict {word: index}
        words = {word: i for i, word in enumerate(words)}
        result = []
        for word, i in words.items():
            for j in range(len(word)):
                preffix = word[:j]
                suffix = word[j:]
                if is_palindrome(preffix):
                    back = suffix[::-1]
                    if back != word and back in words:
                        result.append([words[back], i])
                if is_palindrome(suffix):
                    back = preffix[::-1]
                    if back != word and back in words:
                        result.append([i, words[back]])
        return result
