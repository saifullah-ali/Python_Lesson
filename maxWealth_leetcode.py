class Solution():
    def __init__(self,val):
        self.val = val
        
    def maximumWealth(self, accounts):
        
        for i in accounts:
            y = self.val
            print(sum(i))
            for x in i:
                y = y + x
                print(f'cumulitive adding {y}')



accounts = [[1,2,3],[3,2,1]]


r = Solution(5)
r.maximumWealth(accounts)

d = Solution(0)
d.maximumWealth(accounts)