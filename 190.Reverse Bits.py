class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        b=bin(n)[2:].zfill(32)
        r=b[::-1]
        return int(r,2)