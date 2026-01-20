# https://leetcode.com/problems/contains-duplicate/description/

# TEST CASES
nums = [1,2,3,4]
nums2 = [1,1,1,3,3,4,3,2,4,2]
nums.sort() # sort in ascending order
nums2.sort()

def contains_duplicate(A, i=0):
    # stop when there's no next element to compare
    if i >= len(A) - 1:
        return False

    if A[i] == A[i+1]:
        return True
    return contains_duplicate(A, i+1)

print(contains_duplicate(nums))
print(contains_duplicate(nums2))


# Have done it playing with sets would have been a much clever approach but ok