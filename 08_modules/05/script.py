import shapes
def show_menu():
    print('Wybierz kształt pomieszczenia')
    print('1 - kwadrat')
    print('2 - prostokąt')
    print('3 - trapez')

def square_room(flat_area):
    a = float(input('Podaj długość boku -> '))
    room_area = shapes.square(a)
    flat_area += room_area
    return flat_area

def rect_room(flat_area):
    a = float(input('Podaj długość boku A -> '))
    b = float(input('Podaj długość boku B -> '))
    room_area = shapes.rectangle(a, b)
    flat_area += room_area
    return flat_area

def trapez_room(flat_area):
    a = float(input('Podaj długość podstawy A -> '))
    b = float(input('Podaj długość podstawy B -> '))
    h = float(input('Podaj wyskosc H -> '))
    room_area = shapes.trapezoid(a, b, h)
    flat_area += room_area
    return flat_area

def main():
    rooms_number = int(input('Podaj liczbe pokoi: '))
    flat_area = 0
    for r in range(rooms_number):
        show_menu()
        room_shape = input()
        if room_shape == '1':
            flat_area = square_room(flat_area)
        elif room_shape == '2':
            flat_area = rect_room(flat_area)
        elif room_shape == '3':
           flat_area = trapez_room(flat_area)
        else:
            print('To nie jest prawidłowy wybór')

    print(f'Powierzchnia całkowita mieszkania to {flat_area} m2')

if __name__ == '__main__':
    main()