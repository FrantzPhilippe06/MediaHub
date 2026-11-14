from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QLineEdit,
    QScrollArea, QDialog,
    QMessageBox, QStackedWidget
)

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("MediaHub")
       # self.resize(1100, 700)
        self.setMinimumSize(800,500)


        # conteneur principale
        conteneur = QWidget()
        self.setCentralWidget(conteneur)

        # disposition principale
        disposition = QHBoxLayout(conteneur)

        # disposition laterale section du menu
        menu = QVBoxLayout()

        # bouton de navigation du menu
        bouton_accueil = QPushButton("Accueil")
        bouton_lecteur = QPushButton("Lecteur")
        bouton_telechargements = QPushButton("Téléchargements")
        bouton_params = QPushButton("Parametre")

        menu.addWidget(bouton_accueil)
        menu.addWidget(bouton_lecteur)
        menu.addWidget(bouton_telechargements)
        menu.addWidget(bouton_params)

        # disposition pour les pages
        self.pages =QStackedWidget()

        self.pages.addWidget(QLabel("Bienvenue sur MediaHub"))
        self.pages.addWidget(QLabel("Lecteur"))
        self.pages.addWidget(QLabel("Téléchargements"))
        self.pages.addWidget(QLabel("Paramètres"))

        # connexion
        bouton_accueil.clicked.connect(lambda: self.pages.setCurrentIndex(0))
        bouton_lecteur.clicked.connect(lambda: self.pages.setCurrentIndex(1))
        bouton_telechargements.clicked.connect(lambda: self.pages.setCurrentIndex(2))
        bouton_params.clicked.connect(lambda: self.pages.setCurrentIndex(3))

        # assemblage
        disposition.addLayout(menu,1)
        disposition.addWidget(self.pages, 4)
