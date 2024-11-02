def find_median_merged_array(merged_array):
    # Sort the merged array
    sorted_array = merge_sort_arrays([], merged_array)
    
    # Calculate the median of the array
    n = len(sorted_array)
    if n % 2 == 0:
        mid1 = sorted_array[n // 2 - 1]
        mid2 = sorted_array[n // 2]
        median = (mid1 + mid2) / 2
    else:
        median = sorted_array[n // 2]
    
    return median

# Example usage:
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]

merged_array = merge_sort_arrays(arr1, arr2)
print("Merged array:", merged_array)

median_result = find_median_merged_array(merged_array)
print("Median of the merged array:", median_result)