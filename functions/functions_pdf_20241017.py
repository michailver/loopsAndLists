# 1. Sukurkite funkciją, kuri išvestų jūsų vardą ir kodėl pasirinkote
# programavimą. Iškvieskite šią funkciją tris kartus.
def fun1 ():
    print('Michail')
    print('nes reikia darbo, ir aš jau ši beita moku šitoje srytije')

for i in range(3):
    fun1()

print('##############################################################################################################')
# 2. Sukurkite funkciją, kuri išvestų 5 eilučių eilėraštį. Iškvieskite šią funkciją 5 kartus.
def fun2 ():
    print(  'Šalta. Medžiai juodi, ir dangus kaip švinas.\n'
            'Lapai pabyra vieni, plėšomi vėjo.\n'
            'Nieko nėra! Nei saulės, nei giedrų dienų.\n'
            'Lengvas rūkas kyla ir nyksta virš žemės...\n'
            'Širdyje – ruduo.') #Salomėja Nėris – "Ruduo"

for i in range(5):
    fun2()

print('##############################################################################################################')
# 3. Sukurkite tris funkcijas, kur kiekviena išvestų skirtingus tekstus. Iškvieskite
# visas tris funkcijas po vieną kartą.
def fun31 ():
    print('fun31')
def fun32 ():
    print('fun32')
def fun33 ():
    print('fun32')
fun31()
fun32()
fun33()
print('##############################################################################################################')
# 4. Sukurkite dvi funkcijas, kur vienoje būtų viena teksto eilutėje, kitoje kita.
# Sukurkite trečią funkciją, kuri iškviestų pirmas dvi funkcijas. Iškvieskite šią
# trečiąją funkciją už visų funkcijų ribų.
def fun4 ():
    fun31()
    fun32()

fun4()
print('##############################################################################################################')
# 5. Sukurkite funkciją, kurios viduje sugeneruotumėte du atsitiktinius
# skaičius. Funkcijoje suskaičiuokite ir išveskite šių dviejų skaičių sumą,
# kartu išvedant ir patį atliekamą veiksmą (pvz 7 + 2 = 9). Iškvieskite šią
# funkciją keletą kartų.
import random
def fun5 ():
    a1 = random.randint(1, 9999)
    a2 = random.randint(1,9999)
    print(f'{a1} + {a2} = {a1+a2}')

for i in range(3):
    fun5()

print('##############################################################################################################')
# 6. Sukurkite ir iškvieskite funkciją, kurioje kintamuosiuose būtų saugoma
# informacija apie policininką (vardas, pavardė, amžius, alga, etatas,
# specializacija). Išveskite šią informaciją suformatuotai (pavyzdžiui įterpkite
# į sakinį, ar išveskite sąrašu ar pan.).
def fun6 (name, surname, age, salary, position, specialization):
    print(f'Policininkas {name} {surname}, {age} metų amžiaus, dirba {position} ir specializacija {specialization}, jo alga siekia {salary} eurų.')
fun6("Jonas","Petrauskas",35,1500,"serzantu","eismo priežiūra")

print('##############################################################################################################')
# 7. Sukurkite funkciją, kuri išvestų 10 atsitiktinių skaičių. Po visų išvestų
# skaičių turėtų padėti tuščią eilutę. Šią funkciją iškvieskite 5 kartus.
def fun7 ():
    for i in range(10):
        if i < 10:
            print (f'{i}: {random.randint(1, 9999)} ', end='')
    print('')

for i in range(5):
    fun7()

print('##############################################################################################################')
# 8. Sukurkite funkciją, kuri išvestų atsitiktinį skaičių. Už funkcijos ribų
# sukurkite ciklą, kurį būtų vykdomas 10 kartų. Iškvieskite sukurtą funkciją
# cikle. Turėtumėte pamatyti 10 atsitiktinių skaičių.
def fun5 ():
    a1 = random.randint(1, 9999)
    print(f'{i}: {a1}')

