'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

''' FIRST PASS SOLUTION
def single_number(arr):
    # Your code here
    arr2 = []
    #loop through array appending all values into arr2 
    # and then removing it if it is seen twice
    for i in arr:
        if i not in arr2:
            arr2.append(i)
        else:
            arr2.remove(i)
    return arr2[0]
'''
#BETTER SOLUTION
def single_number(arr):
    # Your code here
    counts = {}
    #loop through array appending all values into arr2 
    # and then removing it if it is seen twice
    for i in arr: # O(n)
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1
    for k,v in counts.items(): #O(n)
        if v ==1:
            return k



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")