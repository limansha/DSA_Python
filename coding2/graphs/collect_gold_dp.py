# User function Template for Python3

class Solution:
    def maxGold(self, n, m, M):
        dp = [[0]*m for _ in range(n)]
        #dp represent the mains number of coins 
        # you can collect "starting" from i,j
        #print(dp)
        #base condition
        for i in range(0,n): #last column  will have same values
            dp[i][m-1] = M[i][m-1]
        #print(dp)
        maxc = 0
        for j in range(m-2,-1,-1): #thrid -1 moves 1 value  and second -1 will say start from backward
            for i in range(n):
                if(j + 1 < m):
                    dp[i][j] = max(dp[i][j],dp[i][j+1])
                    if(i-1 >= 0):
                        dp[i][j] = max(dp[i][j],dp[i-1][j+1])
                    if(i + 1 < n):
                        dp[i][j] = max(dp[i][j],dp[i+1][j+1])
                dp[i][j] += M[i][j]
            #print(dp)

        #print("###################")    
        #print(dp)
        for i in range(0,n):
            maxc = max(maxc,dp[i][0])

        return maxc
        
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