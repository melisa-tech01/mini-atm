import getpass 

users = [
    ["melisa", "1234", 1500],
    ["lucky", "abcd", 800],
    ["alex", "passwort", 2500]
]

print("1. Login")

eingeloggter_user = None            
login = False     

# 1. Login                       
while not login:
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    for user in users:
        if username == user[0] and password == user[1]:
            print("Anmeldug erfolgreich")
            eingeloggter_user = user
            login = True
            break
    else:
        print("Username oder Password falsch")

while login:
    print("1. Kontostand anzeigen\n2. Geldeinzahlen\n3. Geld abheben\n4. Password ändern\n5. Logout")
    auswahl = input("> ")

    # 2. Kontostand
    if auswahl == "1":
        print(eingeloggter_user[2])

    # 3. Geld einzahlen
    elif auswahl == "2":
        print("Wie viel möchten Sie einzahlen? ")

        betrag = None

        while betrag is None:
            try:
                betrag = int(input("> "))
            except ValueError:
                print("Bitte geben Sie eine gültige Zahl ein.")

        if betrag > 0:
            print("Hinzugefügter Betrag: ", betrag)
            eingeloggter_user[2] = eingeloggter_user[2] + betrag
            print("Kontostand: ", eingeloggter_user[2])

        else:
            print("Ungültiger Betrag. Der Betrag muss größer als 0 sein.")

    # 4. Geld abheben
    elif auswahl == "3":
        print("Wie viel möchten Sie abheben? ")

        betrag = None

        while betrag is None:
            try:
                betrag = int(input("> "))
            except ValueError:
                print("Bitte geben Sie eine gültige Zahl ein.")
        
        if betrag > eingeloggter_user[2]:
            print("Nicht genügend Guthaben")
        elif betrag <= 0:
            print("Ungültiger Betrag. Der Betrag muss größer als 0 sein.")
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