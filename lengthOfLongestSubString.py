class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        currentS = ""
        currentl = 0
        longest = 0
        for i in range(l):
            currentS = currentS + s[i]
            if currentS.count(s[i]) > 1:
                
                currentS = currentS[1:]

            print(s[i])
            print(currentS)
            print(len(currentS))    
            print("---")
        return len(currentS)
        
        
# Example usage:
sol = Solution()
print(sol.lengthOfLongestSubstring("pwwkew"))  # Output: 3