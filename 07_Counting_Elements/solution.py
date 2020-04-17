class Solution:
    def countElements(self, arr: List[int]) -> int:
        return sum([1 for elem in arr if elem + 1 in arr])
