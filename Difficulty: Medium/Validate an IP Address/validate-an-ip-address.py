#User function Template for python3
class Solution:
    def isValid(self, s):
        parts = s.split(".")
        
        if len(parts) != 4:
            return False
        
        for part in parts:
            if not part.isdigit():
                return False
            num = int(part)
            if num < 0 or num > 255:
                return False 
            if part != "0" and part[0] == "0":
                return False
                
        return True
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends