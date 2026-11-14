
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QSizePolicy,
    QHBoxLayout,
    QSlider, QPushButton,
)


class LecteurPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.creer_interface()

    def creer_interface(self) -> None:
        # disposition de la page
        disposition = QVBoxLayout(self)

        # titre
        titre = QLabel("Lecteur Multimedia")
        disposition.addWidget(titre)

        # section d'affichage
        self.section_affichage = QLabel("Aucun média selectionné")
        self.section_affichage.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )
        self.section_affichage.setMinimumHeight(250)
        self.section_affichage.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )

        disposition.addWidget(self.section_affichage)

        # zone de progression

        progression = QHBoxLayout()

        temps_actuel = QLabel("00:00")
        slider = QSlider(
            Qt.Orientation.Horizontal
        )
        temps_Total = QLabel("00:00")

        progression.addWidget(temps_actuel)
        progression.addWidget(slider)
        progression.addWidget(temps_Total)

        disposition.addLayout(progression)

        # bouton de controle
        controles = QHBoxLayout()

        self.bouton_reculer = QPushButton("⏮")
        self.bouton_lecture = QPushButton("▶️")
        self.bouton_arreter = QPushButton("⏹")
        self.bouton_avancer = QPushButton("⏭")

        controles.addWidget(self.bouton_reculer)
        controles.addWidget(self.bouton_lecture)
        controles.addWidget(self.bouton_arreter)
        controles.addWidget(self.bouton_avancer)

        controles.addStretch()

        # Volume
        self.bouton_volume = QPushButton("🔊")

        self.barre_volume = QSlider(
            Qt.Orientation.Horizontal
        )
        self.barre_volume.setRange(0, 100)
        self.barre_volume.setValue(50)
        self.barre_volume.setFixedWidth(120)

        controles.addWidget(self.bouton_volume)
        controles.addWidget(self.barre_volume)

        # Plein écran
        self.bouton_plein_ecran = QPushButton("⛶")
        controles.addWidget(self.bouton_plein_ecran)

        disposition.addLayout(controles)








