########################################################################################################################
# 1. Susikurkite list vardams saugoti ir užpildykite jį informacija. Išveskite visą
# šį list, tuomet pirmą narį iš jo, paskutinį narį, bei kiek narių jame yra.
# nameList = ['Jonas', 'Petras', 'Tadas', 'Ana', 'Katia']
# print(nameList)
# print(nameList[0])
# print(nameList[len(nameList)-1])
# print(f'Nariu yra: {len(nameList)}')

# print('###############################################################################################################')
# 2. Susikurkite list žmonių ūgiams saugoti ir užpildykite jį informacija.
# Išveskite viso šio list duomenis bei kiek ūgių turite.
# humansHeight = [175, 189, 205, 165, 159]
# print(humansHeight)
# print(len(humansHeight))

# print('###############################################################################################################')
# # 3. Susikurkite list pažymiams saugoti. Pamėginkite sukurti programą, kur
# # vartotojas galėtų suvesti norimą kiekį naujų duomenų. Galiausiai išveskite
# # visus pažymius ir jų kiekį.
# raw_marks= input('Suveskite pazimius per tarpa:')
# marks = list(map(int,raw_marks.split(' ')))
# print(f'visi pazimiai: {marks}')
# print(f'pazimiu kiekis: {len(marks)}')

# print('###############################################################################################################')
# 4. Susikurkite miestų sąrašą. Į šį list pridėkite duomenų kurdami patį list.
# Toliau sukurkite galimybę vartotojui papildyti list. Išveskite tiek pradinį list,
# tiek papildytą duomenimis. Pamėginkite papildyti programą, kad
# vartotojas galėtų pasirinkti į kurią list vietą būtų įrašytas naujas miestas.
# towns = ['Vilnius', 'Kaunas', 'Ryga']
# towns.append('Talin')
# print(towns)
# towns.append(input('Iveskite miesto pavadinima: '))
# print(towns)
# ind = int(input(f'i kuria pozicija norite pridet miesta nuo 0 iki {len(towns)}: '))
# towns.insert(ind, input('Iveskite miesto pavadinima: '))
# print(towns)

# print('###############################################################################################################')
# 5. Sukurkite pasirinktą list ir užpildykite jį duomenimis. Iš jo pašalinkite
# keletą įrašų, tiesiog parašant pop() funkciją. Taip pat, sukurkite, kad
# vartotojas galėtų pasirinkti kiek dar duomenų pašalinti ir pašalinkite iš list
# pasirinktą kiekį įrašų.
# list = ['Vilnius', 'Kaunas', 'Ryga', 'aaa', 'bbb', 'ccc', 'ddd']
# print(list)
# list.pop()
# list.pop()
# print(list)
# ind = int(input(f'kiek elementu pasalint (max {len(list)}): '))
# list = list[:-ind]
# print(list)



# print('###############################################################################################################')
# 6. Sukurkite list su pasirinktais duomenimis. Patikrinkite ar sąraše yra
# daugiau nei 5 įrašai ir jeigu taip - jį išvalykite (clear funkcija).
# list = ['Vilnius', 'Kaunas', 'Ryga', 'aaa', 'bbb', 'ccc', 'ddd']
# print(list)
# if len(list) > 5:
#     list.clear()
# print(list)

# print('###############################################################################################################')
# 7. Sukurkite list, kuriame būtų surašyti bet kokie žodžiai. Leiskite vartotojui
# atlikti paiešką tame sąraše - vartotojas įvestų norimą žodį ir programa
# pasakytų ar tame sąraše tas žodis yra ir jeigu yra, tai kurioje vietoje.
# list = ['Vilnius', 'Kaunas', 'Ryga', 'aaa', 'bbb', 'ccc', 'ddd']
# search_word = input(f'Kuo ieškom: ')
# if search_word in list:
#     print(f'Radom! Pozicija: {list.index(search_word)}')
# else:
#     print(f'Neradom :(')

# print('###############################################################################################################')
# 8. Sukurkite sąrašą, kuriame būtų surašyti studentų pažymiai. Galite
# padaryti taip, kad pasirinktą kiekį pažymių galėtų suvesti pats vartotojas.
# Programa turi pasakyti kiek dešimtukų studentas turi.
# raw_marks= input('Suveskite pazimius per tarpa (nuo 0 iki 10):')
# marks = list(map(int,raw_marks.split(' ')))
# print(f'Turim {marks.count(10)} dešimtuku.')

