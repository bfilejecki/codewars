def comp(array1, array2):
    if (array1 is None and array2 is not None) or (array1 is not None and array2 is None):
        return False
    if len(array1) != len(array2):
        return False
    for num in array1:
        try:
            array2.remove(num**2)
        except:
            return False
    return True if len(array2) == 0 else False

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

print(comp(a1,a2))