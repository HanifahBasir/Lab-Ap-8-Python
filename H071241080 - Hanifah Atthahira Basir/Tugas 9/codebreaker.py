from mathoperations import MathOperations

class CodeBreaker:
    def __init__(self, secret_code):
        try:
            self.code = secret_code
            self.math_ops = MathOperations() # menambahkan fungsi
        except Exception as e:
            print(f"Error initializing CodeBreaker: {e}")

    def break_code(self):
        try:
            code = self.code.get_code() # kode rahasia
            step_1 = self.math_ops.factorial(code % 10) #modulus 10 untuk mengambil digit terakhir
            step_2 = self.math_ops.digit_sum(step_1) # jumlah digit
            step_3 = (step_2 * code) % 1000 # mengambil 3 digit terakhir 
            return step_3 # mengembalikan hasil
        except Exception as e:
            print(f"Error breaking code: {e}")
            return None
