class MathOperations:
    def factorial(self, n):
        if n == 0 or n == 1: # jika n adalah 0 atau 1
            return 1
        else:
            return n * self.factorial(n - 1) # faktorial

    def digit_sum(self, n): # menghitung jumlah setiap digit
        return sum(int(digit) for digit in str(n))
