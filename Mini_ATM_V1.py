users = [
    ["melisa", "1234", 1500],
    ["lucky", "abcd", 800],
    ["alex", "passwort", 2500]
]

print("1. Login")

eingeloggter_user = None            
login = False           

# 1. Login                        #True → ein Benutzer ist eingeloggt    False → niemand ist eingeloggt
while login == False:
    username = input("Username: ")
    password = input("Password: ")

    for user in users:
        print(user[0]) #kannst beide entfernen. for user in users bedeutet:
        print(user[1])
        if username == user[0] and password == user[1]:
            print("Anmeldug erfolgreich")
            eingeloggter_user = user
            login = True
            break
    else:
        print("Username oder Password falsch")

print("1. Kontostand anzeigen\n2. Geldeinzahlen\n3. Geld abheben\n4. Password ändern\n5. Logout")
auswahl = input("> ")
print(auswahl) #Kannst du entfernen

# 2. Kontostand
if auswahl == "1":
    print(eingeloggter_user[2])

# 3. Geld einzahlen
elif auswahl == "2":
    print("Wie viel möchten Sie einzahlen? ")
    betrag = int(input("> "))
    print("Hinzugefügter Betrag: ", betrag)

    eingeloggter_user[2] = eingeloggter_user[2] + betrag
    print("Kontostand: ", eingeloggter_user[2])

# 4. Geld abheben
elif auswahl == "3":
    print("Wie viel möchten Sie abheben? ")
    betrag = int(input("> "))

    if betrag > eingeloggter_user[2]:
        print("Nicht genügend Guthaben")
    else:
        eingeloggter_user[2] = eingeloggter_user[2] - betrag
        print("Kontostand: ", eingeloggter_user[2])
        print("Auszahlung erfolgreich")

# 5. Password ändern
elif auswahl == "4":
    print("Ändern Sie Ihr Password: ")
    neues_password = input("> ")
    eingeloggter_user[1] = neues_password
    print("Passwort erfolgreich geändert")

# 6. Logout
elif auswahl == "5": 
   print("Auf Wiedersehen!")
   login = False

else:
    print("Ungültige Auswahl.")


    
    
    
    
            
                       
# users ist eine verschachtelte Liste (eine Liste mit mehreren Listen)
# Jede innere Liste enthält: [Username, Passwort, Kontostand]

# users[0] gibt den ersten Benutzer zurück:
# ["melisa", "1234", 1500]

# users[0][0] bedeutet:
# Gehe zur ersten Benutzerliste und nehme das erste Element → "melisa"

# users[0][1] bedeutet:
# Gehe zur ersten Benutzerliste und nehme das zweite Element → "1234"

# In einer for-Schleife:
# for user in users:
#     user nimmt nacheinander jede innere Liste an

# Erster Durchlauf:
# user = ["melisa", "1234", 1500]

# Zweiter Durchlauf:
# user = ["lucky", "abcd", 800]

# Dritter Durchlauf:
# user = ["alex", "passwort", 2500]

# Nach der Schleife bleibt user beim letzten Wert:
# user = ["alex", "passwort", 2500]
#user[0]       → Username komplett
#user[0][0]    → erster Buchstabe vom Username
#user[0][1]    → zweiter Buchstabe vom Username
