import re

def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur: Division par zéro"
    return a / b

def calculatrice():
    historique = []

    while True:
        print("Options disponibles :")
        print("1. Addition (+)")
        print("2. Soustraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Afficher l'historique")
        print("6. Effacer l'historique")
        print("7. Quitter")

        choix = input("Choisissez une option (1-7) : ")

        if choix in ['1', '2', '3', '4']:
            nombre1 = input("Entrez le premier nombre : ")
            nombre2 = input("Entrez le deuxième nombre : ")

            # Vérification des entrées
            if not re.match(r'^-?\d+\.?\d*$', nombre1) or not re.match(r'^-?\d+\.?\d*$', nombre2):
                print("Erreur: Entrez des nombres valides.")
                continue

            nombre1 = float(nombre1)
            nombre2 = float(nombre2)

            if choix == '1':
                resultat = addition(nombre1, nombre2)
                operation = f"{nombre1} + {nombre2} = {resultat}"
            elif choix == '2':
                resultat = soustraction(nombre1, nombre2)
                operation = f"{nombre1} - {nombre2} = {resultat}"
            elif choix == '3':
                resultat = multiplication(nombre1, nombre2)
                operation = f"{nombre1} * {nombre2} = {resultat}"
            elif choix == '4':
                resultat = division(nombre1, nombre2)
                if isinstance(resultat, str):
                    print(resultat)
                    continue
                operation = f"{nombre1} / {nombre2} = {resultat}"

            print(f"Résultat : {resultat}")
            historique.append(operation)

        elif choix == '5':
            if not historique:
                print("L'historique est vide.")
            else:
                print("Historique des opérations :")
                for operation in historique:
                    print(operation)

        elif choix == '6':
            historique = []
            print("Historique effacé.")

        elif choix == '7':
            print("Au revoir !")
            break

        else:
            print("Erreur: Choix invalide. Veuillez choisir un nombre entre 1 et 7.")

calculatrice()
