#User function Template for python3

class Solution:
    def rotate(self, arr):
        last_ele = arr.pop()
        arr.insert(0,last_ele)
        return arr
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.rotate(arr)
        print(" ".join(map(str, arr)))
        print("~")
        t -= 1

# } Driver Code Ends