# print('###############################################################################################################')
# 9. Susikurkite automobilių markių sąrašą ir užpildykite jį duomenimis
# (kuriantis sąrašą arba su vartotojo įvestimi). Išveskite turimus duomenis
# ekrane. Tuomet surikiuokite automobilių markes didėjimo tvarka ir
# išveskite. Taip pat, surikiuokite mažėjimo tvarka ir išveskite.

#raw_cars = input('Surašikite automobilius modelius per \',\':')
# raw_cars = 'opel,kia,audi,vw,man,volvo,lexus,toyota'
# cars = list(map(str,raw_cars.split(',')))
# print(cars)
# cars.sort()
# print(cars)
# cars.reverse()
# print(cars)

# print('###############################################################################################################')
# 10.Susikurkite studento pažymių sąrašą ir užpildykite duomenimis. Išveskite
# tris didžiausius turimus pažymius.

# raw_marks= input('Suveskite pazimius per tarpa (nuo 0 iki 10):')
# marks = list(map(int,raw_marks.split(' ')))
# print(marks)
# marks.sort()
# print(marks[-3:])


# print('###############################################################################################################')
# 11.Susikurkite studentų pažymių sąrašą ir užpildykite duomenimis. Jeigu
# studentas turi neigiamų pažymių (1, 2, 3, arba 4), išveskite kiek tokių
# pažymių jis turi.
# #raw_marks= input('Suveskite pazimius per tarpa (nuo 0 iki 10):')
# raw_marks = '5 10 6 10 2 3 5 9'
# marks = list(map(int,raw_marks.split(' ')))
# print(marks)
# if 1 in marks or 2 in marks or 3 in marks or 4 in marks:
#     print('yra neigiamu')
#     if 1 in marks:
#         c = marks.count(1)
#         print(f'1 yra: {c}')
#     if 2 in marks:
#         c = marks.count(2)
#         print(f'2 yra: {c}')
#     if 3 in marks:
#         c = marks.count(3)
#         print(f'3 yra: {c}')
#     if 4 in marks:
#         c = marks.count(4)
#         print(f'4 yra: {c}')
# else:
#     print(f'visi pazimiai teigiami')

# [start:stop]
# [start:stop:stepover]
# print('###############################################################################################################')
# 12.Susikurkite pasirinktą sąrašą su duomenimis. Pritaikykite list slicing tokiais
# būdais ir gautus atsakymus išveskite:

# list = ['Vilnius 0', 'Kaunas 1', 'Ryga 2', 'aaa 3', 'bbb 4', 'ccc 5', 'ddd 6']
# print(list)
# print('1. Paimkite pirmus tris narius.') # [start:stop]
# print(list[:2])
# print('2. Paimkite du narius, pradedant trečiu.')
# print(list[3:3+2])
# print('3. Paimkite paskutinius keturis narius.')
# print(list[-4:])
# print('4. Paimkite kas antrą narį, pradedant trečiu nariu.') # [start:stop:stepover]
# print(list[3::2])
# print('5. Paimkite visus atbuline tvarka.')
# print(list[::-1])

# print('###############################################################################################################')
# 13.Susikurkite list studentų vidurkiams saugoti. Išsitraukite ir pasidėkite į
# atskirą list tris didžiausius pažymius (galite surikiuoti ir išsikirpti ką reikia).
# list slicing

#raw_marks= input('Suveskite pazimius per tarpa (nuo 0 iki 10):')
# raw_marks = '5 10 6 10 2 3 5 9'
# marks = list(map(int,raw_marks.split(' ')))
# print(marks)
# marks.sort()
# print(marks[-3:])
# top3_marks = marks[-3:]
# print(top3_marks)

# print('###############################################################################################################')
# 14.Pamėginkite sukurti žodžių žodyną. Šį žodyną turėtų užpildyti vartotojas,
# įvesdamas visus norimus žodžius. Po kiekvieno įvedimo jam turėtų būti
# parodomi visi žodžiai, tačiau surikiuoti, t.y. įdėjus žodį į sąrašą, jį
# surikiuokite iš naujo.
# words =[]
# enter = True
# while enter:
#     word = input('Pridet zodi i zodina (norit baigti irashikit exit): ')
#     if word == 'exit':
#         enter = False
#     else:
#         words.append(word)
#         words.sort()
#         print (words)
# print(words)


