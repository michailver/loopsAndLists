# # 1. Sukurkite funkciją, kuri išvestų jūsų vardą ir kodėl pasirinkote
# # programavimą. Iškvieskite šią funkciją tris kartus.
# def fun1 ():
#     print('Michail')
#     print('nes reikia darbo, ir aš jau ši beita moku šitoje srytije')
#
# for i in range(3):
#     fun1()
#
# print('##############################################################################################################')
# # 2. Sukurkite funkciją, kuri išvestų 5 eilučių eilėraštį. Iškvieskite šią funkciją 5 kartus.
# def fun2 ():
#     print(  'Šalta. Medžiai juodi, ir dangus kaip švinas.\n'
#             'Lapai pabyra vieni, plėšomi vėjo.\n'
#             'Nieko nėra! Nei saulės, nei giedrų dienų.\n'
#             'Lengvas rūkas kyla ir nyksta virš žemės...\n'
#             'Širdyje – ruduo.') #Salomėja Nėris – "Ruduo"
#
# for i in range(5):
#     fun2()
#
# print('##############################################################################################################')
# # 3. Sukurkite tris funkcijas, kur kiekviena išvestų skirtingus tekstus. Iškvieskite
# # visas tris funkcijas po vieną kartą.
# def fun31 ():
#     print('fun31')
# def fun32 ():
#     print('fun32')
# def fun33 ():
#     print('fun32')
# fun31()
# fun32()
# fun33()
# print('##############################################################################################################')
# # 4. Sukurkite dvi funkcijas, kur vienoje būtų viena teksto eilutėje, kitoje kita.
# # Sukurkite trečią funkciją, kuri iškviestų pirmas dvi funkcijas. Iškvieskite šią
# # trečiąją funkciją už visų funkcijų ribų.
# def fun4 ():
#     fun31()
#     fun32()
#
# fun4()
# print('##############################################################################################################')
# # 5. Sukurkite funkciją, kurios viduje sugeneruotumėte du atsitiktinius
# # skaičius. Funkcijoje suskaičiuokite ir išveskite šių dviejų skaičių sumą,
# # kartu išvedant ir patį atliekamą veiksmą (pvz 7 + 2 = 9). Iškvieskite šią
# # funkciją keletą kartų.
# import random
# def fun5 ():
#     a1 = random.randint(1, 9999)
#     a2 = random.randint(1,9999)
#     print(f'{a1} + {a2} = {a1+a2}')
#
# for i in range(3):
#     fun5()
#
# print('##############################################################################################################')
# # 6. Sukurkite ir iškvieskite funkciją, kurioje kintamuosiuose būtų saugoma
# # informacija apie policininką (vardas, pavardė, amžius, alga, etatas,
# # specializacija). Išveskite šią informaciją suformatuotai (pavyzdžiui įterpkite
# # į sakinį, ar išveskite sąrašu ar pan.).
# def fun6 (name, surname, age, salary, position, specialization):
#     print(f'Policininkas {name} {surname}, {age} metų amžiaus, dirba {position} ir specializacija {specialization}, jo alga siekia {salary} eurų.')
# fun6("Jonas","Petrauskas",35,1500,"serzantu","eismo priežiūra")
#
# print('##############################################################################################################')
# # 7. Sukurkite funkciją, kuri išvestų 10 atsitiktinių skaičių. Po visų išvestų
# # skaičių turėtų padėti tuščią eilutę. Šią funkciją iškvieskite 5 kartus.
# def fun7 ():
#     for i in range(10):
#         if i < 10:
#             print (f'{i}: {random.randint(1, 9999)} ', end='')
#     print('')
#
# for i in range(5):
#     fun7()
#
# print('##############################################################################################################')
# 8. Sukurkite funkciją, kuri išvestų atsitiktinį skaičių. Už funkcijos ribų
# sukurkite ciklą, kurį būtų vykdomas 10 kartų. Iškvieskite sukurtą funkciją
# cikle. Turėtumėte pamatyti 10 atsitiktinių skaičių.
# def fun8 ():
#     a1 = random.randint(1, 9999)
#     print(f'{i}: {a1}')
#
# for i in range(10):
#     fun8()
# print('##############################################################################################################')
# 9. Sukurkite funkciją pasisveikinimui, šiai funkcijai per argumentus
# perduokite vardą, funkcijoje išveskite tekstą labas ir gautą vardą.
# Sukurkite kitą funkciją, kuri irgi per argumentus gautų vardą, tačiau
# pasakytų 'viso gero' ir patį vardą. Ne funkcijose susikurkite kintamąjį
# vardui saugoti ir įrašykite vardą. Iškvieskite abi funkcijas, perduodant
# kintamąjį joms.
# def fun8_hi (name):
#     print(f'Labas {name}')
# def fun8_bye (name):
#     print(f'Viso gero {name}')
# name1 = 'Kestas'
# fun8_hi(name1)
# fun8_bye(name1)


