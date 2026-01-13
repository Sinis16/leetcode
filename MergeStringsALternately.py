class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        w1l = len(word1)
        w2l = len(word2)
        minLength = min(w1l, w2l)

        while minLength:
            minLength -= 1
            result = result + word1[0] + word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
        return result + word1 + word2
        
sol = Solution()
print(sol.mergeAlternately("abc", "pqraaa"))  # Output: "apbqcr"