#biggest number 
#finding the largest number out of the 3 numbers
num1 = int(input('Enter your first number.' ))
num2 = int(input('Enter your second number.'))
num3 = int(input('Enter your thrid number.' ))
num4 = int(input('Enter your fourth number.' ))



largestNum = max(num1,num2,num3,num4)
print('Hey I find biggest number first ======ha ha ha ', largestNum ,'too late')

if num1 >= num2 and num1 >= num3:
    print (f'{num1} is the largest number which is number 1.')
elif num2 >= num1 and num2 >= num3:
    print (f'{num2} is the largest number which is number 2.')
else:
    print (f'{num3} is the largest number which is number 3.')


print('==========================End of the program=============================')