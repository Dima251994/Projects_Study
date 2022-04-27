
def same_case(a, b): 
    """take two arguments
       check types and case
       return result of checking"""
    if (type(a) is int) and (type(b) is int):
        return "Numbers"
    elif (type(a) is int) or (type(b) is int):
        return "Numbers and string"
    elif a == b:
        return "Same"
    elif not a.isalpha() or not b.isalpha():
        return "Symbol"
    elif a.islower() and b.islower():
        return "Lower"
    elif a.isupper() and b.isupper():
        return "Upper"
    else:
        return "Different"