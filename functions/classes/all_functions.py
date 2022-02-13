from ast import For
from classes.formula import Formula
from classes.basic_maths import Basicmaths
from classes.python_function import Pythonfunctions

class Allfunctions(Formula, Basicmaths, Pythonfunctions):
    def integer_error(self):
        return "Both values must be integer"
    
    def is_integer(self,a,b):
        if isinstance(a, int) and isinstance(b, int):
            return True
        return False