# print('##############################################################################################################')
# # 10.Sukurkite funkciją, kuriai perduotumėte du skaičius. Ši funkcija turi rasti
# # kuris skaičius yra didesnis ir išvesti gautą atsakymą, o jei skaičiai lygūs -
# # tuomet išvesti, kad skaičiai lygūs. Iškvieskite šią funkciją keletą kartų,
# # duodant skirtingus skaičius.
# import random
# def fun10 (x, y):
#     print(f'ivesta: {x}, {y}')
#     if x > y:
#         print(f'didžiausias skaičius: {x}')
#     elif x < y:
#         print(f'didžiausias skaičius: {y}')
#     else:
#         print(f'skaicia lygūs: {x}')
#
# fun10 (random.randint(1, 9999), random.randint(1, 9999))
# fun10 (random.randint(1, 9999), random.randint(1, 9999))
# fun10 (random.randint(1, 9999), random.randint(1, 9999))
# # print('##############################################################################################################')
# # 11.Sukurkite funkciją, kuri per argumentus gautų automobilių duomenis
# # (markė, modelis, gamybos metai, darbinis tūris). Ši funkcija turėtų šiuos
# # duomenis išvesti kaip nors gražiai formatuotai. Iškvieskite šią funkciją du
# # kartus, perduodant skirtingus duomenis jai.
# def fun11 (brand, model, year,eng_volume):
#     print(f"Automobilis: {brand} {model}")
#     print(f"Gamybos metai: {year}")
#     print(f"Darbinis tūris: {eng_volume} litrų")
#     print("-" * 20)
# fun11("Toyota", "Corolla", 2023, 1.8)
# fun11("BMW", "5 Series", 2022, 3.0)
# print('##############################################################################################################')
# # 12.Sukurkite funkciją sumai skaičiuoti, ši funkcija per argumentus turėtų
# # gauti du skaičius, bei išvesti patį veiksmą kartu su atsakymu (pvz 7 + 5 =
# # 12). Sukurkite tokias pačias funkcijas skirtumui, sandaugai ir dalmeniui
# # rasti. Sukurkite dar vieną funkciją, kuri sugeneruotų du atsitiktinius
# # skaičius, bei iškviestų kitas 4 funkcijas, perduodant joms sugeneruotus
# # skaičius. Šią bendrąją funkciją iškvieskite keletą kartų.
# import random
#
# def fun12_sum (x,y):
#     print(f'{x} + {y} = {x + y}')
#
# def fun12_sub (x,y):
#     print(f'{x} - {y} = {x - y}')
#
# def fun12_mult (x,y):
#     print(f'{x} * {y} = {x * y}')
#
# def fun12_div (x,y):
#     print(f'{x} / {y} = {x / y}')
#
# def fun12_call ():
#     x = random.randint(1, 99)
#     y = random.randint(1, 99)
#     fun12_sum(x, y)
#     fun12_sub(x, y)
#     fun12_mult(x, y)
#     fun12_div(x, y)
#     print('-' * 20)
# fun12_call()
# fun12_call()

# print('##############################################################################################################')
# # 13.Susikurkite funkciją, kuri per argumentus priimtų žodžių masyvą.
# # Funkcijoje išveskite visus žodžius iš masyvo atskirose eilutėse, nurodant
# # žodžio ilgį (simbolių kiekį). Už funkcijos ribų susikurkite žodžių masyvą ir
# # užpildykite jį duomenimis. Iškvieskite sukurtą funkciją perduodant turimą
# # masyvą.
# def fun13(list1):
#     for word in list1:
#         print(f'Zodis: {word}. Zodžio ilgis: {len(word)}')
#
#
# shoping_List = ['pienas', 'duona', 'superduper extra big appel', 'sorai', 'suris']
# fun13(shoping_List)

