list = [1,2,3,4,5,6,7,8,9,10]

for num in list:
    if num % 2 == 0:
        print(f"Num {num} is even")
    else:
        print("Num {} is odd".format(num))

for letter in "Hello World":
    print(letter)

my_list = [(0,1),(2,3),(4,5)]
for a,b in my_list:
    print(a)

d = {"k1": 1, "k2": 2, "k3": 3}
for key, value in d:
    print(key)