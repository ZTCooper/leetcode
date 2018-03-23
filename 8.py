'''
32位整数范围-2 ** 31 ~ 2 ** 31-1
'''
class Solution:
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0

        count = 0
        for i in s:
            count += i == "+" or i == "-"
        if count > 1:
            return 0

        num, flag = 0, 1
        if s.startswith("-"):
            flag = -1
            s = s[1:]
        if s.startswith("+"):
            s = s[1:]
        for i in s:
            if i >= "0" and i <= "9":
                num = num * 10 + ord(i) - ord("0")
            else:
                break
        num = flag * num
        num = num if num <= 2 ** 31 - 1 else 2 ** 31 - 1
        num = num if num >= -2 ** 31 else -2 ** 31
        return num


s = Solution()
print(s.myAtoi("2147483648"))
