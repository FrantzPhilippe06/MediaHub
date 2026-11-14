from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTableWidgetItem,
    QLabel,
    QTableWidget,
    QHeaderView,
    QAbstractItemView
)


class AccueilPage(QWidget):

    # Interface d'accueil
    def __init__(self) -> None:
        super().__init__()

        self.creer_interface()

    def creer_interface(self) -> None:
        # disposition de la page
        disposition = QVBoxLayout()
        self.setLayout(disposition)

        # titre de la page
        titre = QLabel("Fichier récents")
        disposition.addWidget(titre)

        # tableau
        self.tableau = QTableWidget(0, 4)
        self.tableau.verticalHeader().setVisible(False)
        self.tableau.setHorizontalHeaderLabels(
            ["Nom", "Type", "Taille", "Date"]
        )

        self.tableau.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )
        self.tableau.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        disposition.addWidget(self.tableau)
        # Données fictives pour tester l'affichage
        self.ajouter_fichier(
            "Voyahe.mp4", "Vidéo", "326 Mo", "2025-01-20 14:32"
        )

        self.ajouter_fichier(
            "Musique.mp3", "Audio", "12 Mo", "2025-01-20 14:32"
        )

        self.ajouter_fichier(
            "nature.mp4", "Vidéo", "184 Mo", "2025-01-20 14:32"
        )

    def ajouter_fichier(
            self, nom: str, type: str,
            taille: str, date: str) -> None:
        ligne = self.tableau.rowCount()
        self.tableau.insertRow(ligne)

        self.tableau.setItem(ligne, 0, QTableWidgetItem(nom))
        self.tableau.setItem(ligne, 1, QTableWidgetItem(type))
        self.tableau.setItem(ligne, 2, QTableWidgetItem(taille))
        self.tableau.setItem(ligne, 3, QTableWidgetItem(date))
