import re

pattern = "term1"
text = "this is a text which includes the term1 and anohter term"

if(re.search(pattern, text)):
    print("Found")
else:
    print("Not found")

split_term = "@"
text = "What's your email: hello@hello.com righ?"
print(re.split(split_term,text))


#A pattern followed by the meta-character * is repeated zero or more times.
#Replace the * with + and the pattern must appear at least once.
#Using ? means the pattern appears zero or one time.
#For a specific number of occurrences, use {m} after the pattern, where m is replaced with the number of times the pattern should repeat.
#Use {m,n} where m** is the minimum number of repetitions and **n is the maximum. Leaving out n** {m,} means the value appears at least **m times, with no maximum.


def multi_re_find(patterns,phrase):
    '''
    Takes in a list of regex patterns
    Prints a list of all matches
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %(pattern))
        print(re.findall(pattern,phrase))
        print('\n')

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [ 'sd*',        # s followed by zero or more d's
                'sd+',          # s followed by one or more d's
                'sd?',          # s followed by zero or one d's
                'sd{3}',        # s followed by three d's
                'sd{2,3}',      # s followed by two to three d's
                '[sd]',         # either s or d
                's[sd]+'        # s followed by one or more s or d
                ]

print(multi_re_find(test_patterns,test_phrase))

test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print(re.findall('[^!.? ]+',test_phrase))


test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns=['[a-z]+',      # sequences of lower case letters
               '[A-Z]+',      # sequences of upper case letters
               '[a-zA-Z]+',   # sequences of lower or upper case letters
               '[A-Z][a-z]+'] # one upper case letter followed by lower case letters
                
multi_re_find(test_patterns,test_phrase)

test_phrase = 'This is a string with some numbers 1233 and a symbol #hashtag'

test_patterns=[ r'\d+', # sequence of digits
                r'\D+', # sequence of non-digits
                r'\s+', # sequence of whitespace
                r'\S+', # sequence of non-whitespace
                r'\w+', # alphanumeric characters
                r'\W+', # non-alphanumeric
                ]

multi_re_find(test_patterns,test_phrase)