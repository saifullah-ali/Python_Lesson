import time
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        sol_civ_dict = {}
        row_num = 0
        print(mat)
        for i in mat:
            sol = 0
            
            for t in i:
                if t == 1:
                    sol = sol+1
                
            sol_civ_dict[row_num] = sol
            row_num = row_num + 1
        

        res = []
        sorted_dict = dict(sorted(sol_civ_dict.items(), key=lambda item: item[1]))
        
        slice_count = 0
        for n in sorted_dict:
            slice_count = slice_count + 1
            res.append(n)
            if slice_count == k:
                break
        #print(res)





#time.sleep(4)






d = Solution()
mat = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
d.kWeakestRows(mat,2)


x=[i for i in range(5,1,-1)]


print(x)

y = x[0:2]

print(y)

z = "kooping"

z = z.replace("k","l")

print(z)