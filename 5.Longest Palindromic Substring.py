class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=''
        for i in range(len(s)):
            for j in range(i,len(s)):
                s1=s[i:j+1]

                if s1==s1[::-1] and len(s1)>len(n):
                    n=s1
        return n
        