'''
Input: a List of integers
Returns: a List of integers
'''
''' FIRST PASS SOLUTION
def moving_zeroes(arr):
    # Your code here

    #grab from array a new array of zero integers
    zarr = [i for i in arr if i is 0]
    #create an array of the non zero
    arr = [i for i in arr if i is not 0]
    # append zero array to non-zero array
    arr = arr + zarr


    return arr
'''
#improved
def moving_zeroes(arr):
    # Your code here
    # create a left and right pointer
    left = 0
    right = len(arr) - 1
    #left is first index in arr and right is last index in arr

    # while left <= right:
    while left != right:
        #if left is 0 and right is not 0:
            if arr[left] == 0:
            #swap 
                arr[left],arr[right] = arr[right],arr[left]
            #decrement right index
                right -= 1
            #if left is not 0, increment left
            elif arr[left] != 0:
                left += 1


    return arr
    



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 2, 3, 0, 4, 0, 0]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")