class Solution(object):
    
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        my_list = []
        for i in range(n):
            val = i + 1
            if val%3 == 0 and val%5 == 0:
                val = "FizzBuzz"
            elif (val%3 == 0 and val%5 != 0):
                val = "Fizz"
            elif (val%3 != 0 and val%5 == 0):
                val = "Buzz"
            my_list.append(val)
        return my_list

d = Solution()
print(d.fizzBuzz(15))