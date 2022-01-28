# return the minimum value from a 2d list using recursion



def min_2d(arr, i1, i2, min_val): # i1, i2 are the indices of the 2d list

    if i2 == len(arr[i1]): # if we've reached the end of the nested list

        if i1 == len(arr) - 1: # if we've reached the end of the main list

            return min_val # return the minimum value

        return min_2d(arr, i1 + 1, 0, min_val) # recurse to the next nested list

    else:
        if arr[i1][i2] < min_val: # if the current value is less than the current minimum value

            min_val = arr[i1][i2] # set the minimum value to the current value

        return min_2d(arr, i1, i2+1, min_val) # recurse to the next value in the nested list

if __name__ == '__main__':
    arr = [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12]]

    min_val = min_2d(arr, 0, 0, arr[0][0])
    print(min_val)











