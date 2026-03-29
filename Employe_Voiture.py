class Employe:
    def __init__(self,num_permis,nom,prenom):
        self.num_permis=num_permis
        self.nom=nom
        self.prenom=prenom
        self.voiture_service= None
    def afficher_info(self):
        print(f"Nom : {self.nom}, Prenom : {self.prenom},Permis : {self.num_permis}")
        if self.voiture_service is None:
            print("Aucune voiture de service pour ce chauffeur")
        else :
            print(f"Voiture service : {self.voiture_service.matricule}")
    def ajouter_voiture(self,voiture):
        if self.voiture_service is not None:
            print("Le Chauffeur a deja une voiture de service")
        elif voiture.chauffeur is not None:
            print("La voiture est deja affecter a un chauffeur")
        else:
            self.voiture_service = voiture
            voiture.chauffeur = self

    def retirer_voiture(self,voiture):
        if self.voiture_service is None:
            print("aucune voiture n'est deja affecter")
        elif self.voiture_service != voiture:
            print("Cette voiture n'est pas affecter a ce chauffeur")
        else :
            self.voiture_service = None
            voiture.chauffeur = None
            print("Voiture retirée")

class Voiture:
    def __init__(self,matricule,marque,modele,annee,kilometrage):
        self.matricule=matricule
        self.marque=marque
        self.modele=modele
        self.annee=annee
        self.kilometrage=kilometrage
        self.chauffeur = None

    def afficher_info(self):
        print(f"marque : {self.marque}, modele : {self.modele},anne: {self.annee}"
              f",matricule: {self.matricule}, kilometrage: {self.kilometrage}")
        if self.chauffeur is None:
            print("Aucun chauffeur pour cette voiture")
        else :
            print(f"Chauffeur : {self.chauffeur.nom},{self.chauffeur.prenom},{self.chauffeur.num_permis}")

#instances Employe
E1=Employe("H1026-606590-09","Hafsi","Nabil")
E2=Employe("A8937-598001-11","Aftis","Naser")
E3=Employe("B1204-100453-06","Belhennich","Amine")
E4=Employe("B5689-004587-10","Boussekine","Nordine")

#instances Voiture

V1=Voiture("GKL 9V1","Dodge", "Caravane",2018,171987)
V2=Voiture("SMA P4O","Toyota","Sienna",2023,101679)
V3=Voiture("JLC 99T","Honda","Odyssey",2016,220198)
V4=Voiture("13L JS0","Ford","Transit","2021",167547)

#Affichage des Informations
"""print("----Liste Chaufffeurs----")
E1.afficher_info()
E2.afficher_info()
E3.afficher_info()
E4.afficher_info()
print("----Liste Voitures----")
V1.afficher_info()
V2.afficher_info()
V3.afficher_info()
V4.afficher_info()"""

#Ajout de voiture au chauffeur
E1.ajouter_voiture(V2)
E2.ajouter_voiture(V4)
E3.ajouter_voiture(V1)

#Afficher les informations
"""E1.afficher_info()
E2.afficher_info()
E3.afficher_info()"""

#Retirer une voiture

E1.retirer_voiture(V2)
E3.retirer_voiture(V4)
E2.retirer_voiture(V4)
E4.retirer_voiture(V1)









