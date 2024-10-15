#print('##############################################################################################################')
# 1. Su for pagalba penkis kartus išveskite savo vardą.
# for i in range(5):
#     print('Michail')

#print('##############################################################################################################')
# 2. Parašyti for, kuris išvestų kiekvieną skaičių pradedant nuo 0 ir baigiant 10.
# for i in range(11):
#     print(i)

#print('##############################################################################################################')
# 3. Parašyti for, kuris išvestų kas antrą skaičių pradedant 0 ir baigiant 15.
# for i in range(15):
#     if i % 2 == 0 or i == 0:
#         print(i)
#
# for i1 in range(0,15,2):
#     print(i1)

#print('##############################################################################################################')
# 4. Parašyti for, kuris išvestų kas trečią skaičių, pradedant 1 ir baigiant 20.
# Kiekvieną skaičių apskliausti laužtiniais skliaustais. Pvz.: [1][4][7]...
# res=''
# for i in range(1,20,3):
#     #print(f'[{i}]')
#     res += '['+f'{i}'+']'
# print(res)
#print('##############################################################################################################')
# 5. Parašyti for, kuris eitų pro kiekvieną skaičių nuo 1 iki 20. Jame apsirašyti if
# sąlygą, kuri patikrintų ar dabartinis skaičius dalinasi iš 4, jei taip tai šį
# skaičių išvesti.
# for i in range(1,20):
#     if i % 4 == 0:
#         print(i)

#print('##############################################################################################################')
# 6. Išveskite visus skaičius nuo 1 iki 15, prie kiekvieno jų nurodant tai lyginis
# ar nelyginis skaičius. Pvz:
# 1 - nelyginis
# 2 - lyginis
# 3 - nelyginis
# for i in range(1,15):
#     if i % 2 == 0:
#         print(f'{i} - lyginis')
#     else:
#         print(f'{i} - nelyginis')

#print('##############################################################################################################')
# 7. Susikurkite kintamuosius rėžių pradžiai ir pabaigai nusakyti. Patikrinkite,
# kad tai būtų validu (pradžia turi būti mažesnė nei pabaiga). Jei rėžiai
# tinkami, tuomet vykdyti for, kuris atskirose eilutėse išvestų kiekvieną
# skaičių iš tų rėžių, bei atskiriant tarpu - tų skaičių kvadratus.
# a = int(input('rezis a = '))
# b = int(input('rezis b = '))
# if a < b:
#     print(f'{a} < {b}: {a < b}')
#     for i in range(a, b):
#         print (f'{i} {i*i}')
# else:
#     print(f'{a} < {b}: {a < b}')
#print('##############################################################################################################')
# 8. Susikurkite kintamuosius rėžių pradžiai ir pabaigai nusakyti. Patikrinkite,
# kad tai būtų validu (pradžia turi būti mažesnė nei pabaiga). Jei rėžiai
# tinkami, tuomet vykdyti for, kuris iš duotų skaičių išvestų visus nelyginius
# skaičius arba tuos, kurie dalinasi iš 8.
# a = int(input('rezis a = '))
# b = int(input('rezis b = '))
# if a < b:
#     print(f'{a} < {b}: {a < b}')
#     for i in range(a, b):
#         if i % 2 != 0: #or i % 8 == 0:
#             print(f'{i} - nelyginis')
#         elif i % 8 == 0:
#             print(f'{i} - dalinasi iš 8')
# else:
#     print(f'{a} < {b}: {a < b}')

#print('##############################################################################################################')
# 9. Leiskite vartotojui įvesti savo vardą. Ciklą for vykdykite tiek kartų kiek
# tame varde yra raidžių. Visais atvejais išveskite tą patį pasisveikinimą,
# pavyzdžiui "Labas, Ieva" (ši eilutė kartotųsi 4 kartus).
# name = input('jusu vardas: ')
# for i in range(len(name)):
#     print (f'labas, {name}')
# print('-----')
# for i in name:
#     print (f'labas, {name}')

#print('##############################################################################################################')
# 10.Susikurkite tokį ciklą: for elementas in [88, 65, 21, 26, 47]
# Iš duotų skaičių išveskite visus skaičius, kurie yra lyginiai.
# for elementas in [88, 65, 21, 26, 47]:
#     if elementas % 2 == 0:
#         print(elementas)
#print('##############################################################################################################')
# 11.Leiskite vartotojui nurodyti rėžių pradžią, pabaigą, žingsnį. Taip pat, kokius
# skaičius jis nori matyti (lyginius ar nelyginius). Patikrinkite ar rėžiai tinkami,
# jei taip vykdykite ciklą, kuris eitų per nurodytą rėžių, darant atitinkamą
# žingsnį. Išveskite tik tokius skaičius kokius vartotojas pasirinko (lyginius
# arba nelyginius).
# a = int(input('rezis a = '))
# b = int(input('rezis b = '))
# z = int(input('zigsnis = '))
# chose=int(input('lyginis = 0, neliginis = 1: '))
# if a < b and z > 0 and (chose == 0 or chose == 1):
#     print(f'{a} < {b}: {a < b}')
#     for i in range(a, b, z):
#         if i % 2 == 0 and chose == 0:
#             print(f'{i} - lyginis')
#         elif chose == 1 and i % 2 != 0 :
#             print(f'{i} - nelyginis')
# else:
#     print(f'{a} < {b}: {a < b}')


#print('##############################################################################################################')
# 12.Su for pagalba, pamėginkite išvesti tokią eglutę:
# *
# **
# ***
# ****
# *****
# (papildomai) leiskite vartotojui pasirinkti kokio dydžio eglutė turėtų būti
# išvesta.
# a = int(input('Eglutes auk6tis = '))
# for i in range(1,a+1):
#     print('*'*i)

#print('##############################################################################################################')
# 13.Leiskite vartotojui įvesti bet kokį žodį, bei pasirinkti po kiek kartų turėtų
# būti pakartojama kiekviena raidė. Su ciklo pagalba išveskite kiekvieną
# raidę iš žodžio atskiroje eilutėje, taip pat, tą raidę eilutėje kartokite tiek
# kartų kiek pasirinko vartotojas (16 pvz).
# word = input ('iveskit betkoki zodi: ')
# r = int(input('kiek kartuoti kiekviena raide: '))
# for l in word:
#     print(l * r)
    
#print('##############################################################################################################')
# 14.(papildomai, sunkiau) Be daugybos veiksmo programoje, sudauginkite du
# skaičius.
sk1 = int(input('sk1: '))
sk2 = int(input('sk2: '))
res = 0
for i in range(sk2):
    res += sk1
print(f'{sk1} * {sk2} = {res}')