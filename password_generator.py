import string
import random 

banner_message = 'AWESOME Password Generator PROGRAM'
stars = '*' * len(banner_message)
print('\n' + stars + '\n' + banner_message + '\n' + stars + '\n')

letters = string.ascii_letters 

password_length = int(input('Enter password length: '))

password = ''

for letter in range(password_length):
    random_letter = random.choice(letters)
    password = password + random_letter

print('Your password is: ' + password)