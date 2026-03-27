class Voiture:
    def __init__(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur
    def afficher_info(self):
        print(f'marque: {self.marque}, couleur: {self.couleur}, matricule: {self.matricule}')



