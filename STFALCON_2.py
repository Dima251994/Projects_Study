list_of_sheeps = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
def count_sheeps(sheep):
    counter = 0
    for one_sheep in sheep:
        if one_sheep == True:
            counter += 1
    return counter

print(count_sheeps(list_of_sheeps))






