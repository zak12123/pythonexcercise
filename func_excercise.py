def calculate_double(number):
    multiplication = number * 2
    return multiplication


number_input = int(input('Enter a number:'))
final_calculation = calculate_double(number_input)
print(f'the answer is: {final_calculation}')
