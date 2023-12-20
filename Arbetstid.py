#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Räknar ut lönen med hjälp av arbetstiden. 

Genom att skriva in sin individuella lön, följt av dagar arbetade under en månad kan användaren räkna ut sin lön.
Lönen räknas ut genom att månadslönen omvandlas till timlön, för att sedan multiplicera med arbetstid, obekväm arbetstid, 
jour, helgdagar, röda dagar, beredskap, uppkommen jour, FM-dygn, etc.
"""
# 1. Fortsätt lägga till andra saker som beredskap
# 2. Lägg till en if-statement där man skriva om man har varit sjuk, jobbat röda dagar, jobbat fredagar, helger etc.


stop = False
while not stop:
    # Menyval
    print("Vänligen följ menyvalen nedan för att räkna ut din lön.") 
    print("1) Räkna ut lön.")
    print("q) Avsluta programmet.")

    choice = input("--> ")

    # Avslutar programmet 
    if choice == "q":
        print("Programmet stänger ner!")
        stop = True

    # Menyval 1 där användaren kan räkna ut sin lön för en månad.
    elif choice == "1":
        
        try:
            # Räknar ut lönen för dagtid.
            monthly_pay = int(input("Skriv in vad din månadslön är:\n"))
            pay_hour = monthly_pay / 140 # ändra heltalet för att ändra från BY91 arbetstid (140h) eller till normal arbetstid (160h)

            blapass_days = int(input("Skriv in hur många dagar du arbetat blåpass:\n"))
            faltpass_days = int(input("Skriv in hur många dagar du arbetat på fält:\n"))
            # Hur funkar arbetsstiden när vi har lunchrast? Hur mycket faktiskt arbetstid får vi??
            blapass_hours = blapass_days * 8
            falt_hours = faltpass_days * 9
            dagtid_pay = (blapass_hours + falt_hours) * pay_hour
            print(f"Du har tjänat {round(dagtid_pay)}kr denna månaden genom dagtid.")
            # Räknar ut lönen för dygn.
            dygn_days = int(input("Skriv in hur många dygn du arbetat:\n"))
            normal_pay = (11.5 * pay_hour) * dygn_days
            enkel_ob_pay = (4.5 * 20) * dygn_days # Enkel Ob_arbetstid i timmar * kronor.
            kval_ob_pay = (3 * 60) * dygn_days # Kval Ob_arbetstid i timmar * kronor.
            jour_pay = (13 * 60) * dygn_days # Jour i timmar * kronor

            dygn_pay = (normal_pay + enkel_ob_pay + kval_ob_pay + jour_pay)
            print(f"Du har tjänat {round(dygn_pay)}kr denna månaden genom dygn.")
            print(f"Du har totalt tjänat {round(dygn_pay + dagtid_pay)}kr denna månaden.")
            



        except ValueError:
            print("Skriv in antalet dagar du har arbetat igen. Var nogrann med att bara skriva med siffror.")


    else:
        print("That is not a valid choice. You can only choose from the menu.")

    if not stop:
        input("\nPress enter to continue...")