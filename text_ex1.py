import pytest
from ExDebug1 import environnement_optimal

def test_environnement_optimal():
    # Arrange
    temperature=25
    poussiere= "Faible"
    humidite= 40
    resultat_attendu= "Tout est sous controle"

     # Act. appeler fonction à traiter
    resultat_obtenu =  environnement_optimal(temperature,poussiere,humidite)

    # Assert: verifier le resultat
    assert resultat_attendu == resultat_obtenu

def test_environnement_optimal2():
        # Arrange
        temperature = 30
        poussiere = "Faible"
        humidite = 40
        resultat_attendu = "Environement non optimal"

        # Act. appeler fonction à traiter
        resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

        # Assert: verifier le resultat
        assert resultat_attendu == resultat_obtenu


def test_environnement_optimal3():
    # Arrange
    temperature = 25
    poussiere = "Faible"
    humidite = 20
    resultat_attendu = "Environement non optimal"

    # Act. appeler fonction à traiter
    resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    # Assert: verifier le resultat
    assert resultat_attendu == resultat_obtenu


def test_environnement_optimal4():
    # Arrange
    temperature = 30
    poussiere = "moyen"
    humidite = 25
    resultat_attendu = "Environement non optimal"

    # Act. appeler fonction à traiter
    resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    # Assert: verifier le resultat
    assert resultat_attendu == resultat_obtenu




