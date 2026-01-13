class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        mres = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                mres.append(nums1[i])
                i += 1 
            else:
                mres.append(nums2[j])
                j += 1

        mres.extend(nums1[i:])
        mres.extend(nums2[j:])

        n = len(mres)

        if n%2 == 0:
            return (mres[n//2-1] + mres[n//2])/2
        else:
            return mres[n//2]

sol = Solution()
print(sol.findMedianSortedArrays([1, 3, 6], [2]))  # Output: 2.0