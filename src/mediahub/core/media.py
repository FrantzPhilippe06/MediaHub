from pathlib import Path
class Media:
    def __init__(self, nom: str, url: Path, type_media: str, taille: str ) -> None:
        self.nom = nom,
        self.url = url,
        self.type_media = type_media,
        self.taille = taille

    @classmethod
    def depuis_fichier(cls, chemein: Path) -> "Media":

        if not chemein.is_file():
            raise FileNotFoundError(f"Fichier introuvable : {chemein}")

        nom = chemein.name
        taille = chemein.stat().st_size
        extension = chemein.suffix.lower()

        if extension in [".mp4", ".mkv", ".avi", ".mov", ".wmv",".webm", ".ogv"]:
            type_media = "video"
        elif extension in [".mp3", ".wav", ".flac", ".ogg",".aac"]:
            type_media = "audio"
        else:
            raise ValueError(
                f"Format nom prise en charge : {extension}"
            )
        return cls(nom, chemein, type_media, str(taille))