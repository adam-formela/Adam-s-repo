# Utwórz klasę Pracownik.
#
#     Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staz pracy.
#     Pracownik powinen miec roczne podwyżki wg. dowolnie wymyślonego sposobu liczenia. Pracownik powinen odprowadzać podatek o wysokoci zależnej od swoich zarobków oraz minimalną składkę zdrowotną.
#     Pracownik powinien mieć pole typu boolowskiego zawierające status studenta. Jeśli pracownik jest studentem jego składka zdrowotna wynosi 0%.
#     Wszyscy pracownicy mają wspólną nazwę firmy. Spółgłoski imienia i nazwiska wraz z nazwą firmy .com tworzą adres mailowy. Np.
#     Adam Kowalski Love Python Company
#     email -> smkwlsk@lovepythoncompany.com

class Worker():
    def __init__(self, name, surname, position, salary:int, experience:float, student:bool):
        self.name = name
        self.surname = surname
        self.position = position
        self.salary = salary
        self.experience = experience
        self.student = student
        self.email = self.name + self.surname + '@lovepythoncompany.com'

    def calc_taxes(self):
        net_salary = self.salary
        if self.student == False:
            net_salary = net_salary - (net_salary * 0.19)
            net_salary = net_salary - (net_salary * 0.09)
            print('Net salary = ', end='')
            return net_salary
        else:
            net_salary = net_salary - (net_salary * 0.19)
            print('Net salary = ', end='')
            return net_salary

    def get_raise(self, percentage):
        self.salary = self.salary + (self.salary * percentage)
        return self.salary


anna = Worker('Anna', 'Baranska', 'Cooker', 2000, 1.5, False)
print(anna.email)
print(anna.calc_taxes())
print('------------------')
print(anna.get_raise(0.05))
print(anna.calc_taxes())