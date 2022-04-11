class Account:
    def __init__(self, first_name, last_name):
      self.first_name = first_name
      self.last_name = last_name
      self.__account_number = '12 4530 0000 1001 2345 3213'

    def show_number(self):
        print(self.last_name, '--->')
        print("Current account number: {}".format(self.__account_number))

    def set_new_bank_nr(self, number):
        self.__account_number = number



account = Account('Anna', 'Kowalska')
account.show_number()

account.last_name = 'Wisniewska'
account.show_number()

account.__account_number = '1111111111' # nie zadziała!!!
account.show_number()

print('***********')
account.set_new_bank_nr('1234 5678 0000 0000')
account.show_number()