#print('##############################################################################################################')
# 15.Sukurkite sąrašą, kuriame saugotumėte sandėlio likučius. Į atskirą sąrašą
# persikelkite visus likučius kurių lieka mažai (mažiau nei 5 vnt. arba trijų
# prekių likučius, kurių likę mažiausiai).
# stockBalance = [
#     ['bulves', 10],
#     ['morkos', 7],
#     ['svogunas', 6],
#     ['obuolis', 6],
#     ['bananas', 15],
#     ['chesnakas',10]
# ]
# orderList=[]
#
# for item in stockBalance:
#     if item[1] < 5:
#         orderList.append(item)
#
# if len(orderList) == 0:
#     sortedStockBalance = sorted(stockBalance, key=lambda quantity: quantity[1])
#     orderList.append(sortedStockBalance[0:3])
#
# print (orderList)
#print('##############################################################################################################')
# 16.Susikurkite norimą sąrašą su duomenimis. Išveskite šį sąrašą šiais
# pavidalais:
# list = ['Vilnius 0', 'Kaunas 1', 'Ryga 2', 'aaa 3', 'bbb 4', 'ccc 5', 'ddd 6']
# # 1. Kiekvieną elementą atskirant kableliu ir tarpu: pirmas, antras, trečias, ...
# sentence1=', '.join(list)
# print(f'1: {sentence1}')
# # 2. Kiekvieną elementą atskiriant vertikaliu brūkšneliu: pirmas|antras|trečias|...
# sentence2='|'.join(list)
# print(f'2: {sentence2}')
# # 3. Kiekvieną elementą atskiriant tarpu: pirmas antras trečias
# sentence3=' '.join(list)
# print(f'3: {sentence3}')

#print('##############################################################################################################')
# 17.Pabandykite atlikti list unpacking. Sąraše sudėkite informaciją ir iškart
# padarykite list unpacking. Tai atlikus išsiveskite gautas reikšmes.
# Pavyzdžiui, sąraše galėtų būti taip pateikta informacija:
# 1. pirmoje vietoje - naudojama programavimo kalba
# 2. antroje vietoje - aplinka (desktop, web, ...)
# 3. likusiose vietose nuo trečios - failai, su kuriais būtų dirbama
#list = ['Python', 'Database', 'Lists_20241014.py', 'Loop.py', 'extract.py']
# programingLanguage, environment, *files = ['Python', 'Database', 'Lists_20241014.py', 'Loop.py', 'extract.py']
# print(programingLanguage)
# print(environment)
# print(files)

#print('##############################################################################################################')
# 18.Susikurkite sąrašą projekto komandos narių vardams ir pavardėms
# saugoti. Išveskite tekstą "prie projekto dirba šie komandos nariai:" ir iškart
# po to kiekvieną komandos narį atskiroje eilutėje.
# workers = ['Linas Adomaitis', 'Kstas Medinskas', 'Aistis Kibiraitis']
# print('prie projekto dirba šie komandos nariai: ')
# for worker1 in workers:
#     print(worker1)

#print('##############################################################################################################')
# 19.Susikurkite sąrašą, kuriame būtų saugomos jau praeitos Python temos.
# Išveskite tekstą "mes jau mokėmės:". Ir iškart po to atskirose eilutėse
# visas temas, tačiau jas sunumeruokite "1-a tema:", "2-a tema:" ir t.t. Tai
# pamėginkite atlikti tiek su for ciklu, tiek su while ciklu.
# list = ['kintamieji', 'Saliginiai sakinia', 'ciklai', 'sarasai']
# indeks=0
# print ('mes jau mokėmės:')
# for indeks in range(len(list)):
#    print(f'{indeks+1}-a tema: {list[indeks]}')
#
# print('---')
# indeks=0
# while indeks < len(list):
#     print(f'{indeks+1}-a tema: {list[indeks]}')
#     indeks += 1

#print('##############################################################################################################')
# 20.Susikurkite masyvą studijų programų pavadinimams saugoti. Užpildykite
# šį masyvą duomenimis. Išveskite kiekvieną studijų programą atskiroje
# eilutėje.
# list = ['kintamieji', 'Saliginiai sakinia', 'ciklai', 'sarasai']
# for item in list:
#     print(item)

#print('##############################################################################################################')
# 21.Susikurkite masyvą šalių pavadinimams saugoti ir jį užpildykite
# duomenimis. Išveskite šalių pavadinimus atskirose eilutėse, su prierašu
# "šalis" ir tada nurodant šalį iš masyvo.
# countries = ['USA', 'UK', 'Finland', 'Latvia', 'Estija']
# for country in countries:
#     print(f'Šalis {country}.')

