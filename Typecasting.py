#cube and square root
def double_and_triple (number):
    double = number ** 2
    triple = number ** 3
    return double, triple

number = float(input('Enter your number'))
d,t = double_and_triple (number)
print ((f'Your number is {d} and {t}'))


