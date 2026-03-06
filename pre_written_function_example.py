# pre written function example

import random  # Import the random module
#Import specific functions
# from discounted_price import calc_discount

# item = int(input('Enter your price of item:  '  ))
# discount = int(input('Enter your discounted price of item: '  ))



#===================# Demonstrating Python's pre-written (built-in) functions=======================

# 2. max() and min() - find largest and smallest values

numbers = [4, 9, 1, 7, 3]
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
print("random value:", random.randint(1,numbers[4]))
print("random value of the list:", random.choice(numbers))



# 3. len() - returns the length of an object
text = "Python"
print("Length of text:", len(text))

#=====function from another program python example code.====================

# final_price = calc_discount(item,discount)

# print (F'The discounted price of your item is now {final_price}  \n')
# print (F'The original price of your item was {item}')
# print (F'We gave you an {discount} % of discount ')

#valadition of calc_discount
# Actual behaviour : function returns the discounted item. example price of the item is 120, discount is 50%.  functon returns £60
# expected behaviour: function returns the discounted item. example price of the item is 120, discount is 50%.  functon returns £60
    


