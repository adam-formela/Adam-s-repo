# Utwórz klasę zegaro-kalendarza. Zegaro-kalendarza łączy cechy zegara oraz kalendarza. Zaimplementuj dziedziczenie wielokrotne.
# Nasz zegaro-kalendarza powinen móc podawać aktualną datę oraz wyświetlać ile dni ma dany miesiąc.
# Dodatkowo utwórz sposób wyświetlania tak, aby zegaro-kalendarz zawierał datę, godzinę oraz widok dni ułożonych tygodniowo. Dla uproszczenia przyjmij 7 dni w tygodniu zawsze zaczyna się od pierwszego dnia.

from datetime import date, datetime

import pytz as pytz


class Watch():
    def __init__(self):
        print('Watch function is presenting the time')

    @staticmethod
    def show_time():
        return datetime.now()


class Calendar():
    def __init__(self):
        print('Calendar function is presenting the date')

    @staticmethod
    def show_date():
        print('12/07/2022')

    @staticmethod
    def show_days_in_month():
        print('30')
        days = 30
        for day in range(1,31):
            if day < 10:
                print('0' + str(day), end='\t')
            else:
                print(str(day), end='\t')

            if (day) % 7 == 0:
                print()
        print()


class Calendarwatch(Watch, Calendar):
    def __init__(self):
        print('CalendarWatch contain functions of watch and calendar')


poland = Calendarwatch()
poland.show_time()
poland.show_date()
poland.show_days_in_month()

print(date.today())

print(poland.show_time())