# https://docs.google.com/document/d/1rAvAekfM4C0THQ_TJ49Su7kuUgGStYYj2ZQpXSW1o6Q/edit?tab=t.0
#print('##############################################################################################################')
# 1. Sukurkite Funkciją kuri priima du int tipo kintamuosius. Juos susumuoja ir atspausdina.
# def fun_sum(a,b):
#     return a+b
#
# print(fun_sum(5,5))
from copyreg import pickle
from random import random


#print('##############################################################################################################')
# 2. Sukurkite Funkciją kuri vadinasi PISq. Funkcija gražina float tipo reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.
def PISq ():
    return float(9.8596)
print(PISq())
print(type(PISq()))

print('##############################################################################################################')
# 3. Sukurkite Funkciją kuri priima du int tipo kintamuosius. Funkcija gražina skaičių sandaugą.; Gautą reikšmę atspausdinkite.
def fun_multi(a,b):
    return a*b

print(fun_multi(3,5))
print('##############################################################################################################')
# 4. Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina kiekvieną narį vienoje eilutėje.
def print_list (list1):
    for i in list1:
        print(i)
list = ['pienas', 'duona', 'manai', 'sorai', 'suris', 5, 7]
print_list(list)
print('##############################################################################################################')
# 5. Sukurkite Funkciją kuri priima du int tipo kintamuosius, min ir max reikšmėms nustatyti ir sugeneruoja random int
# skaičių ir jį gražintų.
import random

def int_rang (a, b):
    if a > b :
        mini = b
        maxi = a
    else:
        mini = a
        maxi = b
    return random.randint(mini,maxi)

print(int_rang(15, 100))

print('##############################################################################################################')
# 6. Sukurkite Funkciją kuri sugeneruotų random int skaičių masyvą ir jį gražintų. Funkcija priima tris int tipo
# kintamuosius, min, max ir length reikšmėms nustatyti.
import random

def int_rand_list (min, max, length):
    res_list=[]
    for i in range(length):
        res_list.append(random.randint(min,max))
    return res_list
print (int_rand_list(10, 100, 10))

print('##############################################################################################################')
# 7. Sukurkite Funkciją kuri panaudotų 6toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį),
# susumuotų ir gražintų reikšmę.
def sum_list (list1):
    sum_1 = 0
    print(list1)
    for item in list1:
        sum_1 += item
    return sum_1
print(sum_list(int_rand_list(10, 20, 3)))

print('##############################################################################################################')
# 8. Sukurkite Funkciją kuri priimtų 6toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį (double).
def avg_list (list2):
    return sum_list(list2) / len(list2)

result = avg_list(int_rand_list(10, 20, 3))
print(result)

print('##############################################################################################################')
# 9. Sukurkite Funkciją kuri priimtų du int skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis.
# Pirmas int - išoriniam ciklui, antras vidiniam.
def rectangle (x, y):
    for ix in range(x):
        print('X'*y)

rectangle(3,50)

print('##############################################################################################################')
# 10. Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų.
# Sakinys - “Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį)
def count_w_and_l (sentence):
    print(f'tarpu yra: {sentence.count(' ')}')
    print(f'raidžių(simbolių) yra: {len(sentence) - sentence.count(' ')}')

sentence= 'Šiandien labai graži diena'
count_w_and_l(sentence)

print('##############################################################################################################')
# 11. Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų. Kodavimas - sakinį apsukame iš kitos pusės.
# Pvz “Naglis” turi gautis “silgaN”.
def code1 (sentence1):
    return sentence1[::-1]
print(code1(sentence))
