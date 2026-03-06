#A condition that checks if an age is greater
#than or equal to 18 and the person is a student
#print eligible for student discount
#if the condition is true,otherwise print 'Not eligible'

age = int(input('Enter your age please. '))# We asign a varible to age and input enter your age please
student = input('Are you a student? (yes/no) ')# We asign a varible to student and display if they are a student

if age >= 18 and student == 'yes': # if statement determining if they are a student and elgible for discount
    print ('You are eligible for student discount.')# We display the sentence
else:
    print ('You are not eligible for student discount.')# if first condtion is not met we display the second sentence





print('==========================End of the program=============================')