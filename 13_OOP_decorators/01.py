# Utwórz dekorator @uppercase_decorator, który przyjmuje dowolną funkcję zawracającą łańcuch znaków i zwracający ten sam tekst zmieniony na wielkie litery.
#     Utwórz funkcję zwracającą tekst
#     Utwórz dekorator przyjujący tę funkcję
#     Wywołaj funkcję, by sprawdzić, że decorator działa


def upper_decorator(func):
    def inside():
        txt = func()
        txt = txt.upper()
        return txt

    return inside

@upper_decorator
def daily_news():
    return 'important'

@upper_decorator
def smart_news():
    return 'smart'


print(daily_news())
print(smart_news())
