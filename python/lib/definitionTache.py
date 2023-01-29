#class contenent toutes les caracteristique d'une tache
class DefinitionTache:
    def __init__(self, id:int, texte:str) -> None:
        
        #id de chaque tache
        self.id = id
        
        #text associer dans la tache
        self.texte = texte