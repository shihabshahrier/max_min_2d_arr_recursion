# return the maximum value from a 2d list using recursion




def max_2d(arr, i1, i2, max_val): # i1, i2 are the indices of the 2d list

    if i2 == len(arr[i1]): # if we've reached the end of the nested list

        if i1 == len(arr) - 1: # if we've reached the end of the main list

            return max_val # return the max value

        return max_2d(arr, i1 + 1, 0, max_val) # recurse to the next nested list

    else:
        if arr[i1][i2] > max_val: # if the current value is greater than the max value

            max_val = arr[i1][i2] # update the max value

        return max_2d(arr, i1, i2+1, max_val) # recurse to the next value in the nested list

if __name__ == '__main__':
    arr = [[1,2,3,4],
            [5,6,7,8],
            [9,12,11,10]]
    max_val = max_2d( arr, 0, 0, 0) # call the function
    print(max_val)  # should print 12











