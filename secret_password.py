#secret password
secret_password = input('Enter your secret password  ')
max_attempts = 3
guesses = 0

while guesses < max_attempts:
    guess = input('Enter your guess password  ') 
    if guess == secret_password:
        print (' Well done')
        break
    else:
        guesses += 1
        attempts_left = max_attempts - guesses
        if attempts_left > 0:
          print (f'You have {attempts_left} attempts left. Please try again   ')
        
        if attempts_left == 0:
          print ('Error you have reached your limit of attempts  ')
