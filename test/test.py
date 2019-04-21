#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
#   almost_there(90) --> True
#   almost_there(104) --> True
#   almost_there(150) --> False
#   almost_there(209) --> True
#NOTE: abs(num) returns the absolute value of a numbe

def almost_there(n):
    return ((abs(100 - n)) <= 10 or (abs(200-n)) <=10)

# Check
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))