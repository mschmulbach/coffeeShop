from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget


class Ui_Menu(object):
    def setupUi(self, Menu: QWidget) -> None:
        """
        Sets up the user interface for the menu.

        Args:
            Menu (QWidget): The main widget to which UI elements are added.
        """
        Menu.setObjectName("Menu")
        Menu.setEnabled(True)
        Menu.resize(370, 323)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Menu.sizePolicy().hasHeightForWidth())
        Menu.setSizePolicy(sizePolicy)
        Menu.setMinimumSize(QtCore.QSize(370, 323))
        Menu.setMaximumSize(QtCore.QSize(370, 323))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setItalic(True)
        Menu.setFont(font)
        self.menuLabel = QtWidgets.QLabel(parent=Menu)
        self.menuLabel.setGeometry(QtCore.QRect(0, 0, 371, 31))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(24)
        font.setItalic(False)
        self.menuLabel.setFont(font)
        self.menuLabel.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.menuLabel.setScaledContents(True)
        self.menuLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.menuLabel.setObjectName("menuLabel")
        self.menuLine = QtWidgets.QFrame(parent=Menu)
        self.menuLine.setGeometry(QtCore.QRect(0, 20, 401, 20))
        self.menuLine.setLineWidth(2)
        self.menuLine.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.menuLine.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.menuLine.setObjectName("menuLine")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Menu)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 50, 221, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.espressoLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.espressoLabel.setObjectName("espressoLabel")
        self.verticalLayout.addWidget(self.espressoLabel)
        self.americanoLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.americanoLabel.setObjectName("americanoLabel")
        self.verticalLayout.addWidget(self.americanoLabel)
        self.cappuccinoLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.cappuccinoLabel.setObjectName("cappuccinoLabel")
        self.verticalLayout.addWidget(self.cappuccinoLabel)
        self.mochaLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.mochaLabel.setObjectName("mochaLabel")
        self.verticalLayout.addWidget(self.mochaLabel)
        self.cafeLatteLabel = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.cafeLatteLabel.setObjectName("cafeLatteLabel")
        self.verticalLayout.addWidget(self.cafeLatteLabel)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=Menu)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(270, 50, 51, 191))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.espressoSpinBox = QtWidgets.QSpinBox(parent=self.verticalLayoutWidget_2)
        self.espressoSpinBox.setObjectName("espressoSpinBox")
        self.verticalLayout_2.addWidget(self.espressoSpinBox)
        self.americanoSpinBox = QtWidgets.QSpinBox(parent=self.verticalLayoutWidget_2)
        self.americanoSpinBox.setObjectName("americanoSpinBox")
        self.verticalLayout_2.addWidget(self.americanoSpinBox)
        self.cappuccinoSpinBox = QtWidgets.QSpinBox(parent=self.verticalLayoutWidget_2)
        self.cappuccinoSpinBox.setObjectName("cappuccinoSpinBox")
        self.verticalLayout_2.addWidget(self.cappuccinoSpinBox)
        self.mochaSpinBox = QtWidgets.QSpinBox(parent=self.verticalLayoutWidget_2)
        self.mochaSpinBox.setObjectName("mochaSpinBox")
        self.verticalLayout_2.addWidget(self.mochaSpinBox)
        self.cafeLatteSpinBox = QtWidgets.QSpinBox(parent=self.verticalLayoutWidget_2)
        self.cafeLatteSpinBox.setObjectName("cafeLatteSpinBox")
        self.verticalLayout_2.addWidget(self.cafeLatteSpinBox)
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Menu)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 240, 371, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addToCartButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addToCartButton.sizePolicy().hasHeightForWidth())
        self.addToCartButton.setSizePolicy(sizePolicy)
        self.addToCartButton.setObjectName("addToCartButton")
        self.horizontalLayout.addWidget(self.addToCartButton)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu: QWidget) -> None:
        """
        Translates the UI elements of the menu.

        Args:
            Menu (QWidget): The main widget containing UI elements to be translated.
        """
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Form"))
        self.menuLabel.setText(_translate("Menu", "MENU"))
        self.espressoLabel.setText(_translate("Menu", "ESPRESSO ................................$3"))
        self.americanoLabel.setText(_translate("Menu", "AMERICANO..............................$5"))
        self.cappuccinoLabel.setText(_translate("Menu", "CAPPUCCINO............................$6"))
        self.mochaLabel.setText(_translate("Menu", "MOCHA......................................$7"))
        self.cafeLatteLabel.setText(_translate("Menu", "CAFE LATTE...............................$7"))
        self.addToCartButton.setText(_translate("Menu", "Add to Cart"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QWidget()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec())
