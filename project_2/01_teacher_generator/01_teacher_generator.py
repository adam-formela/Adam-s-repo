import sys


def load_csv_file():
    try:
        with open('students.csv', encoding='utf-8') as file:
            content = file.readlines()
            print("File 'students' loaded.\n")
            new_list = []
            for row in content:
                row = row[0:-1]#usuwa znak nowej linii na koncu wiersza
                row = row.split(',')
                for i in row:
                    new_list.append(i)
            new_list = new_list[5:]
            return new_list
    except FileNotFoundError:
        print('The file is empty. Exiting...')
        sys.exit()

def load_message():
    try:
        with open('message.txt', 'r', encoding='utf-8') as text:
            text = text.readlines()
            print("File 'message' loaded.\n")
            return text
    except FileNotFoundError:
        print('The file is empty. Exiting...')
        sys.exit()


due_date = '30/06/2022'
new_list = load_csv_file()

names = new_list[1:len(new_list):5]
tasks = new_list[3:len(new_list):5]
grades = new_list[4:len(new_list):5]

message = load_message()
message = ' '.join(message)# format list to string

if __name__ == '__main__':
    for name, task, grade in zip(names, tasks, grades):
        if grade == '0' or grade[0:8] == 'nieobecn':
            print(f"Welcome {name}, \n\nThis is a kindly reminder that you have 5 task(s) left to submit before you can graduate. \nYour current grade is 0. If you want to pass this semester you must submit all due assignments before the due date: 30/06/2022.")
            print('***********************************')
        else:
            print(message.format(name, task, grade, float(grade) + 1, due_date))
            print('***********************************')