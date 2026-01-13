class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        longest = s[0]
        
        for i in range(len(s)):
            h = i - 1
            j = i + 1
            current = s[i]
            
            while h >= 0 and j < len(s) and s[h] == s[j]:
                current = s[h] + current + s[j]
                h -= 1
                j += 1
            
            if len(current) > len(longest):
                longest = current
            
            h = i
            j = i + 1
            
            if j < len(s) and s[h] == s[j]:
                current = s[h] + s[j]
                
                h -= 1
                j += 1
                
                while h >= 0 and j < len(s) and s[h] == s[j]:
                    current = s[h] + current + s[j]
                    h -= 1
                    j += 1
                
                if len(current) > len(longest):
                    longest = current

        return longest

# Example usage:
solution = Solution()
print(solution.longestPalindrome("abbcccba"))  # Output: "bab" or "aba
                

                

                


                
            
                

        