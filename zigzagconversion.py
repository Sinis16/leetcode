class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lists = [[] for _ in range(numRows)]
        i = j = 0

        while i < len(s):
            # Columns
            while j < numRows and i < len(s):
                lists[j].append(s[i])
                j += 1
                i += 1
            j = numRows - 2
            print(lists[j])
            
            # Diagonals
            while j > 0 and i < len(s):
                lists[j].append(s[i])
                j -= 1
                i += 1
            j = 0
        print(lists)
        res = "".join(
        item
        for sublist in lists
        for item in sublist
        )

        return res


# Example usage:
solution = Solution()
print(solution.convert("ABCD", 3))  # Output: "PAHNAPLSIIGYIR"