# print('##############################################################################################################')
# # 14.Susikurkite funkciją, kuri per argumentus priimtų skaičių masyvą. Funkcija
# # turėtų atspausdinti visus skaičius, šalia jų išvedant to skaičiaus kvadratą ir
# # jį padalintą iš dviejų. Už funkcijos ribų susikurkite du skaičių masyvus ir
# # užpildykite jį duomenimis. Iškvieskite funkciją du kartus, kiekvieną kartą
# # perduodant skirtingą turimą masyvą.
# def fun14(num_list):
#     for number in num_list:
#         print(f'{number} | Kvadratas: {number*number} | padalinta iš {number / 2}')
#     print('#'*40)
#
#
# num_list1 = [2,4,8,10,25,36,4,5,87,24]
# num_list2 = [45,15,18,369,148,2]
# fun14(num_list1)
# fun14(num_list2)

# print('##############################################################################################################')
# 15.Susikurkite funkciją, kuri per argumentus priimtų pažymių masyvą, bei
# studento vardą su pavarde. Funkcija turėtų išvesti studento vardą ir
# pavardę, jo pažymius. Taip pat, suskaičiuoti vidurkį, bei jį išvesti. Už
# funkcijos ribų susikurkite reikiamus kintamuosius ir masyvus, arba
# objektus studentų pažymiams saugoti ir užpildykite juos duomenimis.
# Iškvieskite šią funkciją perduodant visus reikalingus duomenis.
def fun15 (st_name, st_surname, marks_list):
    print(f'studentas: {st_name} {st_surname} | Pazimiai: ', end='')
    mark_sum = 0
    for mark in marks_list:
        mark_sum += mark
    #print(' '.join(str(marks_list)), end='')
    print(', '.join(map(str, marks_list)), end='')
    print(f' | Pazimiu vidurkis: {round(mark_sum/len(marks_list),1)}')

studens_marks = [
    ['jonas', 'jonaitis', [3, 5, 8]],
    ['jone','jonaitiene', [6, 10, 5]],
    ['petras','Petraitis', [10, 9, 8, 2, 2]]
]

for one_student in studens_marks:
    #print(one_student)
    fun15(one_student[0],one_student[1],one_student[2])

# print('##############################################################################################################')
# 16.Susikurkite funkciją, kuri per argumentus priimtų skaičių masyvą. Funkcija
# turėtų rasti didžiausią skaičių iš masyvo bei išvesti gautą atsakymus. Taip
# pat, susikurkite funkciją, kuri per argumentus priimtų masyvą ir į jį
# sugeneruotų pasirinktą kiekį atsitiktinių skaičių. Susikurkite tris tuščius
# masyvus. Iškvieskite atsitiktinių skaičių generavimo funkciją tris kartus,
# kiekvieną kartą perduodant funkcijai vis kitą masyvą. Kai duomenys bus
# užpildyti, masyvuose esančią informaciją išsiveskite norimu būdu (per
# console.log arba per dar atskirą funkciją). Tuomet kvieskite didžiausio
# skaičiaus paieškos funkciją tris kartus, kiekvieną kartą perduodant
# skirtingą masyvą į ją.
def fun16_max (number_list)
    max_number = max(number_list)
    print(f'didziausias skaicius:{max_number}')



