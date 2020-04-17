from collections import defaultdict


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxik = 0
        counter = 0
        distances = dict()
        distances[0] = [0, None]
        for x in range(0, len(nums)):
            counter += 1 if nums[x] == 1 else -1
            if distances.get(counter):
                distances[counter][1] = x + 1
            else:
                distances[counter] = [x + 1, None]
        for _, v in distances.items():
            if v[1]:
                dist = v[1] - v[0]
                if dist > maxik:
                    maxik = dist
        return maxik



