class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        b=bin(n)[2:]
        c="".join('1'if bit =='0' else '0' for bit in b)
        return int(c,2)

        