# User function Template for Python3

class Solution:
    def maxGold(self, n, m, M):
        dp = [[0]*n for _ in range(m)]
        
        #base condition
        res = 0
        maxc = 0
        for i in range(0,n): #for each row
            temp = self.collectGold(M,i,0,0,n,m)
            maxc = max(temp,maxc)
            print(f"at row pos {i} temp is {temp} res is {maxc}")
            
        return maxc
    
    def collectGold(self,M,x,y,res,n,m):
        if (self.isValidPos(x,y,n,m)):
            temp = max(
                self.collectGold(M,x,y+1,res,n,m),
                self.collectGold(M,x+1,y+1,res,n,m),
                self.collectGold(M,x-1,y+1,res,n,m)
                )
            
            res = M[x][y] + max(temp, res)
            print(f"x : {x} y : {y} current res :{res} temp : {temp} value at M : {M[x][y]}")
            
        return res
    
    
    def isValidPos(self,x,y,n,m):
        if((0 <= x and x < n) and (0 <= y and y < m)):
            return True
        else:
            return False
    

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        tarr = [int(x) for x in input().split()]
        M = []
        j = 0
        for i in range (n):
            M.append(tarr[j:j + m])
            j = j+m
        
        ob = Solution()
        print(ob.maxGold(n, m, M))
# } Driver Code Ends