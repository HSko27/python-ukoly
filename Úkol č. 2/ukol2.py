#zadaný array studentů a jejich zapsaných předmětů 

studenti = { 
 "Ivana" : [ "Python" , "Linární algebra" , "Statistika" ], 
 "Irena" : [ "Python" , "Linární algebra" ], 
 "Igor" : [ "Python" , "Statistika" , "Databáze" , "Soft Skills" ], 
 "Ignác" : [ "Linární algebra" , "Statistika" , "Databáze" ], 
 "Iveta" : [ "Soft Skills" , "Linární algebra" , "Python" ] 
 } 

input ( " \n Enter" ) 

 #1. Část - Přidání Ivetě předmět Statistika 

studenti [ "Iveta" ]. append ( "Statistika" ) 
print ( studenti ) 
input ( " \n Enter" ) 

 #2. Část - Náhrada předmětu Linární algebra za Soft Skills 

studenti [ "Ivana" ][ 1 ] = "Soft Skills" 
print ( studenti ) 
input ( " \n Enter" ) 

 #3. Část - seznam všech předmětů neopakujících se předmětů 

unikatni_predmety = [] 

for predmety in studenti . values (): 
 for predmet in predmety : 
    if predmet not in unikatni_predmety : 
        unikatni_predmety . append ( predmet ) 
 
print ( unikatni_predmety ) 
input ( " \n Enter" ) 

 #4. Část - Kolik předmětů má Igor 

print ( "Igor má: " , len ( set ( studenti [ "Igor" ])), "předměty." ) 
input ( " \n Enter" ) 

 #5. Část - Kolik studentů má zapsaný Předmět Databáze 

count = sum ( "Databáze" in predmety for predmety in studenti . values ()) 

print ( "Studenti kteří mají předmět Databáze: " , { count } )