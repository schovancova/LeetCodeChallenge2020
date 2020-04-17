class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while True:
            stones.sort()
            try:
                last = stones[-1]
                pre_last = stones[-2]
            except IndexError:
                try:
                    return stones[0]
                except IndexError:
                    return 0
            res = last - pre_last
            if not res:
                del stones[-2]
                del stones[-1]
            elif res > 0:
                del stones[-2]
                stones[-1]  = res
            else:
                del stones[-1]
                stones[-1] = res