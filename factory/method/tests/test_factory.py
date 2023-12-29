from provider.factorymethod import *
"""
factory method 

Create subclasses via different procediments, using a same interface
this pattern returns 'products'

the client or consumer just only has to use creator interface to acceed product's interface!
"""
def test_multiplier_should_return_a_product():
    factory = DuplicatorFactory(12,"stub","stub")
    product = factory.make_product()
    assert issubclass(product.__class__,PRODUCT)
    assert product.calculate() == 24


def test_adder_should_return_a_product():
    factory = AdderFactory(142, 124)
    product = factory.make_product()
    assert issubclass(product.__class__,PRODUCT)
    assert product.calculate() == 266


