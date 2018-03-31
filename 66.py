class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return list(map(int, [i for i in str(int("".join(map(str, digits))) + 1)]))
        