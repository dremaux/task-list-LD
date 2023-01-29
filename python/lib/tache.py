import infoTache
import definitionTache

class Tache(infoTache.Info_Tache, definitionTache.DefinitionTache):
    def __init__(self, id, texte, check) -> None:
        infoTache.Info_Tache.__init__(self, check)
        definitionTache.DefinitionTache.__init__(self, id, texte)
    
    def check(self):
        if self.check:
            return True
        return False