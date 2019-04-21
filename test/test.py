# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order¶
#   spy_game([1,2,4,0,0,7,5]) --> True
#   spy_game([1,0,2,4,0,5,7]) --> True
#   spy_game([1,7,2,0,4,5,0]) --> False

def spy_game(nums):

    spy = ""

    for num in nums:
        if (num == 0 or num == 7):
            spy += str(num)
    
    return spy == "007"

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))