class Pythonfunctions:
    
    def is_dict(self, variable):
        if isinstance(variable, dict):
            return True
        return False
    
    def is_list(self, variable):
        if isinstance(variable, list):
            return True
        return False
    
    def is_tuple(self, variable):
        if isinstance(variable, tuple):
            return True
        return False
    
    def is_set(self, variable):
        if isinstance(variable, set):
            return True
        return False