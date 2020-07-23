'''
Input: a List of integers
Returns: a List of integers
'''
import time

def product_of_all_other_numbers(arr):
    # Your code here
    product = 1
    prodarray = []
    cur = 0
    
    while cur != len(arr):
        newArr = arr[:cur]+arr[cur+1:]
        for b in newArr:
            product = product * b

        prodarray.append(product)
        product = 1    
        cur += 1


    return prodarray
        



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [70, 37, 100, 66, 1, 45, 27, 62, 75, 57, 92, 66, 9, 39, 15, 69, 46, 72, 35, 68, 54, 51, 35, 36, 13, 27, 27, 24, 6, 33, 83, 97, 55, 5, 25, 85, 56, 4, 100, 38, 38, 83, 29, 1, 11, 27, 64, 99, 64, 29, 41, 95, 59, 46, 75, 67, 40, 49, 62, 30, 56, 88, 71, 77, 43, 79, 27, 65, 24, 18, 74, 50, 23, 47, 45, 60, 62, 84, 53, 2, 90, 29, 99, 75, 59, 44, 71, 7, 59, 59, 27, 72, 6, 89, 90, 40, 51, 45, 43, 86, 37, 100, 66, 1, 45, 27, 62, 75, 57, 92, 66, 9, 39, 15, 69, 46, 72, 35, 68, 54, 51, 35, 36, 13, 27, 27, 24, 6, 33, 83, 97, 55, 5, 25, 85, 56, 4, 100, 38, 38, 83, 29, 1, 11, 27, 64, 99, 64, 29, 41, 95, 59, 46, 75, 67, 40, 49, 62, 30, 56, 88, 71, 77, 43, 79, 27, 65, 24, 18, 74, 50, 23, 47, 45, 60, 62, 84, 53, 2, 90, 29, 99, 75, 59, 44, 71, 7, 59, 59, 27, 72, 6, 89, 90, 40, 51, 45, 43, 86]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]
    # arr = [7, 9, 1, 8, 6, 7, 8, 8, 7, 10]
    start_time = time.time()
    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
    end_time = time.time()
    print(f"TIME IT TOOK: {end_time - start_time}s")