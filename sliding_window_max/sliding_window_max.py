'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    mults = len(nums) - k + 1
    windarr = []
    triparr = []
    for i in range(0,mults):
        triparr = nums[i:k+i]
        triparr.sort()
        windarr.append(triparr[-1])
    
    return windarr

        




if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
