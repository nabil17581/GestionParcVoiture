class Voiture:
    def __init__(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur
    def afficher_info(self):
        print(f'marque: {self.marque}, couleur: {self.couleur}, matricule: {self.matricule}')


class Parc:
    def __init__(self,identifiant,adresse,capacite):
        self.identifiant = identifiant
        self.adresse = adresse
        self.capacite = capacite
        self.liste_voiture = []

    def entrer_voiture(self,voiture):
        if voiture in self.liste_voiture:
            print("est deja dans le parc")
        elif len(self.liste_voiture) >= self.capacite:
            print("Parc plein")
        else :
            self.liste_voiture.append(voiture)
            print("Voiture ajouter avec succes")


    def sortir_voiture(self,voiture):
        if voiture not in self.liste_voiture:
            print("Voiture non trouvée dans le parc")
        else:
            self.liste_voiture.remove(voiture)
            print(f"Voiture retirée")
            print(f"Places libre:", self.compterNombrePlace())
    def compterNombrePlace(self):
        cap = self.capacite - len(self.liste_voiture)
        return cap
