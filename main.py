def merged_sort(arr):
    
    #What does it need to be greater than to complete it
    if len(arr) > 1:
        #Both sides of the array need declaring
        left_arr = arr[:len(arr) //2]
        right_arr = arr[len(arr) //2:]
        
        #run the algo on the arrays
        merged_sort(left_arr)
        merged_sort(right_arr)
        
        #declare starting point for the indexes
        i = 0
        j = 0
        k = 0
        
        # compare the left to the right
        while i < len(left_arr) and j < len(right_arr):
            #What do we do if it's bigger
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            #what do we do if its not bigger
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        #If everything from the right array is gone, we need to consider moving all the left array stuff
        # what's it less than, assign the arry to left array
        #Don't forget to increment indexes
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        
        #What happenes if we're not at the end of the right array, ou need to assign it to the merged array
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    
    
arr_test = [1,5,3,5,8,2,10]
merged_sort(arr_test)
print(arr_test)