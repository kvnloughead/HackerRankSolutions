def left_rotate(arr):
    """Left rotates array in place.  
    Ex:  [1, 2, 3, 4, 5] -> [2, 3, 4, 5, 1]"""
    return arr[1:] + [arr[0]]

print(left_rotate([1,2,3,4,5]))