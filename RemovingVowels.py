Vowels=('a','e','i','o','u')
msg=input('Enter The Word:')
new_msg=''

for letter in msg:
    if letter not in Vowels:
        new_msg +=letter
        print(letter,'is not a vowel')
    else:
        if letter in Vowels:
            print(letter,'is a Vowel')
print(new_msg)