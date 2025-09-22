"""def retrait(solde:str = 0, retrait: float = 0) -> bool:
    if retrait > solde:
        retrait = solde
        print(f"* Solde insuffisant, retrait effectué: {retrait} $")

    else:
        solde = solde - retrait
        print(f"* Retrait effectué: {retrait}")

    return solde

if __name__ == "__main__":
    MONTANT_INITIAL = 1000

    solde = MONTANT_INITIAL

    print("*************************")
    print("***      GUICHET      ***")
    print("*************************")
    print(f"Solde initial:  {solde} $")
    print("*************************")

    retrait_1 = float(input("Retrait 1: Combien voulez-vous retirer? "))
    solde = retrait(solde, retrait_1)

    retrait_2 = float(input("Retrait 2: Combien voulez-vous retirer? "))
    solde = retrait()

    print("*********************")
    print(f"Solde initial: {MONTANT_INITIAL} $")
    print(f"Retrait 1:     {retrait_1} $")
    print(f"Retrait 2:     {retrait_2} $")
    print(f"Solde final:    {solde} $")
    print(f"*********************")
"""

def retrait(solde: float = 0, montant: float = 0) -> float:
    # Vérifier si le montant est négatif ou nul
    if montant <= 0:
        print("* Retrait invalide. Aucun montant retiré.")
        return solde

    # Vérifier si le solde est suffisant
    if montant > solde:
        print(f"* Solde insuffisant, retrait de {solde} $ effectué.")
        solde = 0
else:
    solde -= montant
    print(f"* Retrait effectué: {montant} $")

return solde


if __name__ == "__main__":
    MONTANT_INITIAL = 1000
    solde = MONTANT_INITIAL

    print("*************************")
    print("***      GUICHET      ***")
    print("*************************")
    print(f"Solde initial:  {solde} $")
    print("*************************")


  # Retrait 1
    retrait_1 = float(input("Retrait 1: Combien voulez-vous retirer? "))
    solde = retrait(solde, retrait_1)

    # Retrait 2
    retrait_2 = float(input("Retrait 2: Combien voulez-vous retirer? "))
    solde = retrait(solde, retrait_2)

   print("*********************")
    print(f"Solde initial: {MONTANT_INITIAL} $")
    print(f"Retrait 1:     {retrait_1} $")
    print(f"Retrait 2:     {retrait_2} $")
    print(f"Solde final:   {solde} $")
    print("*********************")