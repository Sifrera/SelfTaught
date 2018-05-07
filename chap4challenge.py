def sqrnum(x):
    """
    Squares x
    :param x: int.
    :return: int square of x.
    """
    return x ** 2

def printstring(word):
    """
    Prints string
    :param word: str.
    """
    print(word)

def multiparam(x, y, z, a = 0, b = 1):
    """
    Returns nothing after recieving variables
    :param x: int.
    :param y: int.
    :param z: int.
    :param a: int.
    :param b: int.
    :return: none.
    """
    return None

def makefloat(var):
    """
    Converts from str to float
    :param var: str.
    :return: string converted to float.
    """
    try:
        return float(var)
    except ValueError:
        print("Must be a number.")


        
