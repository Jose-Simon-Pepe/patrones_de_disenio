"""
factory method

Create subclasses via different procediments, using a same interface
this pattern returns 'products'
"""

class PRODUCT:
    """
    This is the Product interfacte the factory method interacts with
    Into the example, this'd be called as "Operator"
    """
    def calculate(self):
        pass


class CREATOR:
    """
    This is the Factory Class with 'make product' method
    In the standard, it's known as 'CREATOR' interface

    it's also responsible for some busineess logic
    """

    def make_product(self,attribute1=None) -> PRODUCT:
        pass

    def calculate(self):
        """
        this is a method which will use product interface
        It also can be overwritten by concrete creators
        """
        return self.make_product().calculate()

class Duplicator(PRODUCT):
    """
    This is an Operator
    This is the Multiplier one
    """

    def __init__(self, attribute1, attribute2,number_to_calculate:int):
        self._attribute1 = attribute1
        self._attribute2 = attribute2
        self._number_to_calculate = number_to_calculate


    def calculate(self):
        return 2*self._number_to_calculate

    #own methods
        
class Adder(PRODUCT):
    """
    This is another Operator
    This is the Plus one
    """

    def __init__(self, number_to_calculate1, number_to_calculate2:str):
        self._add1 = number_to_calculate1
        self._add2 = number_to_calculate2

    def calculate(self):
        return self._add1+self._add2

    #own methods


class DuplicatorFactory(CREATOR):

    def __init__(self,number_to_calculate:int,attribute1,attribute2):
        super().__init__()
        self._number_to_calculate = number_to_calculate
        self._attribute1 = attribute1
        self._attribute2 = attribute2

    
    def make_product(self) -> PRODUCT:
        """
        The factory method
        Method is overwritten to return different object type
        Method signature is the original, product's dependencies are injected trhought concrete creator constructor
        """
        return Duplicator(self._attribute1, self._attribute2, self._number_to_calculate)



class AdderFactory(CREATOR):

    def __init__(self,attribute1,number_to_calculate:int):
        super().__init__()
        self._attribute1 = attribute1
        self._number_to_calculate = number_to_calculate

    
    def make_product(self) -> PRODUCT:
        """
        The factory method
        Method is overwritten to return different object type
        Method signature is the original, product's dependencies are injected trhought concrete creator constructor
        """
        return Adder(self._attribute1, self._number_to_calculate)


