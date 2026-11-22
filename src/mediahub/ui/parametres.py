from mediahub.service.parametre_service import ParametreService
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout, QLabel,
    QLineEdit,
    QPushButton,
    QComboBox, QCheckBox, QFileDialog,
    QMessageBox,
)
from pathlib import Path


class ParametresPage(QWidget):

    def __init__(self) -> None:
        super().__init__()

        self.creer_interface()
        self.configuration_service = ParametreService()
        self.charger_parametre()

    def creer_interface(self) -> None:
        # l'interface des paramètres.

        disposition = QVBoxLayout(self)

        # Titre
        titre = QLabel("Paramètres")
        disposition.addWidget(titre)

        # Dossier de téléchargement
        dossier_layout = QHBoxLayout()
        self.champ_dossier = QLineEdit()
        self.champ_dossier.setReadOnly(True)
        self.bouton_parcourir = QPushButton("Parcourir")

        dossier_layout.addWidget(QLabel("Dossier de téléchargement"), 2)
        dossier_layout.addWidget(self.champ_dossier, 7)
        dossier_layout.addWidget(self.bouton_parcourir, 1)

        disposition.addLayout(dossier_layout)

        # Qualité vidéo
        qualité_layout = QHBoxLayout()

        self.choix_qualite = QComboBox()
        self.choix_qualite.addItems([
            "Meilleure disponible",
            "1080p",
            "720p",
            "480p",
            "360p"
        ])
        qualité_layout.addWidget(QLabel("Qualité vidéo par défaut"), 1)
        qualité_layout.addWidget(self.choix_qualite, 4)

        disposition.addLayout(qualité_layout)

        # Format

        format_layout = QHBoxLayout()

        format_layout.addWidget(QLabel("Format par défaut"), 1)

        self.choix_format = QComboBox()
        self.choix_format.addItems([
            "MP4",
            "MP3"
        ])
        format_layout.addWidget(self.choix_format, 4)
        disposition.addLayout(format_layout)

        # Options
        self.case_lecture_auto = QCheckBox(
            "Lecture automatique après téléchargement"
        )

        self.case_notifications = QCheckBox(
            "Notifications de fin de téléchargement"
        )

        disposition.addWidget(self.case_lecture_auto)
        disposition.addWidget(self.case_notifications)

        # Boutons
        disposition.addStretch()

        boutons_layout = QHBoxLayout()

        self.bouton_annuler = QPushButton("Annuler")
        self.bouton_enregistrer = QPushButton("Enregistrer")

        boutons_layout.addWidget(self.bouton_annuler)
        boutons_layout.addWidget(self.bouton_enregistrer)

        disposition.addLayout(boutons_layout)

        # connexion
        self.bouton_parcourir.clicked.connect(self.choisir_dossier)
        self.bouton_enregistrer.clicked.connect(self.enregistrer_parametres)

    def choisir_dossier(self) -> None:
        # Ouvre une boîte de dialogue pour choisir un dossier.

        dossier = QFileDialog.getExistingDirectory(
            self,
            "Choisir le dossier de téléchargement"
        )

        if dossier:
            self.champ_dossier.setText(dossier)

    def enregistrer_parametres(self) -> None:

        chemin = self.champ_dossier.text().strip()

        if not chemin:
            QMessageBox.warning(
                self,
                "Attention",
                "Veuillez sélectionner un dossier."
            )
            return

        self.configuration_service.enregistrer_dossier(
            Path(chemin)
        )

        QMessageBox.information(
            self,
            "Succès",
            "Dossier de téléchargement enregistré."
        )
    def charger_parametre(self) ->None :
        dossier = self.configuration_service.obtenir_dossier()
        if dossier is not None:
            self.champ_dossier.setText(str(dossier))