for i in range(10):
    fun5()

# 9. Sukurkite funkciją pasisveikinimui, šiai funkcijai per argumentus
# perduokite vardą, funkcijoje išveskite tekstą labas ir gautą vardą.
# Sukurkite kitą funkciją, kuri irgi per argumentus gautų vardą, tačiau
# pasakytų 'viso gero' ir patį vardą. Ne funkcijose susikurkite kintamąjį
# vardui saugoti ir įrašykite vardą. Iškvieskite abi funkcijas, perduodant
# kintamąjį joms.
# 10.Sukurkite funkciją, kuriai perduotumėte du skaičius. Ši funkcija turi rasti
# kuris skaičius yra didesnis ir išvesti gautą atsakymą, o jei skaičiai lygūs -
# tuomet išvesti, kad skaičiai lygūs. Iškvieskite šią funkciją keletą kartų,
# duodant skirtingus skaičius.
# 11.Sukurkite funkciją, kuri per argumentus gautų automobilių duomenis
# (markė, modelis, gamybos metai, darbinis tūris). Ši funkcija turėtų šiuos
# duomenis išvesti kaip nors gražiai formatuotai. Iškvieskite šią funkciją du
# kartus, perduodant skirtingus duomenis jai.
# 12.Sukurkite funkciją sumai skaičiuoti, ši funkcija per argumentus turėtų
# gauti du skaičius, bei išvesti patį veiksmą kartu su atsakymu (pvz 7 + 5 =
# 12). Sukurkite tokias pačias funkcijas skirtumui, sandaugai ir dalmeniui
# rasti. Sukurkite dar vieną funkciją, kuri sugeneruotų du atsitiktinius
# skaičius, bei iškviestų kitas 4 funkcijas, perduodant joms sugeneruotus
# skaičius. Šią bendrąją funkciją iškvieskite keletą kartų.
# 13.Susikurkite funkciją, kuri per argumentus priimtų žodžių masyvą.
# Funkcijoje išveskite visus žodžius iš masyvo atskirose eilutėse, nurodant
# žodžio ilgį (simbolių kiekį). Už funkcijos ribų susikurkite žodžių masyvą ir
# užpildykite jį duomenimis. Iškvieskite sukurtą funkciją perduodant turimą
# masyvą.
# 14.Susikurkite funkciją, kuri per argumentus priimtų skaičių masyvą. Funkcija
# turėtų atspausdinti visus skaičius, šalia jų išvedant to skaičiaus kvadratą ir
# jį padalintą iš dviejų. Už funkcijos ribų susikurkite du skaičių masyvus ir
# užpildykite jį duomenimis. Iškvieskite funkciją du kartus, kiekvieną kartą
# perduodant skirtingą turimą masyvą.
# 15.Susikurkite funkciją, kuri per argumentus priimtų pažymių masyvą, bei
# studento vardą su pavarde. Funkcija turėtų išvesti studento vardą ir
# pavardę, jo pažymius. Taip pat, suskaičiuoti vidurkį, bei jį išvesti. Už
# funkcijos ribų susikurkite reikiamus kintamuosius ir masyvus, arba
# objektus studentų pažymiams saugoti ir užpildykite juos duomenimis.
# Iškvieskite šią funkciją perduodant visus reikalingus duomenis.
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
# 17.Susikurkite funkciją, kuri grąžintų bet kokį jūsų norimą sakinį. Iškvieskite
# šią funkciją ir išspausdinkite gautus rezultatus.
# 18.Susikurkite funkciją, kuri grąžintų atsitiktinai sugeneruotą skaičių.
# Iškvieskite šią funkciją kelis kartus ir gautus atsakymus išveskite kokiu
# norite būdu.
# 19.Susikurkite funkciją, kuri per argumentus priimtų studento vardą ir
# vidurkį. Ši funkcija turėtų sugeneruoti iš to sakinį (pvz Studentas Tomas
# turi vidurkį 8.7) ir tai grąžinti kaip atsakymą. Iškvieskite šią funkciją bent
# porą kartų, perduodant vis skirtingus duomenis. Gautus atsakymus
# išveskite.
# 20.Susikurkite funkciją, kuri per argumentus gautų skaičių. Ji turėtų surasti
# duoto skaičiaus mažiausią daliklį (skaičių iš kurio dalinasi be liekanos). Už
# funkcijos ribų sukite ciklą nuo 10 iki 30 ir kiekvienoje ciklo iteracijoje
# iškvieskite šią funkciją, perduodant ciklo kintamąjį.
# 21.Susikurkite funkciją, kuri per argumentus gautų skaičių. Ji turėtų patikrinti
# ar šis skaičius yra pirminis (grąžina True jei pirminis, ir False jei ne
# pirminis). Už funkcijos ribų sukite ciklą nuo 2 iki 15, kiekvienoje ciklo
# iteracijoje išveskite tikrinamą skaičių ir šalia jo iškviestos funkcijos
# atsakymą (pvz 10 false, 11 true, ...).
# 22.Susikurkite bent 3 matematines funkcijas, priimančias reikiamus
# argumentus (pvz suma iš dviejų skaičių, suma iš trijų skaičių, skirtumas,
# sandauga, dalyba) ir grąžinančias atitinkamus atsakymus. Taip pat,
# susikurkite funkciją, kurioje būtų sugeneruojamas reikiamas kiekis
# atsitiktinių skaičių ir išvedami visų skaičiavimų atsakymai su veiksmais
# (iškviečiant atitinkamas kitas funkcijas ir perduodant reikiamus
# kintamuosius) (pagal 23 pavyzdį). Iškvieskite šią pagrindinę funkciją bent
# kartą.
# 23.Susikurkite funkciją kuri priimtų skaičių masyvą per argumentus. Ši
# funkcija turėtų rasti duotųjų skaičių sumą ir grąžinti gautą atsakymą. Už
# funkcijos ribų susikurkite du skaičių masyvus ir užpildykite juos
# duomenimis. Iškvieskite turimą funkciją du kartus, jai abu kartus
# perduodant skirtingą masyvą. Gautus atsakymus išveskite. Taip pat,
# raskite kuri suma gavosi didesnė ir išveskite atsakymą.
# 24.Susikurkite funkciją kuri per argumentus priimtų žodžių masyvą. Ji turėtų
# rasti ir grąžinti ilgiausią žodį masyve. Už funkcijos ribų susikurkite žodžių
# masyvą. Iškvieskite funkciją perduodant jai žodžių masyvą. Gautą
# atsakymą išveskite, taip pat, nurodykite šio žodžio ilgį.
# 25.Susikurkite funkciją kuri per argumentus priimtų pažymių masyvą. Ji
# turėtų patikrinti ar visi pažymiai teigiami: jei visi teigiami turėtų grąžintų
# True kaip atsakymą, o jei yra bent vienas neigiamas - False. Susikurkite du
# pažymių masyvus. Iškvieskite šią funkciją du kartus, abu kartus
# perduodant skirtingus masyvus. Gautus atsakymus paverskite į tekstą
# (jeigu gavote True - išveskite tekstą 'visi studento pažymiai teigiami', jei
# False - 'studentas turi bent vieną neigiamą pažymį'). Šiam iškonvertavimui
# iš True/False į tekstą galite pamėginti pasikurti atskirą funkciją, jai
# perduoti kitos funkcijos atsakymą.
# 26.Pabandykite parašyti bent dvi pasirinktas funkcijas, kuriose būtų
# naudojami default parametrai. Iškvieskite šias funkcijas įvairiais būdais
# (perduodant visus argumentus, bei neperduodant tų kuriuos galima
# praleisti (turinčius default reikšmes)).