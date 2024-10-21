import datetime
from tabulate import tabulate

users = [
    ['Jonas','Jonaitis',datetime.date(2024, 6, 15), datetime.date(2024, 12, 15), True, False],
    ['Kestas', 'Kestaitis', datetime.date(2024, 5, 15), datetime.date(2024, 11, 15), True, False],
    ['Petras', 'Petraitis', datetime.date(2024, 1, 15), datetime.date(2024, 7, 15), False, True],
    ['Ona', 'Onaitienė', datetime.date(2024, 8, 15), datetime.date(2025, 2, 15), True, False],
    ['Mantas', 'Mantaitis', datetime.date(2024, 10, 15), datetime.date(2025, 4, 15), False, False],
    ['Ieva', 'Ievaitė', datetime.date(2023, 3, 15), datetime.date(2023, 9, 15), True, True]
]

def updateDoorEnterStatus(users):
    for user in users:
        if user[4] and user[3] < datetime.date.today():
            user[4] = False
            user[5] = False
        if user[4] == False and user[3] >= datetime.date.today():
            user[4] = True


def printMenu():
    print('*' * 40)
    print('1. C: Pridet nauja irasha. ')
    print('2. R: Parodyti įrašus.')
    print('3. U: Redaguoti irašus.')
    print('4. D: Pašalinti įraša.')
    print('5.    Uždaryti programa')
    print('*' * 40)


def newUserInsert():
    names = input('Vartotojo vardas: ')
    surname = input('Vartotojo pavarde: ')
    start_date = datetime.datetime.strptime(input('Įveskite pradžios datą (yyyy-mm-dd): '), "%Y-%m-%d").date()
    end_date = start_date + datetime.timedelta(days=180)
    enter = True  # galimibe patekti
    box = input('Ar yra sandeliavimo dėžė? (taip/ne): ').lower() == 'taip'  # naris nebutinai turi tureti
    users.append([names, surname, start_date, end_date, enter, box])


print('-= Dirbtuviu nariu valdymo systema =-')
print('ishsirinkit veiksma ivedus to veiksmo numeri')
while True:
    updateDoorEnterStatus(users)
    printMenu()
    choice = input('Komandos numeris: ')
    print('*' * 40)
    match choice:
        case '1':
            newUserInsert()
        case '2':
            print(tabulate(users, headers = ['Vardas', 'Pavarde', 'naristes pradzia', 'naristes pabaiga', 'Duris', 'Deze'],
                           tablefmt='orgtbl', showindex='always'))
        case '3':
            edit_index = int(input(f'Iveskit nario numeri (indeksa) kuri noretumete redaguoti (max:{len(users)-1}): '))
            print('*' * 40)
            edit_all = input('Ar redaguoti viska(1) ar tik pratest(2) nariste nuo šiandiena? (1/2): ').lower() == '1'
            if edit_all:
                selected_user = users[edit_index]
                print(f'Senas irašas')
                print(tabulate([selected_user]))
                names = input('Vartotojo vardas: ')
                surname = input('Vartotojo pavarde: ')
                start_date = datetime.datetime.strptime(input('Įveskite pradžios datą (yyyy-mm-dd): '), "%Y-%m-%d").date()
                end_date = datetime.datetime.strptime(input('Įveskite pabaigos datą (yyyy-mm-dd): '), "%Y-%m-%d").date()
                enter = input('Ar duris atsidaro? (t/n): ').lower() == 't'       # galimibe patekti
                box = input('Ar yra sandeliavimo dėžė? (t/n): ').lower() == 't'  # naris nebutinai turi tureti
                users[edit_index] = [names, surname, start_date, end_date, enter, box]
            else:
                start_date = datetime.date.today()
                end_date = datetime.date.today() + datetime.timedelta(days=180)
                users[edit_index][2] = start_date
                users[edit_index][3] = end_date

        case '4':
            delete_index = int(input(f'Iveskit nario numeri (indeksa) kuri noretumete pashalinti (max:{len(users)}): '))
            users.pop(delete_index)
        case '5':
            print("Programa uzdaroma, joke pakeitimai neišsaugoti.")
            break
        case _:
            print ('ERROR: Programos ivedimo klaida.')