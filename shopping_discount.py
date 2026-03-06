#This program will calculate shopping outfit

#Variable stores original prices
price_suit = float(input('Enter the price of the suit: '))
price_trouser = float(input('Enter the price of the trouser: '))
price_shirt = float(input('Enter the price of the shirt:  \n'))
uk_vat = 0.2


  
if price_suit <= 0: 
    print("Negative input given. Exiting...")
    exit() 
elif price_trouser <= 0:
  print ('Negative input hmm interesting')
  exit()
elif price_shirt <= 0:
  print (' Negative input hmm interesting')
  exit()
else:
  print (f'Your final price will be calcualted \n')  
   
#variable stores discount percentages
discount_suit = 50
discount_trouser = 40
discount_shirt = 20

#Defines a function called price after discount and price and discount are the parameters
#function will be brought back after to calc price after discount
def price_after_discount (price,discount):
  discount_amount = price * (discount  / 100)
 #How much money saved because of discount
  final_price = price - discount_amount
  #calcs final price of discount
  return final_price

#sends value of final price back to the function
final_suit = price_after_discount (price_suit,discount_suit)
final_trouser = price_after_discount (price_trouser,discount_trouser)
final_shirt = price_after_discount (price_shirt, discount_shirt)
total_price =final_suit + final_trouser + final_shirt
vat_price = uk_vat * total_price
price_after_vat = total_price + vat_price

#Calcs the final prices of each clothing with their discount


#Using f strings to format it nicely

# Redundancy means refers to the unnecessary duplication of data across multiple locations or tables.
#calculating total price of outifts
#original prices of items
# original_price_suit = 120
# original_price_trouser = 80
# original_price_shirt = 50

#after discount prices

after_discount_suit = final_suit
after_discount_trouser = final_trouser
after_discount_shirt = final_shirt
def total_price (suit,trouser,shirt):
 return suit + trouser + shirt
#Calculating total prices for items
total_of_price = total_price(after_discount_suit,after_discount_trouser,after_discount_shirt)

print(f'shopping programm \n')  

print(f'the original price of suit is £{price_suit} ')   
print(f'the original price of the trouser is £{price_trouser} ')
print(f'the original price of the shirt is £{price_shirt} \n') 


print(f'the discounted percentage is {discount_suit}%')
print(f'the discounted percentage is {discount_trouser}%')
print(f'the discounted percentage is {discount_shirt}% \n')

print(f'the after discount of price for suit is £{after_discount_suit}')
print(f'the after discount of price for trouser is £{after_discount_trouser}')
print(f'the after discount of price for shirt is £{after_discount_shirt} \n')

print(f'The total price of the items are £{total_of_price}')
print(f'The VAT amount is {uk_vat}')
print(f'The price after VAT is £{price_after_vat} \n')

print('==========================End of the program=============================')