import json

filename = "library.json"

# 1. Einmaliges Laden am Anfang
try:
    with open(filename, "r") as f:
        library = json.load(f)
except FileNotFoundError:
    library = []

# 2. Die Endlosschleife für das Menü
while True:
    print("\n--- MEINE BIBLIOTHEK ---")
    print("1. Buch hinzufügen")
    print("2. Bücher anzeigen")
    print("3. Beenden")

    wahl = input("Was möchtest du tun? (1/2/3): ")

    if wahl == "1":
        neu = input("Name des Buches: ")
        library.append(neu)
        # Speichere die Liste direkt nach dem Hinzufügen
        with open(filename, "w") as f:
            json.dump(library, f)

    elif wahl == "2":
        print("\nDeine Bücher:")
        for b in library:
            print(f"- {b}")

    elif wahl == "3":
        print("Bye Bye!")
        break  # Das beendet die Schleife
    else:
        print("Ungültige Eingabe, probier's nochmal.")
