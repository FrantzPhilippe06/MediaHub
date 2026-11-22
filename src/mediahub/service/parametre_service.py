import json
from pathlib import Path

class ParametreService:
    def __init__(self) -> None:
        self.fichier_configuration = (Path.home() / "mediahub" / "configuration.json")


    def enregistrer_dossier(self, chemin: Path) -> None:

        # Vérifier que le dossier existe
        if not chemin.is_dir():
            raise ValueError("Le dossier n'existe pas.")

        # Créer le dossier de configuration si nécessaire
        self.fichier_configuration.parent.mkdir(
            parents=True,
            exist_ok=True
        )


        # Préparer les données
        donnees = {
            "dossier_telechargement": str(chemin.resolve())
        }

        # Enregistrer les données dans le fichier JSON
        with self.fichier_configuration.open(
            "w", encoding="utf-8"
        ) as fichier:
            json.dump(donnees, fichier, indent=4)


    def obtenir_dossier(self) -> Path | None:

        # Vérifier si le fichier de configuration existe
        if not self.fichier_configuration.is_file():
            return None

        # Lire le fichier JSON
        with self.fichier_configuration.open(
            "r", encoding="utf-8"
        ) as fichier:
            donnees = json.load(fichier)

        # Récupérer le chemin enregistré
        chemin = donnees.get("dossier_telechargement")

        if not isinstance(chemin, str) or not chemin:
            return None

        # Transformer le chemin en objet Path
        dossier = Path(chemin)

        # Vérifier que le dossier existe toujours
        if not dossier.is_dir():
            return None

        return dossier
