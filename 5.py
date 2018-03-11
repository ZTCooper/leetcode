class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""
        if (len(s) == 1) or (s == s[::-1]):
            return s
        
        targets = []
        for i in range(len(s)):
            for j in range(len(s), i+1, -1):
                if s[i:j] == s[i:j][::-1]:
                    targets.append(s[i:j])
                else:
                    continue
        try:            
            lengths = [len(target) for target in targets]
            ind = lengths.index(max(lengths))
            return targets[ind]
        except ValueError:
            return s[0]
