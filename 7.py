class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < -2**31 or x > 2**31 - 1:
            return 0
        if x == 0:
            return 0
        buff = []
        x = str(x)
        if x.startswith("-"):
            buff.append("-")
        buff.extend(list(reversed(x.lstrip("-").rstrip("0"))))
        result = ""
        for i in buff:
            result += i
        if int(result) < -2**31 or int(result) > 2**31 - 1:
            return 0
        return int(result)
