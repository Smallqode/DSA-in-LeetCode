class Solution:
    def maximum69Number (self, num: int) -> int:
        length = math.floor(math.log10(num)) + 1
        for n in range(length):
            digit = (num // 10**(length - n - 1)) % 10
            if digit == 6:
                num += 3 * (10**(length - n - 1))
                break
        return num
