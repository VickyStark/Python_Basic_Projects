Vowels=('a','e','i','o','u')
msg=str(input('Enter The Sentence:'))


for letter in msg:
    if letter in Vowels:
        print(letter,'is a Vowel')
    else:
        if letter not in Vowels:
            print(letter,'is not in Vowel')



