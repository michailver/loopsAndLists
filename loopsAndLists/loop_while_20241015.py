# 1. Išveskite visus skaičius nuo 1 iki 20.
# i=1
# while i < 21:
#     print(i)
#     i += 1

#print('##############################################################################################################')
# 2. Išveskite visus skaičius nuo 1 iki 50. Prie kiekvieno lyginio skaičiaus
# parašykite žodį "lyginis", o prie kiekvieno nelyginio – "nelyginis".
# i=1
# while True:
#     if i % 2 == 0:
#         print(f'{i} - lyginis')
#     else:
#         print(f'{i} - nelyginis')
#     if i == 50:
#         break
#     i += 1

#print('##############################################################################################################')
# 3. Išveskite visus skaičius nuo 25 iki 50. Vietoj skaičių, kurie dalinasi iš 3
# išveskite tekstą "dalinasi iš 3".
# i=25
# while i < 50+1:
#     if i % 3 ==0:
#         print(f'{i} - dalinasi iš 3')
#     else:
#         print(i)
#     i += 1

#print('##############################################################################################################')
# 4. Išveskite visus skaičius nuo 1 iki 100 arba iki tol kol pasitaikys toks, kuris
# dalinasi iš 7.
# i = 1
# while True:
#     print(i)
#     if i > 100 or i % 7 == 0:
#         print (f'{i} dalinasi is 7 arba didesnis uz 100')
#         break
#     i += 1

#print('##############################################################################################################')
# 5. Išvedinėkite visus skaičius nuo 1 iki tol kol pasitaikys skaičius, kuris
# dalinasi iš 3 ir iš 5.
# i = 1
# while True:
#     print(i)
#     if i % 3 == 0 and i % 5 == 0:
#         print (f'{i}: dalinasi iš 3 ir iš 5')
#         break
#     i += 1

#print('##############################################################################################################')
# 6. Vartotojas turi suvesti rėžių pradžią ir pabaigą. Tačiau jūs turite patikrinti
# ar nurodyti rėžiai yra geri (pradžia mažesnė už pabaigą). Liepkite
# vartotojui kartoti įvedimą tol, kol rėžiai jau bus įvesti tinkamai. Turint
# tinkamus rėžius, išveskite visus skaičius nuo rėžių pradžios iki pabaigos
# (šitam jau vietoj while galite naudoti for ciklą), šalia kiekvieno skaičiaus
# išvedant jo kvadratą, bei ar jis lyginis/nelyginis.
# while True:
#     print('turi atitikt saliga a < b')
#     a = int(input('rezis a = '))
#     b = int(input('rezis b = '))
#     if a >= b:
#         print ('saliga neivikdyta')
#     else:
#         break
# for i in range(a, b):
#     if i % 2 == 0:
#         print (f'skaicius: {i} | sk. kvadratas: {i * i} | lyginis')
#     else:
#         print (f'skaicius: {i} | sk. kvadratas: {i * i} | nelyginis')
#print('##############################################################################################################')
# 7. Išveskite visus skaičius nuo 1 iki kol pasitaikys toks, kuris yra pirminis ir
# yra didesnis nei 20.
# Pirminis skaičius yra bet kuris natūralusis skaičius, didesnis nei 1, kuris dalijasi tik iš savęs ir vieneto.
# Kitaip tariant, tai skaičius, kurį galima padalyti be liekanos tik iš 1 ir jo paties.
# Pavyzdžiai: 2, 3, 5, 7, 11, 13 ir taip toliau yra pirminiai skaičiai.
# i = 1
# while True:
#     daliklis = 1
#     p=False
#     #print(f'while: {i}')
#     if i > 1:
#         for daliklis in range (2,i+1):
#             #print(f'for: {daliklis} | ', end='')
#             if i % daliklis == 0 and i != daliklis:
#                 # print (f'{i} dalinasi is {daliklis}: {i} / {daliklis} = {i/daliklis}')
#                 p = False
#                 break
#             else:
#                 # print (f'nesidalina be lekanos: {i} / {daliklis} = {i/daliklis}')
#                 p = True
#     if p:
#         print(i)
#     if i > 20:
#         break
#     i += 1

#print('##############################################################################################################')
# 8. Liepkite vartotojui įvedinėti bet kokius skaičius. Vykdykite įvedinėjimą iki
# kol įvestas skaičius bus lygus 0. Raskite įvestų skaičių sumą.
# suma = 0
# print ('ivedus 0 daugiau ivadinet nereikes')
# while True:
#     n = int(input(f'iveskit skaiciu: '))
#     if n == 0:
#         break
#     suma += n
# print(f'ivestu sk. suma lygi: {suma}')

