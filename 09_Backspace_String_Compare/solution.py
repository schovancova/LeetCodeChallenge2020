class Solution:
    def getResult(self, s: str) -> str:
        leng = len(s)
        i = 0
        while i < leng:
            if s[i] == '#':
                if i == 0:
                    s = s[1:]
                    leng -= 1
                else:
                    s = s[:i - 1] + s[(i + 1):]
                    i -= 1
                    leng -= 2
            else:
                i += 1
        return s

    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.getResult(S) == self.getResult(T)
