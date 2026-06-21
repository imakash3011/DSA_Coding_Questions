def all_subsequences(arr, n, curr_sub_seq):
    if n==len(arr):
        print(curr_sub_seq)
        return
    curr_sub_seq.append(arr[n])
    all_subsequences(arr, n+1, curr_sub_seq)
    curr_sub_seq.pop()
    all_subsequences(arr, n+1,curr_sub_seq)

  
arr = [1,2,3]
all_subsequences(arr, 0 , [])




def all_subsequences_iterative(arr):
    # Start with the base empty subset
    subsequences = [[]]
    
    # Process each element one by one
    for num in arr:
        # Take a snapshot of the subsets we have built so far
        current_size = len(subsequences)
        
        # Add the current number to all existing subsets
        for i in range(current_size):
            # Create a new subset by adding 'num' to the existing subset
            new_subset = subsequences[i] + [num]
            subsequences.append(new_subset)
            
    # Print the final results
    for sub in subsequences:
        print(sub)

# Driver Code
arr = [1, 2, 3]
print("All subsequences without bit manipulation:")
all_subsequences_iterative(arr)




def all_subsequences_powerset(arr):
    n = len(arr)
    # Total number of subsets is 2^n
    total_subsets = 1 << n  # Equivalent to 2^n

    # Run a loop from 0 to 2^n - 1
    for i in range(total_subsets):
        current_subsequence = []
        
        # Check every bit of the number 'i'
        for j in range(n):
            # If the j-th bit of 'i' is set (1), include arr[j]
            if (i & (1 << j)) > 0:
                current_subsequence.append(arr[j])
                
        print(current_subsequence)

# Driver Code
arr = [1, 2, 3]
print("All subsequences using Power Set:")
all_subsequences_powerset(arr)