#print('##############################################################################################################')
# 22.Susikurkite sąrašą prekių krepšeliui saugoti. Išveskite kiek prekių
# krepšelyje yra narių. Tuomet išveskite visą prekių krepšelio informaciją,
# nurodant kelinta prekė, pvz "nr 1 pirkinys:", "nr 2 pirkinys:" ir t.t.
# shopingList = ['pienas', 'duona', 'manai', 'sorai', 'suris']
# print(f'krep6eli sudaro {len(shopingList)} prekiu')
# i = 0
# for i in range(len(shopingList)):
#    print(f'nr {i+1} pirkinys: {shopingList[i]}')

#print('##############################################################################################################')
# 23.Susikurkite pažymių sąrašą ir užpildykite jį informacija. Surikiuokite
# pažymius nuo didžiausio iki mažiausio. Išveskite visus turimus pažymius
# atskirose eilutėse. Prie kiekvieno pažymio taip pat prirašykite "puikiai",
# jeigu jis yra 10, "labai gerai", jeigu jis yra 9 ir t.t.
# marks=[10, 9, 8, 10, 1, 6, 3, 2, 8, 5]
# marks.sort(reverse=False)
# print(marks)
# for (mark) in marks:
#    print (f'{mark} ', end ='')
#    if mark == 10:
#       print('Puikiai')
#    elif mark == 9:
#       print('labai gerai')
#    elif mark == 8:
#       print('Gerai')
#    elif mark == 7:
#       print('Patenkinamai')
#    elif mark == 6:
#       print('Tenka pasistengti.')
#    elif mark <= 5:
#       print('Nepakankamai')
#print('##############################################################################################################')
# 24.Susikurkite programą, kurioje vartotojas galėtų nusakyti kiek atsitiktinių
# skaičių turėtų būti sugeneruota. Tuomet programa turėtų būtent tokį kiekį
# atsitiktinių skaičių sugeneruoti ir sudėti į sąrašą. Išveskite visus šiuos
# skaičius ekrane. Tuomet tuos pačius skaičius išveskite ekrane dar kartą,
# tačiau viską spausdinkite atskirose eilutėse, eilutėje nurodant patį skaičių
# ir jo kvadratą.
# import random
# # tuscias list
# numbers = []
# # skaiciu generavimas
# size = int(input("kiek skaiciu norite: "))
# for i in range(size):
#    numbers.append(random.randint(10, 100))
# print(numbers)
# for number in numbers:
#    print (f'sk: {number}, to skai2iaus kvdratas {number * number}')

#print('##############################################################################################################')
# 25.Susikurkite norimą sąrašą su duomenimis. Išsiveskite viso šio sąrašo
# informaciją. Pakeiskite trijų pasirinktų narių reikšmes į kitas. Išsiveskite
# pakeisto sąrašo informaciją.
# import random
# shopingList = ['pienas', 'duona', 'manai', 'sorai', 'suris']
# print(shopingList)
# for i in range(3):
#    change = random.randint(0, len(shopingList)-1)
#    if i ==0:
#       shopingList[change] = 'bananai'
#    if i ==1:
#       shopingList[change] = 'kokosai'
#    if i ==2:
#       shopingList[change] = 'šokoladas'
# print(shopingList)
#print('##############################################################################################################')
# 26.Susikurkite sąrašą ir jį užpildykite skaičiais (savarankiškai arba
# atsitiktiniais). Iš pradžių išveskite tekstą "lyginiai skaičiai" ir visus lyginius
# skaičius. Tuomet išveskite tekstą "visi nelyginiai skaičiai" ir visus nelyginius
# skaičius. Bei ant galo tekstą "visi skaičiai, kurie dalinasi iš 3" ir visus
# skaičius, kurie atitinka tokią sąlygą.
# import random
# # tuscias list
# numbers = []
# # skaiciu generavimas
# size = int(input("kiek skaiciu norite: "))
# for i in range(size):
#    numbers.append(random.randint(10, 100))
# print(numbers)
# lyginiai = []
# nelyginiai = []
# dalinasiIs3 = []
# for number in numbers:
#    if number % 2 == 0:
#       lyginiai.append(number)
#    else:
#       nelyginiai.append(number)
#    if number % 3 == 0:
#       dalinasiIs3.append(number)
# print(f'Visi  lyginiai  skaičiai: {lyginiai}')
# print(f'Visi nelyginiai skaičiai: {nelyginiai}')
# print(f'visi skaičiai, kurie dalinasi iš 3: {dalinasiIs3}')



