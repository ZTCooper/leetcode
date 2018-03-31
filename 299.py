class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s, g = collections.Counter(secret), collections.Counter(guess)
        a = sum(i == j for i, j in zip(secret, guess))
        b = sum((s & g).values()) - a
        return "%dA%dB" % (a, b)
