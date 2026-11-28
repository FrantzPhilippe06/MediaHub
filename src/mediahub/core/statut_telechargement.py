from enum import Enum

class StatutTelechargement(Enum):
    EN_ATTENTE = "En attente"
    EN_COURS = "En cours"
    TERMINE = "Terminé"
    ECHEC = "Échec"