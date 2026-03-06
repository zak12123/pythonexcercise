#animal sound detector
a_animal = input('Enter the name of the animal and i will tell you the sound \n')


def get_animal_sound(animal_name):
    if animal_name == 'dog':
        print('woof')
        # return 'woof'
    elif animal_name == 'cat':
        print('meow')
        # return 'meow'
    elif  animal_name == 'snake':
     print ('hiss')
    else:
        print('it is not an animal that i know!')
        # return "I don't know what noise it is"


get_animal_sound(a_animal)
# print (get_animal_sound('dog'))
# print (get_animal_sound('cat'))
# print (get_animal_sound('cow'))   

print('==========================End of the program=============================')

 