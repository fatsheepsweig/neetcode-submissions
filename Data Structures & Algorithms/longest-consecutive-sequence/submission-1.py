class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        contains = s.__contains__

        best = 0
        for x in s:
            if contains(x - 1):
                continue  # not a start

            y = x + 1
            while contains(y):
                y += 1

            # streak length = y - x
            if y - x > best:
                best = y - x

        return best