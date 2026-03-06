#countdown timer
import time

timer = int(input('Enter your countdown '))

for i in range (timer,0,-1):
   print (f'You have {i} seconds left ')
   time.sleep (1)

print ('Times up')


   
