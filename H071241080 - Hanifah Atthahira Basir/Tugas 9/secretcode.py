class SecretCode:
    def __init__(self, initial_code): # menambahkan konstruktor
        self.code = initial_code

    def get_code(self): # mengambil kode
        try:
            return self.code
        except Exception as e:
            print(f"Error getting code: {e}")
            return None

    def set_code(self, new_code): # mengubah kode
        try:
            self.code = new_code
        except Exception as e:
            print(f"Error setting code: {e}")
            