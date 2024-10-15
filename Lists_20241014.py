########################################################################################################################
# 1. Susikurkite list vardams saugoti ir užpildykite jį informacija. Išveskite visą
# šį list, tuomet pirmą narį iš jo, paskutinį narį, bei kiek narių jame yra.
# nameList = ['Jonas', 'Petras', 'Tadas', 'Ana', 'Katia']
# print(nameList)
# print(nameList[0])
# print(nameList[len(nameList)-1])
# print(f'Nariu yra: {len(nameList)}')
from operator import truediv

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
stockBalance = [
    ['bulves', 10],
    ['morkos', 7],
    ['svogunas', 6],
    ['obuolis', 6],
    ['bananas', 15],
    ['chesnakas',10]
]
orderList=[]

for item in stockBalance:
    if item[1] < 5:
        orderList.append(item)

if len(orderList) == 0:
    sortedStockBalance = sorted(stockBalance, key=lambda quantity: quantity[1])
    orderList.append(sortedStockBalance[0:3])

print (orderList)
    

