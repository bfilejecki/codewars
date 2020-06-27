#Ones and Zeros
#Given an array of ones and zeroes, convert the equivalent binary value to an integer.

def binary_array_to_number(arr):
    arr.reverse()
    return sum(2**i if x == 1 else 0 for i, x in enumerate(arr))

print(binary_array_to_number([1,1,1,1]))