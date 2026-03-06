#a program decides an even or odd number

num = int(input('Please give me a number that determines if it is even or odd. '))# We asign a varible that is an integer to determine if num is odd or even
if (num % 2 == 0):# there is a condition for it so we use if statement and the modulo symbol tells us if the number is able to be divided by 2 as an integer it is even
    print (f'{num} is an even number. ')# Then we dispay using f string to insert value into the sentence we want to print
else:
    print (f' {num} is an odd number. ')# If the first condition is not met then we move onto the other conditon which is odd






print('==========================End of the program=============================')