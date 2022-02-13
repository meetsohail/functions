
class Basicmaths:
    
    def add(self, a, b):
        if self.is_integer(a,b):
            return a+b
        return self.integer_error()

    def subtract(self, a, b):
        if self.is_integer(a,b):
            return a-b
        return self.integer_error()

    def mutiply(self, a, b):
        if self.is_integer(a,b):
            return a*b
        return self.integer_error()

    def division(self, a, b):
        if self.is_integer(a,b):
            try:
                return a/b
            except ZeroDivisionError:
                return "Not allowed to divide by zero."
        return self.integer_error()
    
    def modulus(self, a, b):
        if self.is_integer(a,b):
            try:
                return a%b
            except ZeroDivisionError:
                return "Zero not allowed"
        return self.integer_error()
    
    def exponentiation(self, a, b):
        if self.is_integer(a,b):
            return a**b
        return self.integer_error()
    
    def floor_division(self, a, b):
        if self.is_integer(a,b):
            try:
                return a//b
            except ZeroDivisionError:
                return "Zero not allowed"
        return self.integer_error()
    