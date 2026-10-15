import string
import random 

banner_message = 'AWESOME Password Generator PROGRAM'
stars = '*' * len(banner_message)
print('\n' + stars + '\n' + banner_message + '\n' + stars + '\n')

letters = string.ascii_letters 

while True:
    try:
        password_length = int(input('Enter password length: '))
        break
    except ValueError:
        print('Error: Enter an integer number. Try again')

    
password = ''

for letter in range(password_length):
    random_letter = random.choice(letters)
    password = password + random_letter

print('Your password is: ' + password)

print('Thank you for using the progam')