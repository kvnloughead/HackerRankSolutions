def swap(idx1, idx2, array):
    arr = list(array)
    arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
    return arr

def minimumSwaps(arr):
    """Returns minimum number of swaps required to sort arr."""
    arr = list(arr)
    swaps = 0
    for i, a in enumerate(arr):
        
        print("Round")
        print("array:", arr)
        print(i+1, a)
        print("num swaps", swaps)
        if arr[i] == i+1:
            pass
        
        elif arr[i] != i+1:

            swaps += 1
            arr = swap(i, a-1, arr)
                       
    return swaps, arr
        

arrays = [
    [7,1,3,2,4,5,6],
    [4,3,1,2]
]

for array in arrays:
    print(minimumSwaps(array))
