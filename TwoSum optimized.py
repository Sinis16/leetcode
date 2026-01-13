class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydickt={}
        for i in range(len(nums)):
            remain=target-nums[i]
            if remain in mydickt:
                return mydickt[remain],i
            mydickt[nums[i]]=i

# Example usage:
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]

