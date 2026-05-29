class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while True:  # exactly one solution guaranteed
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]   # 1-indexed
            if s < target:
                l += 1
            else:
                r -= 1