#původní seznam

zavod = { 
 "Anna" : ( 21 , 52.4 ), 
 "Petr" : ( 25 , 48.7 ), 
 "Jana" : ( 19 , 55.2 ), 
 "Martin" : ( 31 , 47.9 ), 
 "Eva" : ( 27 , 51.3 ), 
 "Dita" : ( 35 , 49.4 ), 
 "Eduard" : ( 22 , 51.0 ), 
 "Vít" : ( 29 , 52.8 ) 
 }

print(zavod)


#1. část - celkový počet závodníků

input("Enter: ")
print("Celkový počet závodníků:", len(zavod))

#2. část - údaje o Petrovi

input("Enter: ")
print("Petr: ")
print("Věk: ", zavod["Petr"][0])
print("Čas: ", zavod["Petr"][1], "Min.")

#3. část - Věk Jany

input("Enter: ")
print("Věk Jany: ", zavod["Jana"][0])

#4. část - Nejlepší výsledek

input("Enter: ")
best = min(zavod, key=lambda x: zavod[x][1])
print(best)

#5. část - seznam jmen závodníků

input("Enter: ")
zavodnici = list(zavod.keys())
print("Seznam jmen závodníků: ", zavodnici)

#6. část - přidání závodníka do seznamu

input("Enter: ")
zavodnici.append("Jan")
print( "Přidaný účastník - Jan: ", zavodnici)

#bonus - přidání nového závodníka do původního seznamu i s daty
input("Enter: ")
zavod.update({"Jan": (28, 50.5)})
print(zavod)



