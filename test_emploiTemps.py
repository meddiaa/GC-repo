from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.schedule_table = QtWidgets.QTableWidget(self.centralwidget)
        self.schedule_table.setObjectName("schedule_table")
        self.gridLayout.addWidget(self.schedule_table, 1, 0, 1, 1)
        self.generate_button = QtWidgets.QPushButton(self.centralwidget)
        self.generate_button.setObjectName("generate_button")
        self.gridLayout.addWidget(self.generate_button, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.generate_button.setText(_translate("MainWindow", "Generate Schedule"))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.generate_button.clicked.connect(self.generate_schedule)

    def generate_schedule(self):
        # Obtenez la disponibilité des coachs et des salles à partir de l'interface utilisateur
        coach_availability = self.get_coach_availability()
        room_availability = self.get_room_availability()
        num_sessions_per_day = self.get_num_sessions_per_day()

        # Générez l'emploi du temps
        schedule = self.generate_schedule_from_availability(coach_availability, room_availability, num_sessions_per_day)

        # Affichez l'emploi du temps généré
        self.display_schedule(schedule)

    def get_coach_availability(self):
        # Exemple: Récupérez la disponibilité des coachs à partir de l'interface utilisateur
        # Retournez un dictionnaire où les clés sont les jours de la semaine et les valeurs sont les listes de coachs disponibles
        coach_availability = {}
        # Exemple de remplissage manuel (remplacez cela par votre propre logique d'interface utilisateur)
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            coach_availability[day] = ["Coach A", "Coach B"]  # Liste des coachs disponibles pour chaque jour
        return coach_availability

    def get_room_availability(self):
        # Exemple: Récupérez la disponibilité des salles à partir de l'interface utilisateur
        # Retournez un dictionnaire où les clés sont les jours de la semaine et les valeurs sont les listes de salles disponibles
        room_availability = {}
        # Exemple de remplissage manuel (remplacez cela par votre propre logique d'interface utilisateur)
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            room_availability[day] = ["Room 1", "Room 2"]  # Liste des salles disponibles pour chaque jour
        return room_availability

    def get_num_sessions_per_day(self):
        # Exemple: Récupérez le nombre de séances par jour à partir de l'interface utilisateur
        # Retournez un dictionnaire où les clés sont les jours de la semaine et les valeurs sont le nombre de séances
        num_sessions_per_day = {}
        # Exemple de remplissage manuel (remplacez cela par votre propre logique d'interface utilisateur)
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
            num_sessions_per_day[day] = 2  # Nombre de séances pour chaque jour
        return num_sessions_per_day

    def generate_schedule_from_availability(self, coach_availability, room_availability, num_sessions_per_day):
        # Générez l'emploi du temps à partir des informations de disponibilité fournies
        schedule = []
        for day in coach_availability.keys():
            sessions = []
            for session in range(num_sessions_per_day[day]):
                coach = coach_availability[day][session % len(coach_availability[day])]
                room = room_availability[day][session % len(room_availability[day])]
                sessions.append((coach, room))
            schedule.append(sessions)
        return schedule

    def display_schedule(self, schedule):
        # Affichez l'emploi du temps généré dans la table
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        num_sessions = max(len(sessions) for sessions in schedule)
        self.schedule_table.setRowCount(num_sessions)
        self.schedule_table.setColumnCount(len(days))
        self.schedule_table.setHorizontalHeaderLabels(days)
        for day_index, day in enumerate(days):
            for session_index, session in enumerate(schedule[day_index]):
                coach, room = session
                item = QtWidgets.QTableWidgetItem(f"{coach}, {room}")
                self.schedule_table.setItem(session_index, day_index, item)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
