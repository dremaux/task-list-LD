# 1.(1pts) un seul niveau d'indentation par méthode                             => ok

# 2.(1pts) ne pas utiliser le mot-clé "ELSE"                                    => ok

# 3.(3pts) envelopper toutes les primitives et les chaînes de caractères        => besion d'aide / pas compris

# 4.(2pts) collections de première classe                                       => si j'ai bien compris ok

# 5.(2pts) un point par ligne                                                   => ok

# 6.(6pts) ne pas abréger                                                       => si je suis pas bête ok

# 7.(2pts) garder toutes les entités petites                                    => si j'ai bien compris ok

# 8.(3pts) pas de classes avec plus de deux variables d'instance                => si j'ai bien compris ok

# 9.(3pts) pas de getters/setters/properties                                    => ok


# ajout d'une règle personnel 
# 10. fair fonctionner le code ( c'est mieux )


import lib.afficherTache
import lib.ajoutTache 
import lib.definitionTache 
import lib.infoTache
import lib.tache

id_tache = lib.definitionTache.DefinitionTache(0, "fini le TP")
une_tache = lib.ajoutTache.AjoutTache(id_tache, False)

lib.ajoutTache.AjoutTache(une_tache)

lib.afficherTache.ajoutTache(lib.ajoutTache.AjoutTache)
