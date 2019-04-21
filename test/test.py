# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 
# and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'¶
#   blackjack(5,6,7) --> 18
#   blackjack(9,9,9) --> 'BUST'
#   blackjack(9,9,11) --> 19

def blackjack(a,b,c):

    total = sum((a,b,c))
    
    if 11 in (a,b,c):
        total -= 10

    if is_under21(total):
        return total
    else:
        return "BUST"

def is_under21(num):
    return num <= 21

# Check
print(blackjack(5,6,7))
print(blackjack(9,9,9))
print(blackjack(9,9,11))