#print('##############################################################################################################')
# 27.Susikurkite sąrašą ir jį užpildykite atsitiktiniais skaičiais. Išveskite visus
# skaičius didesnius nei vidurkis.
# import random
# # tuscias list
# numbers = []
# # skaiciu generavimas
# size = int(input("kiek skaiciu norite: "))
# for i in range(size):
#    numbers.append(random.randint(1, 100))
# print(numbers)
# suma = 0
# for number in numbers:
#    suma += number
# avg_number=suma/len(numbers)
# print(avg_number)
# largerThanAverage=[]
# for number in numbers:
#    if number > avg_number:
#       largerThanAverage.append(number)
# print(largerThanAverage)

#print('##############################################################################################################')
# 28.Susikurkite programą, kurioje būtų sukurtas sąrašas iš pasirinkto kiekio
# atsitiktinių skaičių. Raskite kiekvieno skaičiaus daliklius, pavyzdžiui:
# skaičius 2 dalinasi iš 2
# skaičius 3 dalinasi iš 3
# skaičius 4 dalinasi iš 2, 4
# skaičius 5 dalinasi iš 5
# skaičius 6 dalinasi iš 2, 3, 6
# import random
# # tuscias list
# numbers = []
# # skaiciu generavimas
# size = int(input("kiek skaiciu norite: "))
# for i in range(size):
#    numbers.append(random.randint(1, 20))
# print(numbers)
#
# for number in numbers:
#     divisible = []
#     for i in range(1,number+1):
#         #print(f'i = {i} | number = {number}')
#         if number % i == 0:
#             divisible.append(i)
#     if len(divisible) > 0:
#         print(f'skaičius {number} dalinasi iš: ', end='')
#         print(', '.join(map(str, divisible)))
#         # for div_num in divisible:
#         #     print(f'{div_num} ',end='')

#print('##############################################################################################################')
# 29.Sukurkite programą, kurioje vartotojas galėtų įvesti norimą kiekį žodžių
# (pasirenka iš pradžių ir vykdomas for iki to kiekio skaičiaus, arba
# vykdomas while kol neįveda q ar kokio kito simbolio/žodžio). Išveskite
# visus šiuos žodžius ekrane.

# tuscias list
words = []
# skaiciu generavimas
size = int(input("kiek zodziu norite ivesti: "))
for i in range(size):
    word = str(input(f'iveskit {i+1} zodi is {size}: '))
    words.append(word)

print(', '.join(map(str, words)))


#print('##############################################################################################################')
# 30.Susikurkite sąrašą iš pasirinktų žodžių. Atskirose eilutėse išveskite patį
# žodį, jo raidžių kiekį.

#print('##############################################################################################################')
# 31.Susikurkite pažymių sąrašą. Šiuos pažymius leiskite įvesti vartotojui.
# Baigus įvedimą, išveskite suvestų pažymių vidurkį. Taip pat, jeigu
# studentas turėjo neigiamų pažymių, tuomet atskirai parodykite tuos
# neigiamus pažymius ir jų kiekį.

#print('##############################################################################################################')
# 32.Susikurkite žodžių sąrašą. Raskite ir išveskite trumpiausią ir ilgiausią
# žodžius, bei jų raidžių kiekius.

#print('##############################################################################################################')
# 33.Sugeneruokite 100-ą atsitiktinių skaičių ir sukelkite visus tuos skaičius į
# sąrašą. Atlikite šiuos veiksmus:
# 1. Raskite mažiausią skaičių, didžiausią skaičių, bei vidurkį.
# 2. Tuomet atrinkite į atskirą sąrašą skaičius, kurie žemesni nei vidurkis. Raskite šių skaičių
# vidurkį.
# 3. Taip pat, atrinkite į dar vieną sąrašą skaičius, kurie didesni nei vidurkis. Raskite šių skaičių
# vidurkį.
# 4. Ekrane išveskite pradinius duomenis, mažiausią ir didžiausią skaičius, rastą vidurkį,
# pirmus atrinktus skaičius ir jų vidurkį, antrus atrinktus skaičius ir jų vidurkį.

#print('##############################################################################################################')
# 34.Susikurkite žodžių masyvą. Išveskite per kiek simbolių yra ilgesnis
# ilgiausias žodis už trumpiausią. Tarkime ilgiausias yra “kompiuteris” (11
# simbolių), o trumpiausias “medis” (5), skirtumas tarp jų 11 - 5 = 6
# simboliai.

