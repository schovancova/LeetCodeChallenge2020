class Solution:
    def curb_shift(self, shift, ln):
        while shift > ln:
            shift -= ln
        return shift

    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_shift = 0
        for shif in shift:
            total_shift += shif[1] if shif[0] == 0 else -shif[1]
        l = list(s)
        # we go right
        if total_shift < 0:
            total_shift = self.curb_shift(total_shift * -1, len(s))
            result = ''.join(l[-total_shift:] + l[:-total_shift])
        elif total_shift > 0:
            total_shift = self.curb_shift(total_shift, len(s))
            result = ''.join(l[total_shift:] + l[:total_shift])
        else:
            return s
        return result
