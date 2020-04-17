class Solution:
    def isHappy(self, n: int) -> bool:
        previous = []
        while True:
            sum = 0
            for digit in str(n):
                sum += pow(int(digit), 2)
            if sum in previous:
                return False
            if sum == 1:
                return True
            previous.append(sum)
            n = sum
