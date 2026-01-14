class Solution:
    def reverse(self, x: int) -> int:
        xList = list(str(x))
        i = len(xList) - 1
        res = ""
        neg = ""
        if xList[0] == "-":
            neg = "-"
            del xList[0]

        while len(xList) > 0:
            res = res + xList.pop()
        
        
        if (res != "0"):
            res = neg + res
        resint = int(res)
        if ((resint > 2147483647) or (resint < -2147483647)):
            resint = 0
        return resint
    
    def reverse2(self, x: int) -> int:
        neg = False

        if x < 0:
            neg = True
            x = -x
        
        res = 0
        while x > 0:
            res = (res * 10) + (x % 10)
            x //= 10
        
        if res > 2**32 - 1:
            return 0

        return res * -1 if is_negative else res
    
# Example usage:
solution = Solution()
print(solution.reverse2(-123))  # Output: -321
