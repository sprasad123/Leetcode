class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        number = n
        while True:
            sum_of_squares = 0
            for digit in str(number):
                sum_of_squares += int(digit) ** 2
            if sum_of_squares == 1:
                return True
            if sum_of_squares in seen:
                break
            seen.add(sum_of_squares)
            number = sum_of_squares
        return False
            
            
        