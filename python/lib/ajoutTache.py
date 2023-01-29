import definitionTache
import infoTache

#class utilise pour l'ajout d'une nouvelle tache
class AjoutTache(definitionTache.DefinitionTache, infoTache.Info_Tache):
    def __init__(self, id, texte, check) -> None:
        super().__init__(id, texte, check)
        self.derniere_id = 0
        self.liste_tache = list()
    
    def ajout_d_une_tache(self):
        self.liste_tache = definitionTache.DefinitionTache(self.derniere_id, self.texte, self.check)
        
    def tache_suivante(self) -> int:
        self.derniere_id += 1
        return self.derniere_id
