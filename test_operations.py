from operations import adder
def test_hello():
    print("Hello test tested")

def test_adder():
    '''
    Tests addition of two numbers
    '''
    assert adder(50,50) == 103, "Your Add function is incorrect"

