def environnement_optimal(temp, poussiere, humidite):
    """
    Vérifie si l'environnement d'un ordinateur est optimal.

    Paramètres :
    - temp : température en °C (int ou float)
    - poussiere : niveau de poussière ("faible", "moyen", "élevé")
    - humidite : taux d’humidité en % (int ou float)

    Retour :
    - "Tout est sous contrôle!" si toutes les conditions sont respectées
    - "Environnement non optimal" sinon (après avoir affiché les problèmes détectés)
    """

    alerte = False

    # Vérification température
    if temp < 18:
        print("Température trop basse")
        alerte = True
    elif temp > 27:
        print("Température trop élevée")
        alerte = True

    # Vérification humidité
    if humidite <= 30:
        print("Humidité trop basse")
        alerte = True
    elif humidite >= 50:
        print("Humidité trop élevée")
        alerte = True

    # Vérification poussière
    if poussiere != "faible":
        print("Trop de poussière")
        alerte = True

    # Retour final
    if not alerte:
        return "Tout est sous contrôle!"
    else:
        return "Environnement non optimal"


if __name__ == "__main__":
#print(environnement_optimal(25, "faible", 40))
#TODO: Creer 3 listes
listes_temp= [10,13,15,17,20]
listes_mots=["Te"]


#TODO : pour 3 Ordinateur
nb_ordinateur=input("Entre le nombre d'ordi")



    #TODO : Demander temp, poussiere, humidite
    #TODO : Mettres les 3 valeurs dans leurs listes

temp= float(input("Entrez la température:"))
poussiere=input("Entrez le niveau de poussiere :")
humidite=float("Entrez l'humidité:")
print(environnement_optimal(temp,poussiere,humidite))


#TODO : Pour les 3 ordinateur
    #TODO : utiliser la fonction et afficher le résultat
print(environnement_optimal(temp,poussiere,humidite))