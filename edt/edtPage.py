
from PyQt5 import QtCore, QtGui, QtWidgets
from random import choice, shuffle
from collections import defaultdict
from connexion_DB import connect_to_DB
import random


class Ui_MainWindowEDT(object):
    def setupUi(self, MainWindowEDT):
        MainWindowEDT.setObjectName("MainWindowEDT")
        MainWindowEDT.resize(1181, 625)
        MainWindowEDT.setStyleSheet("QMainWindow#MainWindowEDT{\n"
"\n"
"background-color: rgb(210, 210, 210);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindowEDT)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{\n"
"\n"
"background-color: rgb(210, 210, 210);\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(10, 2, 10, 2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(26, 61, 119);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEditListeCoaches = QtWidgets.QLineEdit(self.widget_2)
        self.lineEditListeCoaches.setMinimumSize(QtCore.QSize(950, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEditListeCoaches.setFont(font)
        self.lineEditListeCoaches.setStyleSheet("border-radius: 2px;")
        self.lineEditListeCoaches.setObjectName("lineEditListeCoaches")
        self.verticalLayout_3.addWidget(self.lineEditListeCoaches)
        self.lineEditListeGroupes = QtWidgets.QLineEdit(self.widget_2)
        self.lineEditListeGroupes.setMinimumSize(QtCore.QSize(950, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditListeGroupes.setFont(font)
        self.lineEditListeGroupes.setStyleSheet("border-radius: 2px;")
        self.lineEditListeGroupes.setObjectName("lineEditListeGroupes")
        self.verticalLayout_3.addWidget(self.lineEditListeGroupes)
        self.lineEditListesSalles = QtWidgets.QLineEdit(self.widget_2)
        self.lineEditListesSalles.setMinimumSize(QtCore.QSize(950, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditListesSalles.setFont(font)
        self.lineEditListesSalles.setStyleSheet("border-radius: 2px;")
        self.lineEditListesSalles.setObjectName("lineEditListesSalles")
        self.verticalLayout_3.addWidget(self.lineEditListesSalles)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonRefaire = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonRefaire.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButtonRefaire.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRefaire.setIcon(icon)
        self.pushButtonRefaire.setObjectName("pushButtonRefaire")
        self.horizontalLayout.addWidget(self.pushButtonRefaire)
        self.pushButtonSauvgarder = QtWidgets.QPushButton(self.widget_2)
        self.pushButtonSauvgarder.setMinimumSize(QtCore.QSize(20, 40))
        self.pushButtonSauvgarder.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/diskette.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonSauvgarder.setIcon(icon1)
        self.pushButtonSauvgarder.setObjectName("pushButtonSauvgarder")
        self.horizontalLayout.addWidget(self.pushButtonSauvgarder)
        self.horizontalLayout.setStretch(0, 3)
        self.verticalLayout.addWidget(self.widget_2)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 7)
        MainWindowEDT.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindowEDT)
        QtCore.QMetaObject.connectSlotsByName(MainWindowEDT)
        MainWindowEDT.showMaximized()
        self.afficher_coach()
        self.pushButtonRefaire.clicked.connect(self.generer_edt)
        self.pushButtonSauvgarder.clicked.connect(self.sauvegarder_edt)
        self.afficher_edt()
        self.tableWidget.setColumnWidth(0,250)
        self.tableWidget.setColumnWidth(1, 250)
        self.tableWidget.setColumnWidth(2, 250)
        self.tableWidget.setColumnWidth(3, 250)
        self.tableWidget.setColumnWidth(4, 250)
        self.tableWidget.setColumnWidth(5, 250)
        self.tableWidget.setColumnWidth(6, 250)

    def retranslateUi(self, MainWindowEDT):
        _translate = QtCore.QCoreApplication.translate
        MainWindowEDT.setWindowTitle(_translate("MainWindowEDT", "MainWindow"))
        self.label.setText(_translate("MainWindowEDT", "Emploi du temps"))
        self.lineEditListeCoaches.setPlaceholderText(_translate("MainWindowEDT", "Veuillez Entrer la liste des coaches (séparés par des virgules)"))
        self.lineEditListeGroupes.setPlaceholderText(_translate("MainWindowEDT", "Veuillez entrer la listes des groupes (séparés par des virgules)"))
        self.lineEditListesSalles.setPlaceholderText(_translate("MainWindowEDT", "Veuillez entrer la liste des salles (séparés par des virgules)"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindowEDT", "Dimanche"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindowEDT", "Lundi"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindowEDT", "Mardi"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindowEDT", "Mercredi"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindowEDT", "Jeudi"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindowEDT", "Vendredi"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindowEDT", "Samedi"))

    def afficher_edt(self):
        connection, cursor = connect_to_DB()
        query = "SELECT Dimanche,Lundi,Mardi,Mercredi,Jeudi,Vendredi,Samedi FROM edt"
        cursor.execute(query)
        data = cursor.fetchall()
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        for numero_ligne, donnees_ligne in enumerate(data):
            self.tableWidget.insertRow(numero_ligne)
            for numero_colonne, donnee_colonne in enumerate(donnees_ligne):
                item = QtWidgets.QTableWidgetItem(str(donnee_colonne))
                item.setFont(QtGui.QFont("Arial", 12))
                self.tableWidget.setItem(numero_ligne, numero_colonne, item)
        self.tableWidget.setRowHeight(0, 150)
        self.tableWidget.setRowHeight(1, 150)
        self.tableWidget.setRowHeight(2, 150)
        self.tableWidget.setRowHeight(3, 150)

    def afficher_coach(self):
        connection, cursor = connect_to_DB()
        cursor.execute("SELECT nom FROM coach")
        result_coaches = cursor.fetchall()
        liste_coaches = [row[0] for row in result_coaches]
        coaches_avec_virgules = ", ".join(liste_coaches)
        self.lineEditListeCoaches.setText(coaches_avec_virgules)
        cursor.close()
        connection.close()

    def generer_edt(self):
        coaches = self.lineEditListeCoaches.text().split(',')
        groupes = self.lineEditListeGroupes.text().split(',')
        salles = self.lineEditListesSalles.text().split(',')

        coaches = [coach.strip() for coach in coaches if coach.strip()]
        groupes = [groupe.strip() for groupe in groupes if groupe.strip()]
        salles = [salle.strip() for salle in salles if salle.strip()]

        if not coaches or not groupes or not salles:
            QtWidgets.QMessageBox.warning(
                self.centralwidget,
                "Données manquantes",
                "Veuillez remplir les listes des coaches, des groupes, et des salles."
            )
            return

        jours = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]

        self.tableWidget.setRowCount(0)
        self.tableWidget.clear()

        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(4)

        for idx, jour in enumerate(jours):
            item = QtWidgets.QTableWidgetItem(jour)
            self.tableWidget.setHorizontalHeaderItem(idx, item)

        coach_count = defaultdict(int)  # Nombre de séances par coach
        salle_occupee = {jour: set() for jour in jours}  # Salles occupées par jour
        groupe_dernier_jour = defaultdict(lambda: -2)  # Dernier jour où le groupe a été utilisé

        seances = []

        # Générer les séances par jour
        for jour in jours:
            nb_seances = random.randint(0, 4)

            for _ in range(nb_seances):
                available_coaches = [c for c in coaches if coach_count[c] < 3]
                if not available_coaches:
                    continue

                coach = random.choice(available_coaches)
                coach_count[coach] += 1

                available_salles = [salle for salle in salles if salle not in salle_occupee[jour]]
                if not available_salles:
                    continue

                salle = random.choice(available_salles)
                salle_occupee[jour].add(salle)

                if jour in jours:
                    index_jour = jours.index(jour)
                    available_groupes = [groupe for groupe in groupes
                                         if index_jour - groupe_dernier_jour[groupe] > 1]

                    if not available_groupes:
                        continue

                    groupe = random.choice(available_groupes)
                    groupe_dernier_jour[groupe] = index_jour

                    texte_seance = f"Coach : {coach}\nGroupe : {groupe}\nSalle : {salle}"

                    seances.append((jour, texte_seance))

        for jour in jours:
            index_jour = jours.index(jour)

            seances_du_jour = [s for s in seances if s[0] == jour]

            for index, (j, texte_seance) in enumerate(seances_du_jour[:4]):

                item = QtWidgets.QTableWidgetItem(texte_seance)
                self.tableWidget.setRowHeight(0, 150)
                self.tableWidget.setRowHeight(1, 150)
                self.tableWidget.setRowHeight(2, 150)
                self.tableWidget.setRowHeight(3, 150)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                item.setFont(QtGui.QFont("Arial", 12))
                self.tableWidget.setItem(index, index_jour, item)

    def sauvegarder_edt(self):
        try:
            connection, cursor = connect_to_DB()
            cursor.execute("DELETE FROM edt")
            jours = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
            contenu_edt = []
            for row in range(self.tableWidget.rowCount()):
                ligne = {}
                for col, jour in enumerate(jours):
                    item = self.tableWidget.item(row, col)
                    if item:
                        ligne[jour] = item.text()
                    else:
                        ligne[jour] = None
                contenu_edt.append(ligne)
            for ligne in contenu_edt:
                cursor.execute(
                    "INSERT INTO edt (Dimanche, Lundi, Mardi, Mercredi, Jeudi, Vendredi, Samedi) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (ligne["Dimanche"], ligne["Lundi"], ligne["Mardi"], ligne["Mercredi"], ligne["Jeudi"],
                     ligne["Vendredi"], ligne["Samedi"])
                )
            connection.commit()
            QtWidgets.QMessageBox.information(
                self.centralwidget,
                "Sauvegarde réussie",
                "L'emploi du temps a été sauvegardé avec succès dans la base de données."
            )

        except mysql.connector.Error as err:
            # Gérer les erreurs de connexion ou de requête SQL
            QtWidgets.QMessageBox.critical(
                self.centralwidget,
                "Erreur de sauvegarde",
                f"Une erreur s'est produite lors de la sauvegarde: {err}"
            )

        finally:
            # Fermer le curseur et la connexion
            if cursor:
                cursor.close()
            if connection:
                connection.close()


import edt_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowEDT = QtWidgets.QMainWindow()
    ui = Ui_MainWindowEDT()
    ui.setupUi(MainWindowEDT)
    MainWindowEDT.show()
    sys.exit(app.exec_())
