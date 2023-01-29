import ajoutTache

class AfficherTache(ajoutTache.AjoutTache):
    
    def __init__(self, id, texte, liste_des_taches):
        ajoutTache.AjoutTache.__init__(id, texte, liste_des_taches)
    
    def show(self):
        for tache in self.liste_tache:
            affichageFinal = str(tache.id) + ", " + str(tache.texte) + (", ") + " etat : "
            etat = "non fini"
            if tache.check == "True":
                etat = "fini"
            print(affichageFinal + etat)