from PyQt5 import QtWidgets, QtGui
import sys
import random


class EmploiDuTempsApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Créez le layout principal
        main_layout = QtWidgets.QVBoxLayout()

        # Création des champs de saisie
        self.coach_input = QtWidgets.QLineEdit()
        self.salle_input = QtWidgets.QLineEdit()
        self.groupe_input = QtWidgets.QLineEdit()

        # Ajoutez les étiquettes et les champs au layout
        main_layout.addWidget(QtWidgets.QLabel("Liste des coachs (séparés par des virgules):"))
        main_layout.addWidget(self.coach_input)

        main_layout.addWidget(QtWidgets.QLabel("Liste des salles (séparées par des virgules):"))
        main_layout.addWidget(self.salle_input)

        main_layout.addWidget(QtWidgets.QLabel("Liste des groupes (séparés par des virgules):"))
        main_layout.addWidget(self.groupe_input)

        # Créez le bouton pour générer l'emploi du temps
        self.generate_button = QtWidgets.QPushButton("Générer l'emploi du temps")
        self.generate_button.clicked.connect(self.generate_schedule)
        main_layout.addWidget(self.generate_button)

        # Créez un tableau pour afficher l'emploi du temps
        self.schedule_table = QtWidgets.QTableWidget()
        self.schedule_table.setRowCount(7)  # Dimanche à samedi
        self.schedule_table.setColumnCount(2)  # Deux séances par jour
        self.schedule_table.setHorizontalHeaderLabels(["Séance 1", "Séance 2"])
        self.schedule_table.setVerticalHeaderLabels(
            ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
        )
        main_layout.addWidget(self.schedule_table)

        self.setLayout(main_layout)

    def generate_schedule(self):
        # Récupérez les valeurs saisies par l'utilisateur
        coachs = self.coach_input.text().split(',')
        salles = self.salle_input.text().split(',')
        groupes = self.groupe_input.text().split(',')

        # Pour éviter les conflits, utilisez des ensembles pour garder la trace des éléments déjà utilisés
        used_coaches = {}  # Clé : (jour, séance), Valeur : liste de coachs
        used_salles = {}  # Clé : (jour, séance), Valeur : liste de salles
        used_groupes = {}  # Clé : jour, Valeur : liste de groupes

        for i in range(7):  # Pour chaque jour de la semaine
            used_groupes[i] = set()  # Assurez-vous qu'un groupe n'est pas utilisé plusieurs fois par jour
            for j in range(2):  # Deux séances par jour
                valid = False
                while not valid:
                    # Choisissez un coach, une salle et un groupe aléatoirement
                    coach = random.choice(coachs).strip()
                    salle = random.choice(salles).strip()
                    groupe = random.choice(groupes).strip()

                    # Vérifiez les conflits
                    coach_conflict = coach in used_coaches.get((i, j), [])
                    salle_conflict = salle in used_salles.get((i, j), [])
                    groupe_conflict = groupe in used_groupes[i]

                    if not (coach_conflict or salle_conflict or groupe_conflict):
                        valid = True
                        # Ajoutez les éléments utilisés à l'ensemble
                        if (i, j) not in used_coaches:
                            used_coaches[(i, j)] = []
                        used_coaches[(i, j)].append(coach)

                        if (i, j) not in used_salles:
                            used_salles[(i, j)] = []
                        used_salles[(i, j)].append(salle)

                        used_groupes[i].add(groupe)

                        # Créez le texte à afficher dans le tableau
                        session_info = f"Coach: {coach}\nSalle: {salle}\nGroupe: {groupe}"
                        self.schedule_table.setItem(i, j, QtWidgets.QTableWidgetItem(session_info))


# Créez une application PyQt5
app = QtWidgets.QApplication(sys.argv)
window = EmploiDuTempsApp()
window.show()
sys.exit(app.exec_())
