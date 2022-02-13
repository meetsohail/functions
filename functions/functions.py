
from classes.formula import Formula
from classes.basic_maths import Basicmaths
from classes.python_function import Pythonfunctions

class Functions(Formula, Basicmaths, Pythonfunctions):
    
    def __ini__(self):
        pass
    
    def integer_error(self):
        return "Both values must be integer"
    
    def is_integer(self,a,b):
        if isinstance(a, int) and isinstance(b, int):
            return True
        return False
    
    
    
if __name__ == "__main__":
    f = Functions()
    print(f.is_list({3,3}))