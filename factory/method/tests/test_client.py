from provider.factorymethod import *

def client(creator:CREATOR):
    print("I'm a math nerd and i need to make maths now!")
    product = creator.calculate()
    return product

def test_client_should_obtain_calcule():
    product1 = client(AdderFactory(124, 345))
    assert product1 == 469
    product2 = client(DuplicatorFactory(124, "stub", "stub"))
    assert product2 == 248


