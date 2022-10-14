# Imports
from getpass import getpass
from time import sleep
from datetime import date
import csv
import sys


# Varbiabeln
space = " "
excl = "!"
ques = "?"


# Farben
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def main():
    menu()

# Menü
def menu():
    print("************Willkommen**************")
    print()

    # Auswahl
    choice = input("""
    A: Altersantwort
    B: Geburtsdatum Rechner
    C: Zahlenausgabe
    D: Countdown
    E: Zahlenraten
    F: ...
    G: ...
    H: ...
    I: ...
    J: ...
    K: ...
    L: ...
    M: ...
    N: ...
    O: ...
    P: ...
    Q: ...
    R: ...
    S: ...
    T: ...
    U: ...
    V: ...
    W: ...
    X: ...
    Y: ...
    Z: ...

    Bitte gebe hier deine Antwort ein: """)
    print ("""
    """)

    # A Ausgewählt
    if choice == "a" or choice == "A":
        age = "False"
        requestagehide = "False"
        requestsexhide = "False"
        sex = "False"
        print (f"{bcolors.BOLD}{bcolors.FAIL}System: {bcolors.ENDC}Du hast die für", "A: Altersantwort", "enschieden!")
        sleep(2)
        ageanswer(requestagehide, age, requestsexhide, sex)

    # B Ausgewählt    
    elif choice == "b" or choice == "B":
        print (f"{bcolors.BOLD}{bcolors.FAIL}System: {bcolors.ENDC}Du hast dich für", "B: Geburtsdatum Rechner", "entschieden!")
        sleep(2)
        datecalcmenu()
    
    # C Ausgewählt
    elif choice == "c" or choice == "C":
        print (f"{bcolors.BOLD}{bcolors.FAIL}System: {bcolors.ENDC}Du hast dich für", "C: Zahlenausgabe", "entschieden!")
        sleep(2)
        numberpress()
    
    # D Ausgewählt
    elif choice == "d" or choice == "D":
        print (f"{bcolors.BOLD}{bcolors.FAIL}System: {bcolors.ENDC}Du hast dich für", "D: Countdown", "entschieden!")
        sleep(2)
        countdown()

    # E Ausgewählt
    elif choice == "e" or choice == "E":
        print (f"{bcolors.BOLD}{bcolors.FAIL}System: {bcolors.ENDC}Du hast dich für", "E: Zahlenraten", "entschieden!")
        sleep(2)
        numberraten()

    # F Ausgewählt
    elif choice == "f" or choice == "F":
        sleep
    
    # G Ausgewählt
    elif choice == "g" or choice == "G":
        sleep

    # H Ausgewählt
    elif choice == "h" or choice == "H":
        sleep

    # I Ausgewählt
    elif choice == "i" or choice == "I":
        sleep

    # J Ausgewählt
    elif choice == "j" or choice == "J":
        sleep

    # K Ausgewählt
    elif choice == "k" or choice == "K":
        sleep

    # L Ausgewählt
    elif choice == "l" or choice == "L":
        sleep
    
    # M Ausgewählt
    elif choice == "m" or choice == "M":
        sleep

    # N Ausgewählt
    elif choice == "n" or choice == "N":
        sleep

    # O Ausgewählt
    elif choice == "o" or choice == "O":
        sleep

    # P Ausgewählt
    elif choice == "p" or choice == "P":
        sleep

    # Q Ausgewählt
    elif choice == "q" or choice == "Q":
        sleep

    # R Ausgewählt
    elif choice == "r" or choice == "R":
        sleep
    
    # S Ausgewählt
    elif choice == "s" or choice == "S":
        sleep

    # T Ausgewählt
    elif choice == "t" or choice == "T":
        sleep

    # U Ausgewählt
    elif choice == "u" or choice == "U":
        sleep

    # V Ausgewählt
    elif choice == "v" or choice == "V":
        sleep

    # W Ausgewählt
    elif choice == "w" or choice == "W":
        sleep

    # X Ausgewählt
    elif choice == "x" or choice == "X":
        sleep

    # Y Ausgewählt
    elif choice == "y" or choice == "Y":
        sleep

    # Z Ausgewählt
    elif choice == "z" or choice == "Z":
        sleep
    
    # Fehlermeldung
    else:
        print(f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Bitte antworte nur mit den Angegebenen Buchstaben!")
        sleep(1)
        menu()

#### Ageanswer ####
def ageanswer(requestagehide, age, requestsexhide, sex):
    # Öffnungstext
    print()
    print(f"{bcolors.BOLD}{bcolors.FAIL}Altersantwort: {bcolors.ENDC}{bcolors.BOLD}Du hast Altersantwort geöffnet!{bcolors.ENDC}")
    print()
    sleep(1)
    # Weiterleitung
    ageanswerquehide(requestagehide, age, requestsexhide, sex)

def ageanswerquehide(requestagehide, age, requestsexhide, sex):
    # Frage
    requestagehide = (input(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Möchtest du dein Alter anzeigen lassen? "))
    # Antworten
    if requestagehide == "quit":
        quit()
    # Ja
    elif requestagehide == "ja" or requestagehide == "Ja":
        ageanswerqueagevis(requestagehide, age, requestsexhide, sex)
    # Nein
    elif requestagehide == "nein" or requestagehide == "Nein":
        ageanswerqueageinv(requestagehide, age, requestsexhide, sex)
    # Fehlermeldung
    else:
        print (f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Bitte nur mit Ja oder Nein antworten!")
        sleep(1)
        ageanswerquehide(requestagehide, age, requestsexhide, sex)

def ageanswerqueagevis(requestagehide, age, requestsexhide, sex):
    # Ausgabe
    print (f"{bcolors.BOLD}{bcolors.FAIL}Settings: {bcolors.ENDC}Dein Alter wird angezeigt.")
    sleep(1.5)
    # Wenn noch nicht angegeben
    if age == "False":
        try:
            # Frage
            age = int(input(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC} Wie alt bist du? "))
        except ValueError:
            # Fehlermeldung
            print(f"{bcolors.BOLD}{bcolors.FAIL}System: {bcolors.ENDC}Bitte nur mit einer Zahl antworten!")
            sleep (1)
            ageanswerqueagevis(requestagehide, age, requestsexhide, sex)
        else:
            # Weiterleitung
            ageanswerquesex(requestagehide, age, requestsexhide, sex)
    else:
        # Weiterleitung wenn Alter schon angegeben
        ageanswerquesex(requestagehide, age, requestsexhide, sex)

def ageanswerqueageinv(requestagehide, age, requestsexhide, sex):
    # Ausgabe
    print (f"{bcolors.BOLD}{bcolors.FAIL}System: {bcolors.ENDC}Dein Alter wird nicht anzeigt.")
    sleep(1.5)
    # Wenn Alter noch nicht angegeben
    if age == "False":
        try:
            # Frage
            age = int(getpass(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC} Wie alt bist du? "))
        except ValueError:
            # Fehlermeldung
            print(f"{bcolors.BOLD}{bcolors.FAIL}System: {bcolors.ENDC}Bitte nur mit einer Zahl antworten!")
            sleep (1)
            ageanswerqueagevis(requestagehide, age, requestsexhide, sex)
        else:
            # Weiterleitung
            ageanswerquesex(requestagehide, age, requestsexhide, sex)
    else:
        # Weiterleitung wenn Alter schon angegeben
        ageanswerquesex(requestagehide, age, requestsexhide, sex)

def ageanswerquesex(requestagehide, age, requestsexhide, sex):
    # Wenn Geschlecht noch nicht angegeben und über 115
    if requestsexhide == "False" and age >= 116:
        requestsexhide = (input(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Möchtest du dein Geschlecht anzeigen lassen? "))
        # Quit
        if requestsexhide == "quit":
            quit()
        # Ja
        elif requestsexhide == "ja" or requestsexhide == "Ja":
            ageanswerquesexvis(requestagehide, age, requestsexhide, sex)
        # Nein
        elif requestsexhide == "nein" or requestsexhide == "Nein-":
            ageanswerquesexinv(requestagehide, age, requestsexhide, sex)
        else:
            # Fehlermeldung
            print (f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Bitte nur mit Ja oder Nein antworten!")
            sleep(1)
            ageanswerquesex(requestagehide, age, requestsexhide, sex)
    else:
        # Weiterleitung wenn Geschlecht schon angegeben oder unter 116
        ageanswercheck(requestagehide, age, requestsexhide, sex)

def ageanswerquesexvis(requestagehide, age, requestsexhide, sex):
    # Ausgabe
    print (f"{bcolors.BOLD}{bcolors.FAIL}System: {bcolors.ENDC}Dein Geschlecht wird anzeigt.")
    sleep(1.5)
    # Wenn Geschlecht noch nicht angegeben
    if sex == "False":
        # Frage
        sex = (input(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Was ist dein Geschlecht? "))
        # Quit
        if sex == "quit":
            quit()
        # Männlich
        elif sex == "m" or sex == "M":
            ageanswercheck(requestagehide, age, requestsexhide, sex)
        # Weiblich
        elif sex == "w" or sex == "W":
            ageanswercheck(requestagehide, age, requestsexhide, sex)
        else:
            # Fehlermeldung
            print (f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Bitte nur mit M(Männlich) oder W(Weiblich) antworten!")
            sleep(1)
            ageanswerquesexvis(requestagehide, age, requestsexhide, sex)

def ageanswerquesexinv(requestagehide, age, requestsexhide, sex):
    # Ausgabe
    print (f"{bcolors.BOLD}{bcolors.FAIL}System: {bcolors.ENDC}Dein Geschlecht wird nicht anzeigt.")
    sleep(1.5)
    # Wenn noch nicht angegeben
    if sex == "False":
        sex = (getpass(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Was ist dein Geschlecht? "))
        # Quit
        if sex == "quit":
            quit()
        # Männlich
        elif sex == "m" or sex == "M":
            ageanswercheck(requestagehide, age, requestsexhide, sex)
        # Weiblich
        elif sex == "w" or sex == "W":
            ageanswercheck(requestagehide, age, requestsexhide, sex)
        else:
            # Fehlermeldung
            print (f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Bitte nur mit M(Männlich) oder W(Weiblich) antworten!")
            sleep(1)
            ageanswerquesexinv(requestagehide, age, requestsexhide, sex)

def ageanswercheck(requestagehide, age, requestsexhide, sex):
    # Alterverstecken Check
    if requestagehide == "False":
        print(f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Es ist ein Fehler aufgetreten, bitte versuche es erneut!")
        ageanswerquehide(requestagehide, age, requestsexhide, sex)
    # Alter Check
    if age == "False":
        print(f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Es ist ein Fehler aufgetreten, bitte versuche es erneut!")
        ageanswerquehide(requestagehide, age, requestsexhide, sex)
    # Wenn Alter anzeigen
    if requestagehide == "ja" or requestagehide == "Ja":
        ageansweranswervis(requestagehide, age, requestsexhide, sex)
    # Wenn Alter nicht anzeigen
    elif requestagehide == "nein" or requestagehide == "Nein":
        ageansweranswerinv(requestagehide, age, requestsexhide, sex)

def ageansweranswervis(requestagehide, age, requestsexhide, sex):

    # Alters Antworten
    if age <= -1:
        print(f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Du bist noch nicht Geboren, mit deinen", str(age), "Jahren" + excl)
    elif age <= 3 and age >= 0:
        print(f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Du bist ein Baby mit deinen", str(age), "Jahren" + excl)
    elif age <= 12 and age >= 4:
        print(f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Du bist Ein Kind mit deinen", str(age), "Jahren" + excl)
    elif age <= 17 and age >= 13:
        print (f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Du bist Jugendlich mit deinen", str(age), "Jahren" + excl)
    elif (age >= 18 and age <= 116) or (age >= 117 and sex != "m" and age <= 122) or (age >= 117 and sex != "M" and age <= 122):
        print (f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Du bist Erwachsen mit deinen", str(age), "Jahren" + excl)
    elif (age >= 123 and sex == "w" and requestsexhide == "ja") or (age >= 123 and sex == "W" and requestsexhide == "Ja") or (age >= 123 and sex == "w" and requestsexhide == "Ja") or (age >= 123 and sex == "W" and requestsexhide == "ja"):
        print (f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Du bist", age, "Jahre alt und somit hast du den Rekord zur ältesten Frau geknackt. Herzlichen Glüchwunsch!")
    elif (age >= 117 and sex == "m" and requestsexhide == "ja") or (age >= 117 and sex == "M" and requestsexhide == "Ja") or (age >= 117 and sex == "m" and requestsexhide == "Ja") or (age >= 117 and sex == "M" and requestsexhide == "ja"):
        print (f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Du bist", age, "Jahre alt und somit hast du den Rekord zum ältesten Mann geknackt. Herzlichen Glüchwunsch!")
    elif age >=123 and requestsexhide == "nein" or requestsexhide == "Nein":
        print (f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Du bist ziemlich alt und somit hast du den Rekord zum ältesten Mensch geknackt. Herzlichen Glüchwunsch!")
    else:
        # Fehlermeldung
        print(f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Es ist ein Fehler aufgetreten, bitte versuche es erneut!")
        sleep(1)
        ageanswerquehide(requestagehide, age, requestsexhide, sex)
    
def ageansweranswerinv(requestagehide, age, requestsexhide, sex):

    # Altersantworten
    if age <= -1:
        print(f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Du bist noch nicht Geboren!")
    elif age <= 3 and age >= 0:
        print(f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Du bist ein Baby!")
    elif age <= 12 and age >= 4:
        print(f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Du bist Ein Kind!")
    elif age <= 17 and age >= 13:
        print (f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Du bist Jugendlich!")
    elif (age >= 18 and age <= 116) or (age >= 117 and sex == "w" and age <= 122) or (age >= 117 and sex == "W" and age <= 122):
        print (f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Du bist Erwachsen!")
    elif (age >= 123 and sex == "w" and requestsexhide == "ja") or (age >= 123 and sex == "W" and requestsexhide == "Ja") or (age >= 123 and sex == "w" and requestsexhide == "Ja") or (age >= 123 and sex == "W" and requestsexhide == "ja"):
        print (f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Du bist ziemlich alt und somit hast du den Rekord zur ältesten Frau geknackt. Herzlichen Glüchwunsch!")
    elif (age >= 117 and sex == "m" and requestsexhide == "ja") or (age >= 117 and sex == "M" and requestsexhide == "Ja") or (age >= 117 and sex == "m" and requestsexhide == "Ja") or (age >= 117 and sex == "M" and requestsexhide == "ja"):
        print (f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Du bist ziemlich alt und somit hast du den Rekord zum ältesten Mann geknackt. Herzlichen Glüchwunsch!")
    elif age >=123 and requestsexhide == "nein" or requestsexhide == "Nein":
        print (f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Du bist ziemlich alt und somit hast du den Rekord zum ältesten Mensch geknackt. Herzlichen Glüchwunsch!")


    else:
        # Fehlermeldung
        print(f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Es ist ein Fehler aufgetreten, bitte versuche es erneut!")
        sleep(1)
        ageanswerquehide(requestagehide, age, requestsexhide, sex)


#### Date Calc ####
def datecalcmenu():
        # Öffnungstext
        print()
        print(f"{bcolors.BOLD}{bcolors.FAIL}Geburtsdatum Rechner: {bcolors.ENDC}{bcolors.BOLD}Du hast Geburtsdatum Rechner geöffnet!{bcolors.ENDC}")
        print()
        sleep(1)
        datecalcbirth()

def datecalcbirth():
    # Fragen
    birthYear = int(input(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Was ist dein Geburtsjahr? "))  
    birthMonth = int(input(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Was ist dein Geburtsmonat? "))  
    birthDay = int(input(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Was ist dein Geburtstag? "))
    try:
        # Fragen zusammenfügen
        dateOfBirth = date(birthYear, birthMonth, birthDay)  
    except ValueError:
        # Fehlermeldung
        print(f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Bitte Antworte mit einem echten Geburtsdatum!")
        sleep(1)
        datecalcbirth()
    else:        
        datecalc(dateOfBirth)    

def datecalc(birthday):
    # Akuteller Tag
    today = date.today()
    # Älter als Heute check
    day_check = ((today.month, today.day) < (birthday.month, birthday.day))
    # Jahr Berechnung
    year_diff  = today.year - birthday.year
    # Jahr vergleich
    age_in_years = year_diff - day_check
    # Monats Berechnung
    remaining_months = abs(today.month - birthday.month)
    # Tage Berechnung
    remaining_days = abs(today.day - birthday.day)
    print(f"{bcolors.BOLD}{bcolors.FAIL}Alter: {bcolors.ENDC}", age_in_years, "Jahre", remaining_months, "Monate und", remaining_days, "Tage") 
    sleep(1)
    ageansque(age_in_years)

#### Date Calc to Ageanswer ####
def ageansque(age_in_years):
    # Fortfahr Frage
    ageansque = input(f"{bcolors.BOLD}{bcolors.FAIL}System: {bcolors.ENDC} Möchtest du mit diesem Alter zur Altersantwort fortfahren? ")
    # Antwort Check
    if ageansque == "ja" or ageansque == "Ja":
        ageanswer(age_in_years)
    elif ageansque == "nein" or ageansque == "Nein":
        quit()
    else:
        #Weiterleitung
        ageansque()

#### Numberpress ####
def numberpress():
    # Öffnungstext
    print()
    print(f"{bcolors.BOLD}{bcolors.FAIL}Zahlenausgabe: {bcolors.ENDC}{bcolors.BOLD}Du hast Zahlenausgabe geöffnet!{bcolors.ENDC}")
    print()
    #Menü
    print("************Was möchtest du tun?**************")
    choice = input("""
    A: Geschriebene Zahl wiedergeben
    B: Zahlenbereich Angabe

    Bitte gebe hier deine Antwort ein: """)
    print ("""
    """)
    # Antwortcheck (Weiterleitung)
    if choice == "a" or choice == "A":
        renumber()
    elif choice == "b" or choice == "B":
        numberarea()
    else:
        # Fehlermeldung
        print(f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Bitte Antworte nur mit den angegebenen Buchstaben!")
        sleep(1)
        numberpress()
    
## Renumber ##    
def renumber():
    # Öffnungstextr
    print()
    print(f"{bcolors.BOLD}{bcolors.FAIL}Zahlenausgabe: {bcolors.ENDC}{bcolors.BOLD}Du hast Zahlenausgabe geöffnet!{bcolors.ENDC}")
    print()
    # Inv Frage
    print(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Möchtest du das deine Zahl beim Angeben angezeigt wird?")
    vischoice = input("Bitte antworte hier! ")
    # Antwortscheck
    if vischoice == "ja" or vischoice == "Ja":
        renumberprocvis()
    elif vischoice == "nein" or vischoice == "Nein":
        renumberprocinv()
    else:
        # Fehlermeldung
        print(f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Bitte antworte nur mit Ja oder Nein!")
        sleep(2)
        renumber()

def renumberprocvis():
    try:
        # Frage
        number = int(input(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Welche Zahl soll ausgegeben werden? "))
    except ValueError:
        # Fehlermeldung
        print(f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Bitte anworte nur mit einer Zahl!")
        sleep(2)
        renumberprocvis()
    else:
        # Ausgabe
        print(f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}", number)

def renumberprocinv():
    try:
        # Frage
        number = int(getpass(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Welche Zahl soll ausgegeben werden? "))
    except ValueError:
        # Fehlermeldung
        print(f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Bitte anworte nur mit einer Zahl!")
        sleep(2)
        renumberprocinv()
    else:
        # Ausgabe
        print(f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}", number)

## Numberarea ##    
def numberarea():
    # Öffnungstext
    print()
    print(f"{bcolors.BOLD}{bcolors.FAIL}Zahlenbereich: {bcolors.ENDC}{bcolors.BOLD}Du hast Zahlenbereich geöffnet!{bcolors.ENDC}")
    print()
    # Frage
    print(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Möchtest du das deine Zahl beim Angeben angezeigt wird?")
    vischoice = input("Bitte antworte hier! ")
    # Antwortscheck
    if vischoice == "ja" or vischoice == "Ja":
        numberareaprocvis()
    elif vischoice == "nein" or vischoice == "Nein":
        numberareaprocinv()
    else:
        # Fehlermeldung
        print(f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Bitte antworte nur mit Ja oder Nein!")
        sleep(2)
        numberarea()

def numberareaprocvis():
    try:
        # Frage
        number = int(input(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Von welcher Zahl soll der Bereich bestimmt werden? "))
    except ValueError:
        # Fehlermeldung
        print(f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Bitte anworte nur mit einer Zahl!")
        sleep(2)
        numberareaprocvis()
    else:
        # Ausgabe (Antwortscheck)
        if number < 10:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Deine Zahl ist kleiner als 10!")
        if number > 10 and number < 20:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Deine Zahl ist zwischen 10 und 20!")
        elif number > 20:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Deine Zahl ist größer als 20!")

def numberareaprocinv():
    try:
        # Frage
        number = int(getpass(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Von welcher Zahl soll der Bereich bestimmt werden? "))
    except ValueError:
        # Fehlermeldung
        print(f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Bitte anworte nur mit einer Zahl!")
        sleep(2)
        numberareaprocinv()
    else:
        # Ausgabe (Antwortscheck)
        if number < 10:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Deine Zahl ist kleiner als 10!")
        if number > 10 and number < 20:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Deine Zahl ist zwischen 10 und 20!")
        elif number > 20:
            print(f"{bcolors.BOLD}{bcolors.FAIL}Answer: {bcolors.ENDC}Deine Zahl ist größer als 20!")

#### COUNTDOWN #####

def countdown():
    # Öffnungscheck
    print()
    print(f"{bcolors.BOLD}{bcolors.FAIL}Countdown: {bcolors.ENDC}{bcolors.BOLD}Du hast Countdown geöffnet!{bcolors.ENDC}")
    print()
    # Frage
    sleep(1)
    print(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Möchtest du das deine Zahl beim Angeben angezeigt wird?")
    vischoice = input("Bitte antworte hier! ")
    # Antwortscheck (Weiterleitung)
    if vischoice == "ja" or vischoice == "Ja":
        countdownprocvis()
    elif vischoice == "nein" or vischoice == "Nein":
        countdownprocinv()
    else:
        # Fehlermeldung
        print(f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Bitte antworte nur mit Ja oder Nein!")
        sleep(2)
        countdown()

def countdownprocvis():
    try:
        # Fragen
        sleep(1)
        number = int(input(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Mit welcher Zahl soll der Countdown starten? "))
        countend = int(input(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Wann soll der Countdown enden? "))
        sleeptime = float(input(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Wie viele Sekunden sollen zwischen den Zahlen im Countdown sein? "))
    except ValueError:
        # Fehlermeldung
        print(f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Bitte anworte nur mit Zahlen!")
        sleep(2)
        countdownprocvis()
    while number == countend:
        # Countdown
        print (number)
        number = number - 1
        sleep(sleeptime)

def countdownprocinv():
    try:
        # Fragen
        number = int(getpass(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Mit welcher Zahl soll der Countdown starten? "))
        countend = int(getpass(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Wann soll der Countdown enden? "))
        sleeptime = float(getpass(f"{bcolors.BOLD}{bcolors.FAIL}Question: {bcolors.ENDC}Wie viele Sekunden sollen zwischen den Zahlen im Countdown sein? "))
    except ValueError:
        # Fehlermeldung
        print(f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Bitte anworte nur mit Zahlen!")
        sleep(2)
        countdownprocinv()
    while number == countend:
        # Countdown
        print (number)
        number = number - 1
        sleep(sleeptime)

### Numberraten ####
def numberraten():
    solved = False
    # Öffnungstext
    print()
    print(f"{bcolors.BOLD}{bcolors.FAIL}Zahlenraten:{bcolors.ENDC}", f"{bcolors.BOLD}Du hast Zahlenraten gestartet!{bcolors.ENDC}")
    print()
    sleep(1)
    numberratenque()
        
def numberratenque():
    try:
        # 1. Frage
        searched = int(getpass(f"{bcolors.BOLD}{bcolors.FAIL}Spieler 1: {bcolors.ENDC}Wie soll die zu erratene Zahl lauten? "))
    except ValueError:
        # Fehlermeldung
        print(f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Bitte anworte nur mit Zahlen!")
        sleep(2)
        numberratenque()
    else:
        sleep(1)
        numberratenans(searched)

def numberratenans(searched):
    solved = False
    tries = 0
    while solved == False:
        try:
            # 2. Frage (Loop)
            rate = int(input(f"{bcolors.BOLD}{bcolors.WARNING}Spieler 2: {bcolors.ENDC}Wie möchtest du raten? "))
        except ValueError:
            # Fehlermeldung
            print(f"{bcolors.BOLD}{bcolors.FAIL}Error: {bcolors.ENDC}Bitte anworte nur mit Zahlen!")
            sleep(2)
            numberratenans(searched)
        else:
            # Antworten
            if rate > searched:
                tries = tries + 1
                print(f"{bcolors.BOLD}{bcolors.FAIL}System: {bcolors.ENDC}Du hast zu hoch geraten!")
            if rate < searched:
                tries = tries + 1
                print(f"{bcolors.BOLD}{bcolors.FAIL}System: {bcolors.ENDC}Du hast zu niedrig geraten!")
            if rate == searched:
                # Ende 
                tries = tries + 1
                print (f"{bcolors.BOLD}{bcolors.FAIL}System: {bcolors.ENDC}Du hast es geschafft, das Spiel ist beendet. Die gesuchte Zahl war:", searched)
                # Bei mehr als 1 Versuch
                if tries > 1:
                    print (f"{bcolors.BOLD}{bcolors.FAIL}System: {bcolors.ENDC}{bcolors.BOLD}{bcolors.WARNING}Spieler 2 {bcolors.ENDC}hat", tries, "Versuche gebraucht um die gesuchte Zahl zu finden!")
                # Bei einem Versuch
                elif tries == 1:
                    print (f"{bcolors.BOLD}{bcolors.FAIL}System: {bcolors.ENDC}{bcolors.BOLD}{bcolors.WARNING}Spieler 2 {bcolors.ENDC}hat", tries, "Versuch gebraucht um die gesuchte Zahl zu finden!")
                solved = True


#Code
main()