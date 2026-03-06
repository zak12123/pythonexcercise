#this program calculates area of rectangle
def area_rectangle (length,width): #defining function
   return length * width

length = float(input('Enter your length ' ))
width =  float(input('Enter your width ' ))

area = area_rectangle (length,width)
print (f'The area of the rectangle {area}cm^2 ')

def add_2numbers (number1,number2):
   sum = number1 + number2
   return sum

sum = add_2numbers(length,width)
print (f'The sum of the two numbers is {sum}')



print('==========================End of the program=============================')