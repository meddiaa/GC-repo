from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QTextEdit , QLabel, QComboBox, QLineEdit
from datetime import datetime, timedelta
import mysql.connector
from connexion_DB import connect_to_DB
from addMember.ajouterMembre import UI_MainWindowAjouterMembre
from modifyMember.modifierMembre import Ui_MainWindowModifierMembre

class Ui_membres(object):
    def setupUi(self, membres):
        membres.setObjectName("membres")
        membres.resize(1327, 576)
        membres.setStyleSheet("background-color: rgb(210, 210, 210);")
        membres.setWindowIcon(QtGui.QIcon("../resourcesGenerales/iconGC.png"))
        self.gridLayout = QtWidgets.QGridLayout(membres)
        self.gridLayout.setObjectName("gridLayout")
        self.topheader = QtWidgets.QWidget(membres)
        self.topheader.setStyleSheet("\n"
"background-color:  rgb(210, 210, 210)")
        self.topheader.setObjectName("topheader")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.topheader)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.topheader)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(26, 61, 119);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout.addWidget(self.topheader, 0, 0, 1, 1)
        self.table = QtWidgets.QWidget(membres)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.table.setFont(font)
        self.table.setStyleSheet("\n"
"background-color:  rgb(210, 210, 210)")
        self.table.setObjectName("table")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.table)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.table)
        font = QtGui.QFont()
        font.setPointSize(1)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QHeaderView::section {background-color: rgb(210, 210, 210);\n"
"border: 1px solid rgb(26, 61, 119);\n"
"font-size: 12pt;\n"
"font:bold;}\n"
"QTableView {\n"
"border: 2px solid rgb(26, 61, 119);\n"
"border-top:1px solid rgb(26, 61, 119);\n"
"}\n"
"")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setAutoScrollMargin(5)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(166)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(38)
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout.addWidget(self.table, 2, 0, 1, 1)
        self.FilterButton = QtWidgets.QWidget(membres)
        self.FilterButton.setStyleSheet("\n"
"background-color:  rgb(210, 210, 210)")
        self.FilterButton.setObjectName("FilterButton")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.FilterButton)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.filterdropdown = QtWidgets.QComboBox(self.FilterButton)
        self.filterdropdown.setMinimumSize(QtCore.QSize(250, 30))
        self.filterdropdown.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.filterdropdown.setFont(font)
        self.filterdropdown.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.filterdropdown.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(163, 163, 163);")
        self.filterdropdown.setEditable(False)
        self.filterdropdown.setObjectName("filterdropdown")
        self.filterdropdown.addItem("")
        self.filterdropdown.addItem("")
        self.filterdropdown.addItem("")
        self.filterdropdown.addItem("")
        self.horizontalLayout.addWidget(self.filterdropdown)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.recherche = QtWidgets.QLineEdit(self.FilterButton)
        self.recherche.setMinimumSize(QtCore.QSize(500, 30))
        self.recherche.setMaximumSize(QtCore.QSize(250, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.recherche.setFont(font)
        self.recherche.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.recherche.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"color: rgb(163, 163, 163);\n"
"border-radius:2px")
        self.recherche.setInputMask("")
        self.recherche.setDragEnabled(False)
        self.recherche.setReadOnly(False)
        self.recherche.setClearButtonEnabled(False)
        self.recherche.setObjectName("recherche")
        self.horizontalLayout.addWidget(self.recherche)
        self.pushButton = QtWidgets.QPushButton(self.FilterButton)
        self.pushButton.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(231, 231, 231);\n"
"border-radius:10px;\n"
"border:1px solid rgb(26, 61, 119);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/loupe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.femme = QtWidgets.QRadioButton(self.FilterButton)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.femme.setFont(font)
        self.femme.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.femme.setObjectName("femme")
        self.horizontalLayout.addWidget(self.femme)
        spacerItem3 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.homme = QtWidgets.QRadioButton(self.FilterButton)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.homme.setFont(font)
        self.homme.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.homme.setObjectName("homme")
        self.horizontalLayout.addWidget(self.homme)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.ajouter = QtWidgets.QPushButton(self.FilterButton)
        self.ajouter.setMinimumSize(QtCore.QSize(50, 50))
        self.ajouter.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.ajouter.setFont(font)
        self.ajouter.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ajouter.setStyleSheet("background-color: rgb(26, 61, 119);\n"
"border-radius:5px")
        self.ajouter.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/add (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ajouter.setIcon(icon1)
        self.ajouter.setIconSize(QtCore.QSize(35, 35))
        self.ajouter.setCheckable(True)
        self.ajouter.setObjectName("ajouter")
        self.horizontalLayout.addWidget(self.ajouter)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.supprimer = QtWidgets.QPushButton(self.FilterButton)
        self.supprimer.setMinimumSize(QtCore.QSize(50, 50))
        self.supprimer.setMaximumSize(QtCore.QSize(50, 50))
        self.supprimer.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.supprimer.setStyleSheet("background-color: rgb(26, 61, 119);\n"
"border-radius:5px;")
        self.supprimer.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/delete (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.supprimer.setIcon(icon2)
        self.supprimer.setIconSize(QtCore.QSize(35, 35))
        self.supprimer.setCheckable(True)
        self.supprimer.setObjectName("supprimer")
        self.horizontalLayout.addWidget(self.supprimer)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.modifier = QtWidgets.QPushButton(self.FilterButton)
        self.modifier.setMinimumSize(QtCore.QSize(50, 50))
        self.modifier.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.modifier.setFont(font)
        self.modifier.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.modifier.setStyleSheet("background-color: rgb(26, 61, 119);\n"
"border-radius:5px;")
        self.modifier.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/compose (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.modifier.setIcon(icon3)
        self.modifier.setIconSize(QtCore.QSize(35, 35))
        self.modifier.setCheckable(True)
        self.modifier.setObjectName("modifier")
        self.horizontalLayout.addWidget(self.modifier)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.gridLayout.addWidget(self.FilterButton, 1, 0, 1, 1)
        self.femme.clicked.connect(self.afficher_femmes)
        self.homme.clicked.connect(self.afficher_hommes)
        self.pushButton.clicked.connect(self.recherche_critere)
        self.supprimer.clicked.connect(self.supprimeradh)
        self.ajouter.clicked.connect(self.afficherAjouterMembre)
        self.modifier.clicked.connect(self.ouverture_page_modification)
        self.ajouter.clicked.connect(self.ouverture_page_ajout)
        self.retranslateUi(membres)
        QtCore.QMetaObject.connectSlotsByName(membres)
        self.tableWidget.setColumnWidth(0, 115)
        self.tableWidget.setColumnWidth(1, 340)
        self.tableWidget.setColumnWidth(2, 350)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 355)
        self.tableWidget.setColumnWidth(5, 350)
        self.tableWidget.setColumnWidth(6, 115)
        self.tableWidget.setColumnWidth(7, 115)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.afficher_tout()
        membres.showMaximized()

    def retranslateUi(self, membres):
        _translate = QtCore.QCoreApplication.translate
        membres.setWindowTitle(_translate("membres", "membre"))
        self.label.setText(_translate("membres", "GESTION DES MEMBRES"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("membres", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("membres", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("membres", "Prénom"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("membres", "Sexe"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("membres", "Date De Naissance"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("membres", "N° De Téléphone"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("membres", "Assuré(e)"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("membres", "Bané(e)"))
        self.filterdropdown.setItemText(0, _translate("membres", "choisir"))
        self.filterdropdown.setItemText(1, _translate("membres", "Nom"))
        self.filterdropdown.setItemText(2, _translate("membres", "Prénom"))
        self.filterdropdown.setItemText(3, _translate("membres", "ID"))
        self.recherche.setPlaceholderText("Rechercher")
        self.femme.setText(_translate("membres", "femme"))
        self.homme.setText(_translate("membres", "homme"))
        self.modifier.clicked.connect(self.afficherModifierMembre)

    def afficherAjouterMembre(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = UI_MainWindowAjouterMembre()
        self.ui.setupUi(self.window)
        self.window.show()
    def afficherModifierMembre(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowModifierMembre()
        self.ui.setupUi(self.window)
        self.window.show()

    def afficher_femmes(self):
        connection, cursor = connect_to_DB()
        sélectionné = self.femme.isChecked()
        if sélectionné:
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            query = "SELECT ID, nom, prénom, Gender, date_naissance, numéro_téléphone, Assuré, Bané FROM adhérant WHERE Gender = 'F'"
            cursor.execute(query)
            data = cursor.fetchall()
            row_count = self.tableWidget.rowCount()
            for row_number, row_data in enumerate(data, row_count):
                self.tableWidget.insertRow(row_number)
                for column_number, column_data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(column_data))
                    item.setFont(QtGui.QFont("Arial", 15))
                    self.tableWidget.setItem(row_number, column_number, item)
    def afficher_hommes(self):
        connection, cursor = connect_to_DB()
        sélectionné = self.homme.isChecked()
        if sélectionné:
            self.tableWidget.clearContents()
            self.tableWidget.setRowCount(0)
            query = "SELECT ID, nom, prénom, Gender, date_naissance, numéro_téléphone, Assuré, Bané FROM adhérant WHERE Gender = 'M'"
            cursor.execute(query)
            data = cursor.fetchall()
            row_count = self.tableWidget.rowCount()
            for row_number, row_data in enumerate(data, row_count):
                self.tableWidget.insertRow(row_number)
                for column_number, column_data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(column_data))
                    item.setFont(QtGui.QFont("Arial", 15))
                    self.tableWidget.setItem(row_number, column_number, item)

    def recherche_critere(self):
        connection, cursor = connect_to_DB()
        texte_recherche = self.recherche.text()
        critere_recherche = self.filterdropdown.currentText()
        if critere_recherche == "choisir":
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QtWidgets.QMessageBox.Warning)
            self.msg.setText("Veuillez choisir un critère de recherche.")
            self.msg.setWindowTitle("Erreur")
            self.msg.exec_()
            return
        if critere_recherche == "Nom":
            query = "SELECT ID, nom, prénom, Gender, date_naissance, numéro_téléphone, Assuré, Bané FROM adhérant WHERE nom LIKE %s"
        elif critere_recherche == "Prénom":
            query = "SELECT ID, nom, prénom, Gender, date_naissance, numéro_téléphone, Assuré, Bané FROM adhérant WHERE prénom LIKE %s"
        elif critere_recherche == "ID":
            query = "SELECT ID, nom, prénom, Gender, date_naissance, numéro_téléphone, Assuré, Bané FROM adhérant WHERE ID LIKE %s"

        texte_recherche_avec_joker = f"%{texte_recherche}%"
        cursor.execute(query, (texte_recherche_avec_joker,))
        data = cursor.fetchall()
        if not data:
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QtWidgets.QMessageBox.Information)
            self.msg.setText("Aucun membre n'existe avec ce critère de recherche.")
            self.msg.setWindowTitle("Erreur")
            self.msg.exec_()
            return
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        for numero_ligne, donnees_ligne in enumerate(data):
            self.tableWidget.insertRow(numero_ligne)
            for numero_colonne, donnee_colonne in enumerate(donnees_ligne):
                item = QtWidgets.QTableWidgetItem(str(donnee_colonne))
                item.setFont(QtGui.QFont("Arial", 15))
                self.tableWidget.setItem(numero_ligne, numero_colonne, item)
    def afficher_tout(self):
        connection, cursor = connect_to_DB()
        query = "SELECT ID, nom, prénom, Gender, date_naissance, numéro_téléphone, Assuré, Bané FROM adhérant"
        cursor.execute(query)
        data = cursor.fetchall()
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)
        for numero_ligne, donnees_ligne in enumerate(data):
            self.tableWidget.insertRow(numero_ligne)
            for numero_colonne, donnee_colonne in enumerate(donnees_ligne):
                item = QtWidgets.QTableWidgetItem(str(donnee_colonne))
                item.setFont(QtGui.QFont("Arial", 15))
                self.tableWidget.setItem(numero_ligne, numero_colonne, item)

    def supprimeradh(self):
        connection, cursor = connect_to_DB()
        critere_id = self.filterdropdown.currentText()
        supp_id = self.recherche.text()
        if critere_id == "ID":
            query = "DELETE FROM adhérant WHERE ID = %s"
            cursor.execute(query, (supp_id,))
            connection.commit()
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QtWidgets.QMessageBox.Information)
            self.msg.setText("Votre adhérent a été supprimé avec succès")
            self.msg.setWindowTitle("Suppression avec succès")
            self.msg.setWindowIcon(QtGui.QIcon("../resourcesGenerales/iconGC.png"))
            self.msg.exec_()
            self.afficher_tout()
        else:
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QtWidgets.QMessageBox.Information)
            self.msg.setWindowIcon(QtGui.QIcon("../resourcesGenerales/iconGC.png"))
            self.msg.setText("Veuillez supprimer un adhérent par son ID uniquement.")
            self.msg.setWindowTitle("Erreur")
            self.msg.exec_()

    def ouverture_page_modification(self):
        connection, cursor = connect_to_DB()
        texte_recherche = self.recherche.text()
        # Connexion à la base de données MySQL
        query = "SELECT * FROM  adhérant WHERE ID = %s"
        cursor.execute(query, (texte_recherche,))
        resultats = cursor.fetchone()
        if resultats:
            infos = [f"{champ}: {valeur}" for champ, valeur in zip(cursor.column_names, resultats)]
            self.deuxieme_fenetre = self.fenetre_modification(infos, texte_recherche)
            self.deuxieme_fenetre.show()
        else:
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QtWidgets.QMessageBox.Information)
            self.msg.setText("Aucun adhérent n'existe avec cet ID. Veuillez réessayer.")
            self.msg.setWindowIcon(QtGui.QIcon("../resourcesGenerales/iconGC.png"))
            self.msg.setWindowTitle("Erreur")
            self.msg.exec_()

    def ouverture_page_ajout(self):
        connection, cursor = connect_to_DB()
        texte_recherche = self.recherche.text()
        query = "SELECT * FROM adhérant WHERE ID = %s"
        value = (texte_recherche,)
        cursor.execute(query, value)
        resultats = cursor.fetchall()
        if resultats:
            self.deuxieme_fenetre = self.DeuxiemeFenetre(texte_recherche)
            self.deuxieme_fenetre.show()
        else:
            print("erreur le resultat n'existe pas")

    class fenetre_modification(QMainWindow):
        connection, cursor = connect_to_DB()
        def __init__(self, infos, texte_recherche):
            super().__init__()
            self.texte_recherche = texte_recherche
            self.setWindowTitle("Informations de l'adhérent")
            self.setGeometry(200, 200, 400, 300)
            self.labels_infos = []
            for i, info in enumerate(infos):
                label = QTextEdit(info, self)
                label.setGeometry(50, 30 + i * 30, 300, 30)
                self.labels_infos.append(label)

            self.button_enregistrer = QPushButton("Enregistrer les modifications", self)
            self.button_enregistrer.setGeometry(100, 200, 200, 30)
            self.button_enregistrer.clicked.connect(self.enregistrer_modifications)

        def enregistrer_modifications(self):
            connection, cursor = connect_to_DB()
            try:
                # extraction des informations
                for label in self.labels_infos:
                    champ, valeur = label.toPlainText().split(":")
                    champ = champ.strip()  # Supprimer les espaces autour du nom du champ
                    valeur = valeur.strip()  # Supprimer les espaces autour de la valeur

                    # Requête SQL pour mettre à jour les données dans la base de données
                    query = f"UPDATE adhérant SET {champ} = %s WHERE ID = %s"
                    cursor.execute(query, (valeur, self.texte_recherche))  # Utilisation de self.value

                connection.commit()

                QMessageBox.information(self, "Information", "Modifications enregistrées avec succès.")

            except mysql.connector.Error as error:
                connection.rollback()
                QMessageBox.critical(self, "Erreur", f"Erreur lors de l'enregistrement des modifications : {error}")

            finally:
                cursor.close()
    class DeuxiemeFenetre(QMainWindow):
            def __init__(self, texte_recherche):
                super().__init__()
                self.setWindowTitle("Deuxième Fenêtre")
                self.setGeometry(800, 300, 350, 300)

                self.texte_recherche = texte_recherche

                self.button_ajouter = QPushButton("Ajouter", self)
                self.button_ajouter.setGeometry(150, 200, 100, 30)
                self.button_ajouter.clicked.connect(self.ajout)

                self.label_mois = QLabel("date de début:", self)
                self.label_mois.setGeometry(50, 20, 150, 30)

                self.label_mois2 = QLabel("date de la fin:", self)
                self.label_mois2.setGeometry(50, 50, 150, 30)

                self.label_id = QLabel("ID:", self)
                self.label_id.setGeometry(50, 80, 50, 30)

                self.current_id = QLineEdit(self)
                self.current_id.setGeometry(100, 80, 200, 30)
                self.current_id.setText(texte_recherche)

                self.label_abonnement = QLabel("Abonnement:", self)
                self.label_abonnement.setGeometry(50, 120, 100, 30)

                self.label_prix = QLabel("Prix:", self)
                self.label_prix.setGeometry(50, 155, 100, 30)

                self.current_prix = QLineEdit(self)
                self.current_prix.setGeometry(150, 155, 150, 30)

                self.combobox_abonnement = QComboBox(self)
                self.combobox_abonnement.setGeometry(150, 120, 150, 30)
                self.combobox_abonnement.addItem("karate garcon")
                self.combobox_abonnement.addItem("karate fille")
                self.combobox_abonnement.addItem("kick -16")
                self.combobox_abonnement.addItem("kick +16")
                self.combobox_abonnement.addItem("fitness N-Edd")
                self.combobox_abonnement.addItem("Fitness femme")
                self.combobox_abonnement.addItem("fitness hit")
                self.combobox_abonnement.addItem("kick walid")
                self.combobox_abonnement.addItem("self defense")

                # Ajout des mois de l'année

                date_debut = datetime.now().strftime("%Y-%m-%d")
                date_fin = datetime.now() + timedelta(days=30)
                self.textedit_datedefin = QTextEdit(self)
                self.textedit_datedefin.setGeometry(155, 50, 150, 30)
                self.textedit_datedefin.setPlainText(date_fin.strftime("%Y-%m-%d"))

                self.textedit_datedebut = QTextEdit(self)
                self.textedit_datedebut.setGeometry(155, 20, 150, 30)
                self.textedit_datedebut.setPlainText(date_debut)

            def ajout(self):
                connection, cursor = connect_to_DB()
                type_abonnement = self.combobox_abonnement.currentText()
                debut_abonnement = self.textedit_datedebut.toPlainText()
                fin_abonnement = self.textedit_datedefin.toPlainText()
                id_abonnement = self.current_id.text()
                prix = self.current_prix.text()

                mois = datetime.now().month

                def definition_mois(mois_actuelle):
                    switcher = {
                        1: "janvier",
                        2: "février",
                        3: "mars",
                        4: "avril",
                        5: "mai",
                        6: "juin",
                        7: "juillet",
                        9: "septembre",
                        10: "octobre",
                        11: "novembre",
                        12: "décembre",
                    }
                    mois_adhérant = switcher.get(mois_actuelle, "Cas par défaut")
                    return mois_adhérant

                mois_adhérant = definition_mois(mois)

                try:
                    query = "INSERT INTO abonnement (type_abonnement, id_abonnement,date_debut,date_fin,prix ) VALUES (%s, %s, %s,%s,%s)"
                    values = (type_abonnement, id_abonnement, debut_abonnement, fin_abonnement, prix)
                    cursor.execute(query, values)

                    connection.commit()

                    query = f"UPDATE adhérant SET {mois_adhérant} = true WHERE ID = {id_abonnement}"

                    cursor.execute(query)
                    connection.commit()

                    print("Ajout avec succès")

                except mysql.connector.Error as error:
                    print("Erreur lors de l'ajout:", error)


from lesMembres import membres_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    membres = QtWidgets.QWidget()
    ui = Ui_membres()
    ui.setupUi(membres)
    membres.show()
    sys.exit(app.exec_())