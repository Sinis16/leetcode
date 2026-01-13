class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = nums.__len__()
        for i in range(l):
            for j in range(i+1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Example usage:
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]

