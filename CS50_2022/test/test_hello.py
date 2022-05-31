from hello import hello 


def test_default():
    assert hello("Andrew") == "Hello, Andrew"
  

def test_argument():
    assert hello() == "Hello, world"