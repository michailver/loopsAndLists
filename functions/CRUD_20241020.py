import datetime
from datetime import datetime, timedelta



users = [
    ['Jonas','Jonaitis',datetime.date(2024, 6, 15), datetime.date(2024, 12, 15), True, False],
    ['Jonas', 'Jonaitis', datetime.date(2024, 6, 15), datetime.date(2024, 12, 15), True, False],
    ['Petras', 'Petraitis', datetime.date(2024, 1, 15), datetime.date(2024, 7, 15), False, True],
    ['Ona', 'Onaitienė', datetime.date(2024, 8, 15), datetime.date(2025, 2, 15), True, False],
    ['Mantas', 'Mantaitis', datetime.date(2024, 10, 15), datetime.date(2025, 4, 15), False, False],
    ['Ieva', 'Ievaitė', datetime.date(2023, 3, 15), datetime.date(2023, 9, 15), True, True]
]

print('-= Dirbtuviu nariu valdymo systema =-')
print('ishsirinkit veiksma ivedus to veiksmo numeri')

while True:
    print('*' * 40)
    print('1. C: Pridet nauja irasha. ')
    print('2. R: Parodyti įrašus.')
    print('3. U: Reaguoti irašus.')
    print('4. D: Pašalinti įraša.')
    print('5.    Uždaryti programa')
    print('*' * 40)
    choice = int(input('Komandos numeris: '))
    match choice:
        case 1:
            names = input('Vartotojo vardas: ')
            surname = input('Vartotojo pavarde: ')
            start_date = input('Naristes pradzia (yyyy-mm-dd): ')
            end_date += datetime.timemedeltas(6 * 30)
            enter = True #galimibe patekti
            box = input('Sandeliavimo deze: ') #naris nebutinai turi tureti
        case 2:
            print('2')
        case 3:
            print('3')
        case 4:
            print('4')
        case 5:
            print("Programa uzdaroma, joki pakeitimai neišsaugoti.")
            break

