# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#   has_33([1, 3, 3]) → True
#   has_33([1, 3, 1, 3]) → False
#   has_33([3, 1, 3]) → False

def has_33(nums):
    for index, num in enumerate(nums):
        if num == 3:
            return num == nums[index + 1]
    
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))