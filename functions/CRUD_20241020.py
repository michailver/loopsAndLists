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
            # print(f'{user[0]} False: {user[3]}')
        if user[4] == False and user[3] >= datetime.date.today():
            # print(f'{user[0]} True: {user[3]}')
            user[4] = True


print('-= Dirbtuviu nariu valdymo systema =-')
print('ishsirinkit veiksma ivedus to veiksmo numeri')

while True:
    updateDoorEnterStatus(users)
    print('*' * 40)
    print('1. C: Pridet nauja irasha. ')
    print('2. R: Parodyti įrašus.')
    print('3. U: Reaguoti irašus.')
    print('4. D: Pašalinti įraša.')
    print('5.    Uždaryti programa')
    print('*' * 40)
    choice = input('Komandos numeris: ')
    print('*' * 40)

    match choice:
        case '1':
            names = input('Vartotojo vardas: ')
            surname = input('Vartotojo pavarde: ')
            # start_date = datetime.date.strftime(input('Naristes pradzia (yyyy-mm-dd): '), "%Y-%m-%d")
            start_date = datetime.datetime.strptime(input('Įveskite pradžios datą (yyyy-mm-dd): '), "%Y-%m-%d").date()
            # end_date = (datetime.date(start_date)) + (datetime.timedelta(6 * 365 / 12).isoformat())
            end_date = start_date + datetime.timedelta(days=180)
            enter = True #galimibe patekti
            box = input('Ar yra sandeliavimo dėžė? (taip/ne): ').lower() == 'taip' #naris nebutinai turi tureti
            users.append([names, surname, start_date, end_date, enter,box])
        case '2':
            # for i in range(len(users)):
            #     print(f'Vartotojas: {users[i][0]} {users[i][1]} | Naristes pradžia: {users[i][2]} | Galioja iki: {users[i][3]}, | '
            #           f'Duru atidarimas: {'Taip' if users[i][4] else 'Ne' } | '
            #           f'Dėžę daiktais: {'Turi' if users[i][5] else 'Neturi' }')
            print(tabulate(users, headers = ['Vardas', 'Pavarde', 'naristes pradzia', 'naristes pabaiga', 'Duris', 'Deze'],tablefmt='orgtbl', showindex='always'))
        case '3':
            edit_index = int(input(f'Iveskit nario numeri (indeksa) kuri noretumete redaguoti (max:{len(users)}): '))
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
                print(f'{users[edit_index][2]} = {start_date}')
                print(f'{users[edit_index][3]} = {end_date}')
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

