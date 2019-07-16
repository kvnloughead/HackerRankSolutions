def left_rotate(arr):
    """Left rotates array in place.  
    Ex:  [1, 2, 3, 4, 5] -> [2, 3, 4, 5, 1]"""
    return arr[1:] + [arr[0]]

def rotLeft(a, d):
    """Rotates array a left d times."""
    for i in range(d):
        arr = left_rotate(arr)
    return arr

