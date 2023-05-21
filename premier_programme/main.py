nom = input("Quel est votre nom ? ")
age = input("Quel est votre âge ? ")

try:
    age_prochain = int(age) + 1
except ValueError:
    print("ERREUR: Vous devez rentrer un nombre pour l'âge.")
else:
    print(f"Vous vous appelez {nom}. Vous avez {age} ans.")
    print(f"L'an prochain vous aurez {age_prochain} ans.")


