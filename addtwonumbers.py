class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nl1 = int(''.join(map(str, l1)))
        nl2 = int(''.join(map(str, l2)))
        n = nl1+nl2
        s = str(n)
        return [int(ch) for ch in s]

# Example usage:
sol = Solution()
print(sol.addTwoNumbers([2,4,3], [5,6,4]))  # Output: [7,0,8]