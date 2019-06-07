from collections import Counter

l = [1,1,1,2,3,4,5,3,4,5,6,7,8,4,5,3,3,3,2,3,4,2,1,3,4,4,2,2,2,2,2]
print(Counter(l))

s = "abvmvalnvpanp vanfjafaf afnajfiaifaifnaifinkn"
print(Counter(s))

s = "how many time appears each word in this sentence word time word word"
words = s.split()
print(Counter(words))

c = Counter(words)
print(c.most_common(4))


from collections import defaultdict

d = {"k1": 1}
print(d["k1"])
#print(d["k2"]) #error not exists

d = defaultdict(lambda: "default value") #assig a default value to none exist keywords
print(d["k2"])
