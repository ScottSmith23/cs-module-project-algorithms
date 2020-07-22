'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here

    #array of zero integers
    zarr = [i for i in arr if i is 0]
    #array of non zero
    arr = [i for i in arr if i is not 0]
  
    arr = arr + zarr


    return arr

    



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")