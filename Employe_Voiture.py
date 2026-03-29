class Employe:
    def __init__(self,num_permis,nom,prenom):
        self.num_permis=num_permis
        self.nom=nom
        self.prenom=prenom
        self.voiture_service= None
    def afficher_info(self):
        print(f"Nom : {self.nom}, Prenom : {self.prenom},num_permis : {self.num_permis}")
        if self.voiture_service is None:
            print("Aucune voiture de service pour ce chauffeur")
        else :
            print(f"Voiture service : {self.voiture_service.afficher_info()}")
    def ajouter_voiture(self,voiture):
        if self.voiture_service is not None:
            print("Le Chauffeur a deja une voiture de service")
        elif voiture.chauffeur is not None:
            print("La voiture est deja affecter a un chauffeur")
        else:
            self.voiture_service = voiture
            voiture.chauffeur = self

    def retirer_voiture(self,voiture):
        if self.voiture_service is not None:
            self.voiture_service = None
            voiture.chauffeur = None
            print("Voiture retirée")
        else:
            print("Aucune voiture attribué a ce chaffeur")



