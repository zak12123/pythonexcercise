#VAT calculator
UK_VAT = 0.2
price_before_vat = float(input('Enter the price before vat(£)'))#ask user to input price before VAT
vat_amount = price_before_vat * UK_VAT #Calc vat amount
total_price = price_before_vat + vat_amount#calc total price including vat
print (f'VAT amount of (20%) is £{vat_amount}')#display vat amount
print (f'The total price including the vat is £{total_price}')#display total amount including vat





print('==========================End of the program=============================')