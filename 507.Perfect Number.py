class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<6:
            return False
        limit=int(num**0.5)
        sum=1
        for i in range(2,limit +1):
            if num%i==0:
                sum+=i
                if i*i!=num:
                    sum+=num//i
            if sum>num:
                return False
        return num==sum
        