# print('##############################################################################################################')
# 17.Susikurkite funkciją, kuri grąžintų bet kokį jūsų norimą sakinį. Iškvieskite
# šią funkciją ir išspausdinkite gautus rezultatus.
# print('##############################################################################################################')
# 18.Susikurkite funkciją, kuri grąžintų atsitiktinai sugeneruotą skaičių.
# Iškvieskite šią funkciją kelis kartus ir gautus atsakymus išveskite kokiu
# norite būdu.
# print('##############################################################################################################')
# 19.Susikurkite funkciją, kuri per argumentus priimtų studento vardą ir
# vidurkį. Ši funkcija turėtų sugeneruoti iš to sakinį (pvz Studentas Tomas
# turi vidurkį 8.7) ir tai grąžinti kaip atsakymą. Iškvieskite šią funkciją bent
# porą kartų, perduodant vis skirtingus duomenis. Gautus atsakymus
# išveskite.
# print('##############################################################################################################')
# 20.Susikurkite funkciją, kuri per argumentus gautų skaičių. Ji turėtų surasti
# duoto skaičiaus mažiausią daliklį (skaičių iš kurio dalinasi be liekanos). Už
# funkcijos ribų sukite ciklą nuo 10 iki 30 ir kiekvienoje ciklo iteracijoje
# iškvieskite šią funkciją, perduodant ciklo kintamąjį.
# print('##############################################################################################################')
# 21.Susikurkite funkciją, kuri per argumentus gautų skaičių. Ji turėtų patikrinti
# ar šis skaičius yra pirminis (grąžina True jei pirminis, ir False jei ne
# pirminis). Už funkcijos ribų sukite ciklą nuo 2 iki 15, kiekvienoje ciklo
# iteracijoje išveskite tikrinamą skaičių ir šalia jo iškviestos funkcijos
# atsakymą (pvz 10 false, 11 true, ...).
# print('##############################################################################################################')
# 22.Susikurkite bent 3 matematines funkcijas, priimančias reikiamus
# argumentus (pvz suma iš dviejų skaičių, suma iš trijų skaičių, skirtumas,
# sandauga, dalyba) ir grąžinančias atitinkamus atsakymus. Taip pat,
# susikurkite funkciją, kurioje būtų sugeneruojamas reikiamas kiekis
# atsitiktinių skaičių ir išvedami visų skaičiavimų atsakymai su veiksmais
# (iškviečiant atitinkamas kitas funkcijas ir perduodant reikiamus
# kintamuosius) (pagal 23 pavyzdį). Iškvieskite šią pagrindinę funkciją bent
# kartą.
# print('##############################################################################################################')
# 23.Susikurkite funkciją kuri priimtų skaičių masyvą per argumentus. Ši
# funkcija turėtų rasti duotųjų skaičių sumą ir grąžinti gautą atsakymą. Už
# funkcijos ribų susikurkite du skaičių masyvus ir užpildykite juos
# duomenimis. Iškvieskite turimą funkciją du kartus, jai abu kartus
# perduodant skirtingą masyvą. Gautus atsakymus išveskite. Taip pat,
# raskite kuri suma gavosi didesnė ir išveskite atsakymą.
# print('##############################################################################################################')
# 24.Susikurkite funkciją kuri per argumentus priimtų žodžių masyvą. Ji turėtų
# rasti ir grąžinti ilgiausią žodį masyve. Už funkcijos ribų susikurkite žodžių
# masyvą. Iškvieskite funkciją perduodant jai žodžių masyvą. Gautą
# atsakymą išveskite, taip pat, nurodykite šio žodžio ilgį.
# print('##############################################################################################################')
# 25.Susikurkite funkciją kuri per argumentus priimtų pažymių masyvą. Ji
# turėtų patikrinti ar visi pažymiai teigiami: jei visi teigiami turėtų grąžintų
# True kaip atsakymą, o jei yra bent vienas neigiamas - False. Susikurkite du
# pažymių masyvus. Iškvieskite šią funkciją du kartus, abu kartus
# perduodant skirtingus masyvus. Gautus atsakymus paverskite į tekstą
# (jeigu gavote True - išveskite tekstą 'visi studento pažymiai teigiami', jei
# False - 'studentas turi bent vieną neigiamą pažymį'). Šiam iškonvertavimui
# iš True/False į tekstą galite pamėginti pasikurti atskirą funkciją, jai
# perduoti kitos funkcijos atsakymą.
# print('##############################################################################################################')
# 26.Pabandykite parašyti bent dvi pasirinktas funkcijas, kuriose būtų
# naudojami default parametrai. Iškvieskite šias funkcijas įvairiais būdais
# (perduodant visus argumentus, bei neperduodant tų kuriuos galima
# praleisti (turinčius default reikšmes)).