
from PySide6.QtCore import Qt, QUrl
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QSizePolicy,
    QHBoxLayout,
    QSlider, QPushButton,
)
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from pathlib import Path
from PySide6.QtMultimediaWidgets import QVideoWidget

class LecteurPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.player = QMediaPlayer(self)
        self.audio_output = QAudioOutput(self)
        self.player.setAudioOutput(self.audio_output)

        self.creer_interface()
        self.player.setVideoOutput(self.zone_video)

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

        # Zone d'affichage de la vidéo
        self.zone_video = QVideoWidget()

        self.zone_video.setMinimumHeight(250)
        disposition.addWidget(self.zone_video)

        self.tire_media = QLabel("---------")
        disposition.addWidget(self.tire_media)

        # zone de progression

        progression = QHBoxLayout()

        temps_actuel = QLabel("00:00")
        slider = QSlider(Qt.Orientation.Horizontal)
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

     #connexion
        self.bouton_lecture.clicked.connect(self.player.play)
        self.bouton_arreter.clicked.connect(self.player.pause)

    def selectionner_media(self, chemin: Path) -> None:

        self.section_affichage.setText("")
        self.tire_media.setText(chemin.name)

        self.player.setSource(QUrl.fromLocalFile(str(chemin.resolve())))