#print('##############################################################################################################')
# 9. Leiskite vartotojui atlikti norimus skaičiavimus tiek kartų kiek jis nori.
# Pavyzdžiui, leiskite vartotojui įvesti du skaičius, tuomet jam parodykite
# pačius skaičius, veiksmus (sudėtis, atimtis, daugyba, dalyba) ir
# suskaičiuotus atsakymus (5 + 3 = 8; 5 - 3 = 2; ...). Kai atsakymai bus
# parodyti, vartotojas turi turėti galimybę pakartoti skaičiavimus, todėl
# leiskite pasirinkti ar dar kartoti veiksmą, ar jau programa turėtų baigti
# savo darbą.
# while True:
#     print('iveskit du skaičius')
#     a = int(input('rezis a = '))
#     b = int(input('rezis b = '))
#     print (f'{a}+{b}={a+b} | '
#            f'{a}-{b}={a-b} | '
#            f'{a}*{b}={a*b} | '
#            f'{a}/{b}={a/b}'
#            )
#     kartoti = input('Ar norite kartoti? (t/n): ')
#     if kartoti != 't':
#         print('Daugiau nebekartojama')
#         break
#print('##############################################################################################################')
# 10.Vartotojui išveskite pasirinkto skaičiaus daugybos lentelę (pvz, skaičiaus 5
# daugybos lentelė būtų 5 * 1 = 5; 5 * 2 = 10; 5 * 3 = 15; ...). Leiskite
# vartotojui kartoti veiksmą (tiek kartų kiek norės) ir gauti dar vieną
# daugybos lentelę su kitu pasirinktu skaičiumi.
# while True:
#     print('iveskit skaičius, nupe šiu jo daugibos lentele')
#     a = int(input('skaicius = '))
#     for i in range(10):
#         print(f'{a} * {i} = {a*i};')
#
#     kartoti = input('Ar norite kartoti? (t/n): ')
#     if kartoti != 't':
#         print('Daugiau nebekartojama')
#         break


#print('##############################################################################################################')
# 11.Liepkite vartotojui įvesti kiek jis nori skaičių. Įvedimą sustabdykite tuomet,
# kai vartototojas įves 0 ar -1, ar kitą jūsų pasirinktą skaičių ar simbolį.
# Raskite vartotojo įvestų skaičių sumą, vidurkį.
# suma = 0
# i = 0
# print ('ivedus 0 daugiau ivadinet nereikes')
# while True:
#     n = int(input(f'iveskit skaiciu: '))
#     if n == 0:
#         break
#     suma += n
#     i += 1
# print(f'ivestu sk. suma lygi: {suma}')
# print(f'ivestu sk. vidurkis lygi: {suma/i}')

#print('##############################################################################################################')
# 12.Sukurkite studentų pažymių vidurkių skaičiuoklę (kaip pavyzdį galite
# naudoti 17-ą pavyzdį). Tačiau tokia skaičiuoklė turėtų leisti skaičiuoti
# vidurkį ne tik iš vieno studento pažymių, bet leistų pakartoti pažymių
# įvedimą ir vidurkio skaičiavimą ant tiek studentų kiek reikia.
# while True:
#     stName = input('iveskite studento varda: ')
#     suma = 0
#     i = 0
#     while True:
#         n = int(input(f'iveskite {stName} pazimi: '))
#         suma += n
#         i += 1
#         kartoti1 = input('Ar tai visi studento pazimiai (t/n): ')
#         if kartoti1 != 'n':
#             print(f'Studento {stName} vidurkis lygi: {suma / i}')
#             break
#     kartoti1 = input('Ar dar bus kitu studentu (t/n): ')
#     if kartoti1 != 't':
#         print(f'Programa baigia darba')
#         break



#print('##############################################################################################################')
# 13.Sukurkite skaičiaus atspėjimo užduotį. Leiskite vartotojui pasirinkti
# žaidimo sudėtingumą (atsitiktinio skaičiaus rėžiai), ar suteikiamos
# pagalbos (skaičius mažesnis/didesnis nei spėjamas), kiek spėjimų
# leidžiama (neribotai, arba pvz iki 10 ėjimų), bei kiti pasirinkti parametrai.
# Vartotojas šiuos parametrus pasirenka žaidimo pradžioje. Turite užtikrinti,
# kad vartotojas pasirinko parametrus tik iš galimų - jeigu ne, liepkite
# įvedimą pakartoti.
import random


print('zaidimas atspek skaiciu.')
while True:
    print('Zaidimo rezia')
    s = int(input(f'Rezio pradzia: '))
    f = int(input(f'Rezio pabaiga: '))
    if s < f and f - s >= 2:
        break
    else:
        print('ERROR: kaz kas blogai su reziais iveskit dar karta')

while True:
    s_kiekis = int(input('kiek spejimu norit turet iveskitt skaiciu(0 - neribotai): '))
    if s_kiekis >= 1:
        neribotas = False
        break
    elif s_kiekis == 0:
        neribotas = True
        break
    else:
        print('ERROR: kaz kas blogai su spejimo kiekiu. skai2iu turi but >= 1')

slaptas = random.randint(s, f)
spejimas = None

while slaptas != spejimas:
    spejimas = int(input(f'Spekite skaiciu tarp {s} ir {f}: '))
    if slaptas > spejimas:
        print('Bandykite didesni')
    elif slaptas < spejimas:
        print('Bandykite mazesni')
    else:
        print('Atspejote!')
        break
    if neribotas == False:
        s_kiekis -= 1
        if s_kiekis > 0:
            print(f'Liko {s_kiekis} spejimu(-as, -ai)')
        else:
            print(f'Deja spejimu skai2iu baigesi. :(')
            break
    print('---')

