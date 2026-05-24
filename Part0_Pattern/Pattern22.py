# ## Pyramid

class Solution:
    def pattern2(self, n): 
        # size represents the total width/height of the matrix (e.g., 5 for n=3)
        size = 2 * n - 1
        
        for i in range(size):
            for j in range(size):
                # Your logic checked for the outermost layer (layer 0):
                # i == 0 or i == size - 1 or j == 0 or j == size - 1
                
                # To make it work for ALL layers, we find which layer layer we are on.
                # We calculate the distance from the 4 edges:
                layer_i = min(i, size - 1 - i)
                layer_j = min(j, size - 1 - j)
                
                # The actual layer number is the smaller of the two
                current_layer = min(layer_i, layer_j)
                
                # Instead of printing a hardcoded n-1, 
                # we subtract the current layer depth from n
                print(n - current_layer, end=" ")
            print()

c1 = Solution()
c1.pattern2(4)



# class Solution:
#     def pattern2(self, n):
#         size = 2 * n - 1
#         for i in range(size):
#             # Calculate the value for every cell in the row instantly
#             row = [str(n - min(i, j, size - 1 - i, size - 1 - j)) for j in range(size)]
#             print(" ".join(row))

# c1 = Solution()
# c1.pattern2(3)






# class Solution:
#     def pattern2(self, n):
#         for i in range(1, n+1):
#             for j in range(1, i+1):
#                 print(j, end="")

#             print("  "*(n-i), end="")

#             for j in range(1, i+1):
#                 print(j, end="")
#             print()

# c1 = Solution()
# c1.pattern2(4)
