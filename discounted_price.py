#This program calculates the discounted price of an item.
item = int(input('Enter your price of item:  '  ))
discount = int(input('Enter your discounted price of item: '  ))
#price_after_disount = ((item * discount) / 100)
'''
Args: x(float): 
'''
'''
def calc_discount(x,y):
    price_after_disount = ((x * y) / 100)
    return price_after_disount
'''
def calc_discount(original_price,discount_percent):
    discount_percent = discount_percent / 100
    discount_percent = original_price * discount_percent
    final_price = original_price - discount_percent
    return final_price
final_price = calc_discount(item,discount)

print (F'The discounted price of your item is now {final_price}  \n')
print (F'The original price of your item was {item}')
print (F'We gave you an {discount} % of discount ')


print('==========================End of the program=============================')