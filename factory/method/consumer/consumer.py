from provider.factorymethod import *


def client(creator:CREATOR):
    print("I'm a math nerd and i need to make maths now!")
    product = creator.calculate()
    print(product)

if __name__ == "__main__":
    """
    Factory method client
    I just has to use Creator interface to use product's one.
    Let's say i'm being using both, by di

    Main'd be ussefull to inject dependency
    """
    client(AdderFactory(124, 345))

