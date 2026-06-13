
'''https://takeuforward.org/plus/dsa/problems/aggressive-cows?source=strivers-a2z-dsa-track'''


################## BINARY SEARCH APPROACH ####################

def aggressive_cows_binary(stalls: list[int], cows: int) -> int:
    stalls.sort()
    low = 1      ## Here low as 1 because we are denoting distance range from 1 to high (we can't start from 0). we are giving here the possible range of value
    high = stalls[-1] - stalls[0]   ## 
    best_dist = -1

    while low <= high:
        # Formula prevents potential integer overflow (useful to keep in mind across languages)
        mid = low + (high - low) // 2

        if can_we_place(stalls, mid, cows):  ## If current distance is valid then lets move forward and check for other greater distance
            # mid is valid, record it as a potential answer
            best_dist = mid
            # Shift the lower boundary up to search for an even larger valid distance
            low = mid + 1
        else:
            # mid is invalid (we couldn't fit the cows), shrink the upper boundary down
            high = mid - 1

    # Note: When the loop terminates, 'high' also points to the maximum possible distance.
    return best_dist

 
##################### LINEAR APPROACH################
def aggressive_cows_linear(stalls: list[int], cows: int) -> int:
    stalls.sort()
    max_dist = stalls[-1] - stalls[0]   #  (last stall - first stall )

    # Test every distance starting from 1
    for d in range(1, max_dist + 1):
        if not can_we_place(stalls, d, cows):
            # Loop breaks at the first invalid distance.
            # The maximum valid distance is the one right before it (d - 1).
            return d - 1

    return max_dist



def can_we_place(stalls: list[int], dist: int, cows: int) -> bool:
    count_cows = 1         # Always place the first cow
    last_placed = stalls[0] # at the very first stall

    for i in range(1, len(stalls)):
        # If the gap is sufficient, place the next cow
        if (stalls[i] - last_placed) >= dist:   ## Dist won't  need to be less for next element to place.... it can be greater but not less.
            count_cows += 1 
            last_placed = stalls[i]

            # Return early if all cows are placed successfully
            if count_cows >= cows:
                return True

    return False




cows = 4
stalls = [0, 3, 4, 7, 10, 9]

# print(aggressive_cows_linear(stalls, cows) )
print(aggressive_cows_binary(stalls, cows))




# =================================== Actual Leetcode question ==================================
''' https://leetcode.com/problems/magnetic-force-between-two-balls/description/ '''
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        def can_we_place(position: list[int], dist: int, cows: int) -> bool:
            count_cows = 1         # Always place the first cow
            last_placed = position[0] # at the very first stall

            for i in range(1, len(position)):
                # If the gap is sufficient, place the next cow
                if (position[i] - last_placed) >= dist:
                    count_cows += 1
                    last_placed = position[i]

                    # Return early if all cows are placed successfully
                    if count_cows >= cows:
                        return True
            return False
        

        position.sort()
        low = 1
        high = position[-1] - position[0]
        best_dist = -1

        while low <= high:
            # Formula prevents potential integer overflow (useful to keep in mind across languages)
            mid = low + (high - low) // 2

            if can_we_place(position, mid, m):
                # mid is valid, record it as a potential answer
                best_dist = mid
                # Shift the lower boundary up to search for an even larger valid distance
                low = mid + 1
            else:
                # mid is invalid (we couldn't fit the cows), shrink the upper boundary down
                high = mid - 1

        # Note: When the loop terminates, 'high' also points to the maximum possible distance.
        return best_dist


# m = 2
# position = [5,4,3,2,1,1000000000]
# c1 = Solution()
# print(c1.maxDistance(position, m))
