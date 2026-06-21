def main_function(nums):
    result = []  # Initialize the results container inside
    
    def print_all_subsequences(index, subset):
        if index >= len(nums):
            result.append(subset.copy())
            return
        
        # Pick the current element
        subset.append(nums[index])
        print_all_subsequences(index + 1, subset)
        
        # Backtrack: Un-pick the current element
        subset.pop()
        print_all_subsequences(index + 1, subset)
        
    # CRITICAL FIX: You must actually trigger the initial call!
    print_all_subsequences(0, [])
    
    # CRITICAL FIX: Return the populated results list
    return result

# Test code
nums = [5,9,7]  # Shortened to 3 elements so it's easy to read the output
print(main_function(nums))
