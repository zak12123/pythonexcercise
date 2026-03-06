#while loops 
#num = int(input('Enter a number between 1-10.'))
#while num < 1 or num > 10:
 #    print (f'{num} is not valid.')
#num = int(input('Enter a number between 1-10.'))
#print (f'Your number is {num} ')

#num =int(input('Enter a number.'))
#while num >= 0:
 #     print (num)
  #    num -= 1
      
#print ('Blast off')

secret_number = 67
guess = int(input('Enter your secret number.'))
while guess != secret_number:
    guess = int(input('Enter your secret number.'))
    print ('Invalid choice')  
else: 
     print ('Lucky chocie')
     guess = int(input('Enter your secret number.'))
     
   
