import random

def generate_number():
    generated_number = ''
    for i in range(40):
        generated_number = generated_number + str(random.randint(0,9))
    return generated_number

def get_number():
    while True:
        try:
            generated_number = input('Enter several of numbers separated by comma: ').split(',')
            print('Provided numbers :', generated_number)
            if len(generated_number) < 2:
                print('Enter at least several numbers')
                continue
            break
        except ValueError as err:
            print('Provide correct numbers')
            continue
    return generated_number
