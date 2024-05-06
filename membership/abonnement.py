from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime, timedelta
from connexion_DB import connect_to_DB
from addAbonnement.ajouterabonnement import Ui_ajouterAbonnement



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
        self.window = QtWidgets.QWidget()  # Créer la nouvelle fenêtre
        self.ui = Ui_ajouterAbonnement()  # Instancier l'interface utilisateur
        self.ui.setupUi(self.window)
        self.window.show()



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
        item.setText(_translate("abonnement", "Date Fin"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("abonnement", "Date De Début"))

        self.filterdropdown.setItemText(0, _translate("abonnement", "choisir"))
        self.filterdropdown.setItemText(1, _translate("abonnement", "Nom"))
        self.filterdropdown.setItemText(2, _translate("abonnement", "Prénom"))
        self.filterdropdown.setItemText(3, _translate("abonnement", "ID Abonnement"))
        self.filterdropdown.setItemText(4, _translate("abonnement", "Sport"))
        self.recherche.setText(_translate("abonnement", "rechercher"))

    def supprimeradh(self):
        connection, cursor = connect_to_DB()
        critere_id = self.filterdropdown.currentText()
        supp_id = self.recherche.text()

        if critere_id == "ID Abonnement":
            query = "select * from abonnement where ID_abonnement = %s"
            cursor.execute(query, (supp_id,))
            existence = cursor.fetchone()
            if existence:
                query = "DELETE FROM abonnement WHERE ID_abonnement = %s"
                cursor.execute(query, (supp_id,))
                connection.commit()  # Validez la transaction dans la base de données
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
        connection.close()

    def afficher_tout(self):
        connection, cursor = connect_to_DB()

        query = "SELECT ID_abonnement,adhérant.ID,nom,prénom,sport,prix,date_fin,date_début FROM adhérant JOIN abonnement ON adhérant.ID = abonnement.ID_adhérant JOIN offre ON abonnement.ID_offre = offre.ID_offre"
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
        connection, cursor = connect_to_DB()

        critere_rech = self.filterdropdown.currentText()
        texte_rech = self.recherche.text()
        try:
            try:
                if critere_rech == "ID Abonnement":
                    query = "SELECT ID_abonnement,adhérant.ID,nom,prénom,sport,prix,date_fin,date_début FROM adhérant JOIN abonnement ON adhérant.ID = abonnement.ID_adhérant JOIN offre ON abonnement.ID_offre = offre.ID_offre where ID_abonnement = %s"
                    cursor.execute(query, (texte_rech,))
                elif critere_rech == "Nom":
                    query = "SELECT ID_abonnement,adhérant.ID,nom,prénom,sport,prix,date_fin,date_début FROM adhérant JOIN abonnement ON adhérant.ID = abonnement.ID_adhérant JOIN offre ON abonnement.ID_offre = offre.ID_offre where nom = %s"
                    cursor.execute(query, (texte_rech,))
                elif critere_rech == "Prénom":
                    query = "SELECT ID_abonnement,adhérant.ID,nom,prénom,sport,prix,date_fin,date_début FROM adhérant JOIN abonnement ON adhérant.ID = abonnement.ID_adhérant JOIN offre ON abonnement.ID_offre = offre.ID_offre where prénom = %s"
                    cursor.execute(query, (texte_rech,))
                elif critere_rech == "Sport":
                    query = "SELECT ID_abonnement,adhérant.ID,nom,prénom,sport,prix,date_fin,date_début FROM adhérant JOIN abonnement ON adhérant.ID = abonnement.ID_adhérant JOIN offre ON abonnement.ID_offre = offre.ID_offre where sport = %s"
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    abonnement = QtWidgets.QWidget()
    ui = Ui_abonnement()
    ui.setupUi(abonnement)
    abonnement.show()
    sys.exit(app.exec_())