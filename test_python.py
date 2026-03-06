print('Hello world, i am zaki')

num1 = int(input('Enter your first number please '))
num2 = int(input('Enter your second number please '))
sum = num1 + num2
print(f'The sum of the two numbers are {sum}')

def bigest_Number(num1,num2):
    if num1 >= num2:
       print (f'{num1} is the largest ')
    else: 
        print (f' {num2} is the largest ')
    
    
bigest_Number(num1,num2)