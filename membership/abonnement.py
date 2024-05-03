from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime, timedelta
import mysql.connector


class Ui_abonnement(object):
    def setupUi(self, abonnement):

        abonnement.setObjectName("abonnement")
        abonnement.resize(1174, 573)
        abonnement.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        abonnement.setStyleSheet("background-color: rgb(210, 210, 210);")
        self.gridLayout = QtWidgets.QGridLayout(abonnement)
        self.gridLayout.setObjectName("gridLayout")
        self.topheader = QtWidgets.QWidget(abonnement)
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
        self.table = QtWidgets.QWidget(abonnement)
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
        self.tableWidget.setColumnCount(9)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(38)
        self.verticalLayout.addWidget(self.tableWidget)
        self.gridLayout.addWidget(self.table, 2, 0, 1, 1)
        self.FilterButton = QtWidgets.QWidget(abonnement)
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

                                     "border-radius:2px")
        self.recherche.setInputMask("")
        self.recherche.setDragEnabled(False)
        self.recherche.setReadOnly(False)
        self.recherche.setClearButtonEnabled(True)
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
        spacerItem2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
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
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
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
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
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
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.gridLayout.addWidget(self.FilterButton, 1, 0, 1, 1)
        self.ajouter.clicked.connect(self.ouverture_page_ajout)

        self.retranslateUi(abonnement)
        QtCore.QMetaObject.connectSlotsByName(abonnement)
        self.supprimer.clicked.connect(self.supprimeradh)
        self.afficher_tout()
        self.pushButton.clicked.connect(self.rechercher)

    def ouverture_page_ajout(self):
        self.ui1 = Ui_ajouterAbonnement()
        self.ui1.ouverture_page_ajout()

    def retranslateUi(self, abonnement):
        _translate = QtCore.QCoreApplication.translate
        abonnement.setWindowTitle(_translate("abonnement", "abonnement"))
        self.label.setText(_translate("abonnement", "GESTION DES ABONNEMENTS"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("abonnement", "ID Abonnement"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("abonnement", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("abonnement", "Nom"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("abonnement", "Prénom"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("abonnement", "Sport"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("abonnement", "Prix"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("abonnement", "Durée"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("abonnement", "Date De Début"))

        self.filterdropdown.setItemText(0, _translate("abonnement", "choisir"))
        self.filterdropdown.setItemText(1, _translate("abonnement", "Nom"))
        self.filterdropdown.setItemText(2, _translate("abonnement", "Prénom"))
        self.filterdropdown.setItemText(3, _translate("abonnement", "ID Abonnement"))
        self.filterdropdown.setItemText(4, _translate("abonnement", "Sport"))
        self.recherche.setText(_translate("abonnement", "rechercher"))

    def supprimeradh(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2608004",
            database="sqltest1"
        )

        cursor = conn.cursor()
        critere_id = self.filterdropdown.currentText()
        supp_id = self.recherche.text()

        if critere_id == "ID Abonnement":
            query = "select * from abonnement where id_abonnement = %s"
            cursor.execute(query, (supp_id,))
            existence = cursor.fetchone()
            if existence:
                query = "DELETE FROM abonnement WHERE id_abonnement = %s"
                cursor.execute(query, (supp_id,))
                conn.commit()  # Validez la transaction dans la base de données
                self.msg2 = QtWidgets.QMessageBox()
                self.msg2.setIcon(QtWidgets.QMessageBox.Information)
                self.msg2.setText("votre abonnement a été supprimé avec succes")
                self.msg2.exec_()
            else:
                self.msg3 = QtWidgets.QMessageBox()
                self.msg3.setIcon(QtWidgets.QMessageBox.Information)
                self.msg3.setText("Attention l'abonnement saisi n'existe pas ")
                self.msg3.exec_()
        else:
            self.msg = QtWidgets.QMessageBox()
            self.msg.setIcon(QtWidgets.QMessageBox.Information)
            self.msg.setText("Il faut supprimer un abonnement à partir de son ID seulement")
            self.msg.setWindowTitle("Erreur")
            self.msg.exec_()

        # Fermez le curseur et la connexion à la base de données
        cursor.close()
        conn.close()

    def afficher_tout(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2608004",
            database="sqltest1"
        )

        cursor = conn.cursor()

        query = "SELECT id_abonnement,adhérant.id,nom,prenom,sport,prix,date_fin,date_debut FROM adhérant JOIN abonnement ON adhérant.id = abonnement.id JOIN offres ON abonnement.id_offre = offres.id;"
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

    def rechercher(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2608004",
            database="sqltest1"
        )

        cursor = conn.cursor()

        critere_rech = self.filterdropdown.currentText()
        texte_rech = self.recherche.text()
        try:
            try:
                if critere_rech == "ID Abonnement":
                    query = "SELECT id_abonnement,adhérant.id,nom,prenom,sport,prix,date_fin,date_debut FROM adhérant JOIN abonnement ON adhérant.id = abonnement.id JOIN offres ON abonnement.id_offre = offres.id where id_abonnement = %s;"
                    cursor.execute(query, (texte_rech,))
                elif critere_rech == "Nom":
                    query = "SELECT id_abonnement,adhérant.id,nom,prenom,sport,prix,date_fin,date_debut FROM adhérant JOIN abonnement ON adhérant.id = abonnement.id JOIN offres ON abonnement.id_offre = offres.id where nom = %s;"
                    cursor.execute(query, (texte_rech,))
                elif critere_rech == "Prénom":
                    query = "SELECT id_abonnement,adhérant.id,nom,prenom,sport,prix,date_fin,date_debut FROM adhérant JOIN abonnement ON adhérant.id = abonnement.id JOIN offres ON abonnement.id_offre = offres.id where prenom = %s;"
                    cursor.execute(query, (texte_rech,))
                elif critere_rech == "Sport":
                    query = "SELECT id_abonnement,adhérant.id,nom,prenom,sport,prix,date_fin,date_debut FROM adhérant JOIN abonnement ON adhérant.id = abonnement.id JOIN offres ON abonnement.id_offre = offres.id where sport = %s;"
                    cursor.execute(query, (texte_rech,))

            finally:
                data = cursor.fetchall()
                self.tableWidget.clearContents()
                self.tableWidget.setRowCount(0)
                for numero_ligne, donnees_ligne in enumerate(data):
                    self.tableWidget.insertRow(numero_ligne)
                    for numero_colonne, donnee_colonne in enumerate(donnees_ligne):
                        item = QtWidgets.QTableWidgetItem(str(donnee_colonne))
                        item.setFont(QtGui.QFont("Arial", 15))
                        self.tableWidget.setItem(numero_ligne, numero_colonne, item)

        except Exception:

            self.msg2 = QtWidgets.QMessageBox()
            self.msg2.setIcon(QtWidgets.QMessageBox.Information)
            self.msg2.setWindowTitle("erreur")
            self.msg2.setText("Attention : veuillez saisir un critere de recherche")
            self.msg2.exec_()


import abonnement_rc


class Ui_ajouterAbonnement(object):
    def setupUi(self, ajouterAbonnement):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2608004",
            database="sqltest1"
        )

        # Création d'un curseur
        cursor = conn.cursor()
        ajouterAbonnement.setObjectName("ajouterAbonnement")
        ajouterAbonnement.resize(926, 570)
        ajouterAbonnement.setStyleSheet("background-color: rgb(219, 219, 219);")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(ajouterAbonnement)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(ajouterAbonnement)
        self.widget.setStyleSheet("background-color: rgb(219, 219, 219);")
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(26, 61, 119);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_6 = QtWidgets.QWidget(self.widget_2)
        self.widget_6.setMinimumSize(QtCore.QSize(500, 20))
        self.widget_6.setSizeIncrement(QtCore.QSize(0, 0))
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget_6)
        self.label_2.setMinimumSize(QtCore.QSize(50, 50))
        self.label_2.setMaximumSize(QtCore.QSize(50, 50))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/add.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.Nom = QtWidgets.QLabel(self.widget_6)
        self.Nom.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Nom.setFont(font)
        self.Nom.setStyleSheet("color: rgb(26, 61, 119);")
        self.Nom.setObjectName("Nom")
        self.verticalLayout_4.addWidget(self.Nom)
        self.lineEditNom = QtWidgets.QLineEdit(self.widget_6)
        self.lineEditNom.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEditNom.setSizeIncrement(QtCore.QSize(0, 0))

        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(13)
        self.lineEditNom.setFont(font)
        self.lineEditNom.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditNom.setObjectName("lineEditNom")
        self.verticalLayout_4.addWidget(self.lineEditNom)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Prenom = QtWidgets.QLabel(self.widget_6)
        self.Prenom.setMinimumSize(QtCore.QSize(0, 35))
        self.Prenom.setFont(font)
        self.Prenom.setStyleSheet("color: rgb(26, 61, 119);")
        self.Prenom.setObjectName("Prenom")
        self.verticalLayout_4.addWidget(self.Prenom)
        self.lineEditPrenom = QtWidgets.QLineEdit(self.widget_6)
        self.lineEditPrenom.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEditPrenom.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(13)
        self.lineEditPrenom.setFont(font)
        self.lineEditPrenom.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditPrenom.setObjectName("lineEditPrenom")
        self.verticalLayout_4.addWidget(self.lineEditPrenom)

        self.sport = QtWidgets.QLabel(self.widget_6)
        self.sport.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.sport.setFont(font)
        self.sport.setStyleSheet("color: rgb(26, 61, 119);")
        self.sport.setObjectName("sport")
        self.verticalLayout_4.addWidget(self.sport)
        self.dropdownSport = QtWidgets.QComboBox(self.widget_6)
        self.dropdownSport.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(13)
        self.dropdownSport.setFont(font)
        self.dropdownSport.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "color: rgb(83, 83, 83);")
        self.dropdownSport.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.dropdownSport.setObjectName("dropdownSport")
        self.dropdownSport.addItem("")
        self.verticalLayout_4.addWidget(self.dropdownSport)
        self.DateDebut = QtWidgets.QLabel(self.widget_6)
        self.DateDebut.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.DateDebut.setFont(font)
        self.DateDebut.setStyleSheet("color: rgb(26, 61, 119);")
        self.DateDebut.setObjectName("DateDebut")
        self.verticalLayout_4.addWidget(self.DateDebut)
        self.lineEditDateDebut = QtWidgets.QLineEdit(self.widget_6)
        self.lineEditDateDebut.setMinimumSize(QtCore.QSize(0, 35))
        self.lineEditDateDebut.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(13)
        self.lineEditDateDebut.setFont(font)
        self.lineEditDateDebut.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditDateDebut.setObjectName("lineEditDateDebut")
        self.verticalLayout_4.addWidget(self.lineEditDateDebut)
        self.DateFin = QtWidgets.QLabel(self.widget_6)
        self.DateFin.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.DateFin.setFont(font)
        self.DateFin.setStyleSheet("color: rgb(26, 61, 119);")
        self.DateFin.setObjectName("DateFin")
        self.verticalLayout_4.addWidget(self.DateFin)
        self.lineEditDateFin = QtWidgets.QLineEdit(self.widget_6)
        self.lineEditDateFin.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(13)
        self.lineEditDateFin.setFont(font)
        self.lineEditDateFin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditDateFin.setObjectName("lineEditDateFin")
        self.verticalLayout_4.addWidget(self.lineEditDateFin)
        self.Offre = QtWidgets.QLabel(self.widget_6)
        self.Offre.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.Offre.setFont(font)
        self.Offre.setStyleSheet("color: rgb(26, 61, 119);")
        self.Offre.setObjectName("Offre")
        self.verticalLayout_4.addWidget(self.Offre)
        self.dropdownOffre = QtWidgets.QComboBox(self.widget_6)
        self.dropdownOffre.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(13)
        self.dropdownOffre.setFont(font)
        self.dropdownOffre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                         "color : rgb(83, 83, 83);")
        self.dropdownOffre.setObjectName("dropdownOffre")
        self.dropdownOffre.addItem("")
        self.verticalLayout_4.addWidget(self.dropdownOffre)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButtonSave = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonSave.setMinimumSize(QtCore.QSize(200, 40))
        self.pushButtonSave.setMaximumSize(QtCore.QSize(200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonSave.setFont(font)
        self.pushButtonSave.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonSave.setStyleSheet("background-color: rgb(38, 255, 0);\n"
                                          "color: rgb(252, 252, 252);\n"
                                          "border-radius:5px;\n"
                                          "")
        self.pushButtonSave.setCheckable(True)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout_3.addWidget(self.pushButtonSave)
        self.pushButtonAnnuler = QtWidgets.QPushButton(self.widget_6)
        self.pushButtonAnnuler.setMinimumSize(QtCore.QSize(200, 40))
        self.pushButtonAnnuler.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonAnnuler.setFont(font)
        self.pushButtonAnnuler.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonAnnuler.setStyleSheet("background-color: rgb(255, 93, 93);\n"
                                             "border-radius:5px;\n"
                                             "color: rgb(252, 252, 252);")
        self.pushButtonAnnuler.setCheckable(True)
        self.pushButtonAnnuler.setObjectName("pushButtonAnnuler")
        self.horizontalLayout_3.addWidget(self.pushButtonAnnuler)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.widget_6)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 8)
        self.horizontalLayout_2.addWidget(self.widget)

        self.retranslateUi(ajouterAbonnement)
        QtCore.QMetaObject.connectSlotsByName(ajouterAbonnement)

        query = "SELECT prix FROM offres WHERE sport = %s"
        sport1 = self.dropdownSport.currentText()
        cursor.execute(query, (sport1,))
        result = cursor.fetchone()
        prix_offre = result[0]
        self.dropdownOffre.addItem(str(prix_offre))

        date_debut = datetime.now().strftime("%Y-%m-%d")  ##########
        date_fin = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
        self.lineEditDateDebut.setText(date_debut)
        self.lineEditDateFin.setText(date_fin)  ##############
        self.dropdownSport.currentTextChanged.connect(self.updateCombo2)
        self.pushButtonSave.clicked.connect(self.ajout)

    def retranslateUi(self, ajouterAbonnement):
        _translate = QtCore.QCoreApplication.translate
        ajouterAbonnement.setWindowTitle(_translate("ajouterAbonnement", "ajouterAbonnement"))
        self.label.setText(_translate("ajouterAbonnement", "Ajouter un Abonnement"))
        self.Nom.setText(_translate("ajouterAbonnement", "Nom"))
        self.lineEditNom.setPlaceholderText(_translate("ajouterAbonnement", " Nom"))
        self.Prenom.setText(_translate("ajouterAbonnement", "Prenom"))
        self.lineEditPrenom.setPlaceholderText(_translate("ajouterAbonnement", " Prenom"))
        self.sport.setText(_translate("ajouterAbonnement", "Sport"))
        self.dropdownSport.addItem("karate fille")
        self.dropdownSport.addItem("kick -16")
        self.dropdownSport.addItem("kick +16")
        self.dropdownSport.addItem("fitness N-Edd")
        self.dropdownSport.addItem("Fitness femme")
        self.dropdownSport.addItem("fitness hit")
        self.dropdownSport.addItem("kick walid")
        self.dropdownSport.addItem("self defense")
        self.dropdownSport.setItemText(0, _translate("ajouterAbonnement", "karate garcon"))
        self.DateDebut.setText(_translate("ajouterAbonnement", "Date de début"))

        self.DateFin.setText(_translate("ajouterAbonnement", "Date de fin"))
        self.Offre.setText(_translate("ajouterAbonnement", "prix"))
        self.pushButtonSave.setText(_translate("ajouterAbonnement", "Enregistrer"))
        self.pushButtonAnnuler.setText(_translate("ajouterAbonnement", "Annuler"))

    def ouverture_page_ajout(self):  #######
        self.ui1 = Ui_ajouterAbonnement()  #######
        self.ajouterAbonnement = QtWidgets.QWidget()  ########
        self.ui1.setupUi(self.ajouterAbonnement)  #########
        self.ajouterAbonnement.show()  ########

    def updateCombo2(self):
        # Effacer les anciennes valeurs de la deuxième QComboBox
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2608004",
            database="sqltest1"
        )

        cursor = conn.cursor()
        self.dropdownOffre.clear()

        selected_value = self.dropdownSport.currentText()

        query = "SELECT prix FROM offres WHERE sport = %s"
        cursor.execute(query, (selected_value,))
        values = cursor.fetchall()

        for value in values:
            self.dropdownOffre.addItem(str(value[0]))

    def ajout(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2608004",
            database="sqltest1"
        )

        cursor = conn.cursor()

        Nom_adhérant = self.lineEditNom.text()
        Prenom_adhérant = self.lineEditPrenom.text()

        debut_abonnement = self.lineEditDateDebut.text()
        fin_abonnement = self.lineEditDateFin.text()

        cursor.execute("select id from adhérant where nom = %s and prenom = %s", (Nom_adhérant, Prenom_adhérant))
        result = cursor.fetchone()  # Récupère la première ligne de résultat
        if result:
            id_adhérant = result[0]
            selected_value = self.dropdownSport.currentText()
            query = "SELECT id FROM offres WHERE sport = %s"
            cursor.execute(query, (selected_value,))
            current_offre = cursor.fetchone()

            if current_offre:
                current_offre_id = current_offre[0]

                query_insert = "INSERT INTO abonnement (id_offre, id, date_debut, date_fin) VALUES (%s, %s, %s, %s)"
                values = (current_offre_id, id_adhérant, debut_abonnement, fin_abonnement)

                try:
                    cursor.execute(query_insert, values)
                    conn.commit()
                    self.msg2 = QtWidgets.QMessageBox()
                    self.msg2.setIcon(QtWidgets.QMessageBox.Information)
                    self.msg2.setWindowTitle("Attention !")
                    self.msg2.setText("votre abonnement a été sajouté avec succes")
                    self.msg2.exec_()
                except mysql.connector.Error as err:
                    self.msg2 = QtWidgets.QMessageBox()
                    self.msg2.setWindowTitle("Attention !")
                    self.msg2.setIcon(QtWidgets.QMessageBox.Information)
                    self.msg2.setText("erreur lors de l'insertion des données")
                    self.msg2.exec_()
            else:
                self.msg2 = QtWidgets.QMessageBox()
                self.msg2.setWindowTitle("Attention !")
                self.msg2.setIcon(QtWidgets.QMessageBox.Information)
                self.msg2.setText("Aucune offre n'est sélectionné")
                self.msg2.exec_()
        else:
            self.msg2 = QtWidgets.QMessageBox()
            self.msg2.setIcon(QtWidgets.QMessageBox.Information)
            self.msg2.setWindowTitle("Attention !")
            self.msg2.setText("Aucun adhérant trouvé avec ce nom et prénom")
            self.msg2.exec_()

        # Fermez le curseur et la connexion à la base de données
        cursor.close()
        conn.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    abonnement = QtWidgets.QWidget()
    ui = Ui_abonnement()
    ui.setupUi(abonnement)
    abonnement.show()
    sys.exit(app.exec_())