class Solution:
    def checkValidString(self, s: str) -> bool:
        leftBalance = rightBalance = 0
        n = len(s)
        for i in range(n):
            if s[i] in "(*":
                leftBalance += 1
            else:
                leftBalance -= 1
            if s[n - i - 1] in "*)":
                rightBalance += 1
            else:
                rightBalance -= 1
            if leftBalance < 0 or rightBalance < 0:
                return False
        return True





