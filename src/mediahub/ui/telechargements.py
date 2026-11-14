from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel, QLineEdit,
    QComboBox,
    QPushButton,
    QTableWidget, QTableWidgetItem, QHeaderView,
    QRadioButton
)

class TelechargementsPage(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.creer_interface()

    def creer_interface(self) -> None:
        """Construit les éléments de l'interface."""

        # Disposition principale
        disposition = QVBoxLayout(self)

        # Titre de la page
        titre = QLabel("Téléchargements")
        disposition.addWidget(titre)

        # Champ URL YouTube
        section_url = QHBoxLayout()

        section_url.addWidget(QLabel("URL YouTube : "))

        self.champ_url = QLineEdit()
        self.champ_url.setPlaceholderText(
            "Coller une URL YouTube"
        )
        section_url.addWidget(self.champ_url)

        disposition.addLayout(section_url)

        # Choix du type
        zone_type = QHBoxLayout()
        zone_type.addWidget(QLabel("Type de média : "),2)

        self.t_video = QRadioButton("Vidéo")
        self.t_audio = QRadioButton("Audio")

        self.t_video.setChecked(True)

        zone_type.addWidget(self.t_video,1)
        zone_type.addWidget(self.t_audio,1)

        disposition.addLayout(zone_type)

        # Nom du fichier
        zone_nom = QHBoxLayout()
        zone_nom.addWidget(QLabel("Nom du fichier : "),2)

        self.champ_nom = QLineEdit()
        self.champ_nom.setPlaceholderText(
            "Nom du fichier"
        )

        zone_nom.addWidget(self.champ_nom,7)

        # Bouton Ajouter
        self.bouton_ajouter = QPushButton("Ajouter")

        zone_nom.addWidget(self.bouton_ajouter,2)

        disposition.addLayout(zone_nom)

        # Titre de la liste
        disposition.addWidget(
            QLabel("Liste des téléchargements")
        )

        # Tableau
        self.tableau = QTableWidget(0, 4)

        self.tableau.setHorizontalHeaderLabels(
            ["Nom", "Type", "Taille", "Statut"]
        )

        self.tableau.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.tableau.verticalHeader().setVisible(False)

        disposition.addWidget(self.tableau)

        # Connexion