#print('##############################################################################################################')
# 35.Susikurkite dviejų studentų pažymių sąrašus. Šią informaciją leiskite
# suvesti vartotojui. Raskite kurio studento vidurkis yra geresnis. Taip pat,
# ar kuris iš jų (ar abu) turi neigiamų pažymių.

#print('##############################################################################################################')
# 36.Susikurkite skaičių masyvą ir užpildykite jį atsitiktiniais skaičiais. Raskite
# visų skaičių, kurie dalinasi iš 4 sumą.

#print('##############################################################################################################')
# 37.Susikurkite skaičių masyvą ir užpildykite jį duomenimis. Išveskite visus
# skaičius atskirose eilutėse. Prie kiekvieno lyginio skaičiaus dar išvedant jo
# kvadratą.

#print('##############################################################################################################')
# 38.Susikurkite studento pažymių sąrašą ir užpildykite jį duomenimis
# (atsitiktiniais arba kokius įrašysite). Išveskite kiekvieną pažymį atskiroje
# eilutėje. Prie kiekvieno pažymio nurodykite ar tai teigiamas, ar neigiamas
# pažymys. Taip pat, jeigu neigiamas pažymys, tuomet dar nurodykite kiek
# balų trūko iki teigiamo pažymio. Teigiamas pažymys skaitosi 5 balai.

#print('##############################################################################################################')
# 39.Susikurkite žodžių sąrašą ir užpildykite duomenimis. Išveskite visus
# žodžius ekrane, nurodant iš kiek raidžių kiekvienas šis žodis yra sudarytas.
# Papildykite programą taip, kad rastumėte visų raidžių kiekį (pvz yra žodžiai
# "medis" ir "alus", 5 ir 4 raidės atitinkamai, o jas sudėjus gaunasi 9 raidės).

#print('##############################################################################################################')
# 40.Susikurkite skaičių sąrašą ir užpildykite duomenimis. Raskite visų skaičių,
# kurie dalinasi iš 3 sumą ir vidurkį. Išveskite pradinius duomenis ir gautus
# atsakymus.

#print('##############################################################################################################')
# 41.Susikurkite sąrašą failų pavadinimams saugoti, užpildykite jį duomenimis.
# Įsivaizduokite kad jums reikės nuskaityti šiuos failus, todėl pirma norėsite
# patikrinti su kuriais galite dirbti. Atrinkite į atskirą sąrašą tik tuos failus,
# kurių galūnė yra .txt arba .json tipo. Išveskite atrinktus duomenis.

#print('##############################################################################################################')
# 42.Susikurkite sąrašą įvykusių klaidų kodams saugoti ir užpildykite šį masyvą
# duomenimis. Tuomet išveskite visas sukauptas klaidas administratoriui,
# taip, kad jis suprastų kas per klaidos įvyko. Pavyzdžiui, jeigu yra kodas
# "ui87", tai kad išvestų "Grafinės sąsajos klaida navigacijoje", arba jeigu
# kodas "sys12", tuomet "Trūksta operatyviosios atminties sistemoje" ir
# pan.

#print('##############################################################################################################')
# 43.Susikurkite sąrašą sandėlio likučiams saugoti (kiekvienas atskiras narys
# sąraše yra atskiros prekės likutis). Su kiekvienu likučiu paskaičiuokite per
# kiek dienų bus išpirktas, jei per dieną vidutiniškai yra nuperkami 5 vnt.
# Išveskite atsakymus atskirose eilutėse, nurodant kiek yra dabar ir kiek
# dienų užteks jo. Pavyzdžiui, jeigu yra likučiai 74, 54 ir 32, tai 74 vnt. prekės
# užteks maždaug 15 dienų, 54 vnt. prekės užteks maždaug 11 dienų ir t.t.
# Pabandykite papildyti programą taip, kad į atskirą sąrašą atrinktų tas
# prekes, kurių užteks savaitei ar mažiau, jas išveskite atskirai, pačioje
# pabaigoje.

#print('##############################################################################################################')
# 44.Susikurkite sąrašą norimiems žodžiams saugoti. Užpildykite šį sąrašą
# duomenimis. Į kitą sąrašą atrinkite tuos žodžius, kurie yra trumpi (sudaro
# mažiau nei 5 raidės). Išveskite pradinius duomenis ir atrinktus.