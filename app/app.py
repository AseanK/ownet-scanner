from PyQt5 import QtCore, QtGui, QtWidgets
import json
import lookup
import deauth

class Ui_MainWindow(object):
    def __init__(self):
        self.data = []

        self.all = True
        self.company = False
        self.address = False
        self.ip = False
        self.mac = False
        self.selected_cell = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1200, 810)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # LOGO
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(350, -150, 500, 500))
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("./static/wifi-logo.png"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")

        # Data Label
        self.dataLabel = QtWidgets.QLabel(self.centralwidget)
        self.dataLabel.setGeometry(QtCore.QRect(220, 150, 100, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataLabel.sizePolicy().hasHeightForWidth())
        self.dataLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(18)
        self.dataLabel.setFont(font)
        self.dataLabel.setObjectName("dataLabel")
        
        # All Check-box
        self.allCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.allCheckBox.setGeometry(QtCore.QRect(220, 230, 180, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allCheckBox.sizePolicy().hasHeightForWidth())
        self.allCheckBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(12)
        self.allCheckBox.setFont(font)
        self.allCheckBox.setObjectName("allCheckBox")
        self.allCheckBox.setChecked(True)

        # Company Check-box
        self.companyCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.companyCheckBox.setGeometry(QtCore.QRect(220, 270, 180, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.companyCheckBox.sizePolicy().hasHeightForWidth())
        self.companyCheckBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(12)
        self.companyCheckBox.setFont(font)
        self.companyCheckBox.setObjectName("companyCheckBox")

        # Address Check-box
        self.addressCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.addressCheckBox.setGeometry(QtCore.QRect(220, 310, 180, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addressCheckBox.sizePolicy().hasHeightForWidth())
        self.addressCheckBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(12)
        self.addressCheckBox.setFont(font)
        self.addressCheckBox.setObjectName("addressCheckBox")
        
        # IP Check-box
        self.ipCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.ipCheckBox.setGeometry(QtCore.QRect(220, 350, 180, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ipCheckBox.sizePolicy().hasHeightForWidth())
        self.ipCheckBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(12)
        self.ipCheckBox.setFont(font)
        self.ipCheckBox.setObjectName("ipCheckBox")

        # MAC Check-box
        self.macCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.macCheckBox.setGeometry(QtCore.QRect(220, 390, 180, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.macCheckBox.sizePolicy().hasHeightForWidth())
        self.macCheckBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(12)
        self.macCheckBox.setFont(font)
        self.macCheckBox.setObjectName("macCheckBox")

        # IP Label
        self.ipLabel = QtWidgets.QLabel(self.centralwidget)
        self.ipLabel.setGeometry(QtCore.QRect(880, 150, 200, 80))
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(18)
        self.ipLabel.setFont(font)
        self.ipLabel.setObjectName("ipLabel")

        # IP Input
        self.ipInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ipInput.setGeometry(QtCore.QRect(880, 230, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(12)
        self.ipInput.setFont(font)
        self.ipInput.setObjectName("ipInput")

        # Get IP Button
        self.getButton = QtWidgets.QPushButton(self.centralwidget)
        self.getButton.setGeometry(QtCore.QRect(980, 260, 100, 35))
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(12)
        self.getButton.setFont(font)
        self.getButton.setObjectName("getButton")

        # Start Button
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(520, 380, 130, 50))
        font = QtGui.QFont()
        font.setFamily("Leelawadee")
        font.setPointSize(18)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")

        # Table window
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 440, 1200, 310))
        self.tableWidget.setObjectName("tableWidget")

        # Menu bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionAbout_us = QtWidgets.QAction(MainWindow)
        self.actionAbout_us.setObjectName("actionAbout_us")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuAbout.addAction(self.actionAbout_us)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        # Button on click
        self.getButton.clicked.connect(self.get_ip)
        self.startButton.clicked.connect(self.clicked)
        self.actionSave.triggered.connect(self.save)
        self.actionOpen.triggered.connect(self.open)
        self.actionNew.triggered.connect(self.new)
        self.actionAbout_us.triggered.connect(self.show_info)

        # Data field check
        self.allCheckBox.stateChanged.connect(lambda:self.check_box_state(self.allCheckBox))
        self.companyCheckBox.stateChanged.connect(lambda:self.check_box_state(self.companyCheckBox))
        self.addressCheckBox.stateChanged.connect(lambda:self.check_box_state(self.addressCheckBox))
        self.ipCheckBox.stateChanged.connect(lambda:self.check_box_state(self.ipCheckBox))
        self.macCheckBox.stateChanged.connect(lambda:self.check_box_state(self.macCheckBox))

        # Cell on click
        self.tableWidget.cellClicked.connect(self.clicked_cell)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Text and Short-cuts
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ownet Scanner"))
        self.dataLabel.setText(_translate("MainWindow", "Data"))
        self.allCheckBox.setText(_translate("MainWindow", "All"))
        self.companyCheckBox.setText(_translate("MainWindow", "Company"))
        self.addressCheckBox.setText(_translate("MainWindow", "Address"))
        self.ipCheckBox.setText(_translate("MainWindow", "IP address"))
        self.macCheckBox.setText(_translate("MainWindow", "MAC address"))
        self.ipLabel.setText(_translate("MainWindow", "IP address"))
        self.getButton.setText(_translate("MainWindow", "Get IP"))
        self.getButton.setStatusTip(_translate("MainWindow", "Get IP address for the default gateway"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.startButton.setStatusTip(_translate("MainWindow", "Start Scanning"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.ipInput.setStatusTip(_translate("MainWindow", "Enter your <eth0> IP address along with subnet mask. E.g. 192.168.1.1/24"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Open a new window"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save the file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open a file"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionAbout_us.setText(_translate("MainWindow", "How to"))

    # Insert IP address to the IP input box
    def get_ip(self):
        self.ipInput.setText(lookup.get_ip_addr())

    # Check data check-box
    def check_box_state(self, checked):
        if checked.text() == "All":
            self.all = checked.isChecked()
        if checked.text() == "Company":
            self.company = checked.isChecked()
        if checked.text() == "Address":
            self.address = checked.isChecked()
        if checked.text() == "IP address":
            self.ip = checked.isChecked()
        if checked.text() == "MAC address":
            self.mac = checked.isChecked()
    

    # Fetch data & self.data = data
    def clicked(self):
        ip = self.ipInput.text()
        if len(ip.split(".")) == 4 and len(ip.split("/")) == 2:
            connected = lookup.send_packets(self.ipInput.text())
            data = []
            for device in connected:
                data.append({"IP Address": device["ip"], 
                             "Company": device["company"], 
                             "Address": device["address"], 
                             "Country": device["country"],
                             "MAC Address": device["mac"]
                            })
            self.data = data
            try:
                self.create_table()
            except IndexError:
                self.show_error("Packets not received", "Try again. if the same error occurs, Try with different IP address.")
                self.new()
        else:
            self.show_error("Invalid IP Address.", "Make sure the format matches the following:\n192.168.1.1/24")

    
    def clicked_cell(self, row, column):
        if column == 0 and self.tableWidget.item(row, column) is not None:
            self.selected_cell = self.tableWidget.item(row, column).text()
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Actions")
            msg.setText("Deauthenticate")
            msg.setInformativeText(f"Would you like to send deauthenticate packets to {self.selected_cell}?")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            msg.buttonClicked.connect(self.popup_button)

            x = msg.exec_()


    def popup_button(self, i):
        if i.text() == "OK":
            i, ok = QtWidgets.QInputDialog.getInt(self.centralwidget, 'Deauth packet', 'How long do you want to send it?\n10 = 1 Sec')
            if ok:
                deauth.send_deauth(self.selected_cell, i)
        else:
            return


    # Create and populate table with data
    def create_table(self):
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(self.data[0].keys())
        self.tableWidget.setRowCount(len(self.data))
        self.tableWidget.setColumnWidth(0, 210)
        self.tableWidget.setColumnWidth(1, 240)
        self.tableWidget.setColumnWidth(2, 355)
        self.tableWidget.setColumnWidth(3, 140)
        self.tableWidget.setColumnWidth(4, 230)
        row = 0

        if self.all:
            for device in self.data:
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(device["IP Address"]))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(device["Company"]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(device["Address"]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(device["Country"]))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(device["MAC Address"]))
                row += 1
        else:
            for device in self.data:
                if self.ip:
                    self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(device["IP Address"]))
                if self.company:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(device["Company"]))
                if self.address:
                    self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(device["Address"]))
                if self.mac:
                    self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(device["MAC Address"]))
                row += 1


    # Reset window and data
    def new(self):
        self.data = []
        while (self.tableWidget.rowCount() > 0):
            self.tableWidget.removeRow(0)
        self.ipInput.setText("")
        self.tableWidget.setColumnCount(0)
        self.allCheckBox.setChecked(True)
        self.companyCheckBox.setChecked(False)
        self.addressCheckBox.setChecked(False)
        self.ipCheckBox.setChecked(False)
        self.macCheckBox.setChecked(False)

    # Display error pop-up window with error
    def show_error(self, err, err_msg):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("ERROR")
        msg.setText(err)
        msg.setInformativeText(err_msg)
        msg.setIcon(QtWidgets.QMessageBox.Warning)

        x = msg.exec_()

    # Save data in JSON format
    def save(self):
        with open("data.txt", "w") as f:
            json.dump(self.data, f)

    # Retrieve saved data
    def open(self):
        try:
            with open("data.txt", "r") as f:
                self.data = json.load(f)
            self.create_table()
        except FileNotFoundError:
            self.show_error("File not found", "Cannot find the data file.")

    # Display info pop-up window
    def show_info(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("How to")
        msg.setText("This program finds devices that is connected to your Wi-Fi.")
        msg.setInformativeText("- Select the data you want to retrieve.\n- Enter your IP address (preferably Default Gateway) with / notation for the subnet\nE.g. 192.168.1.1/24")

        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    with open("./static/style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    sys.exit(app.exec_())
