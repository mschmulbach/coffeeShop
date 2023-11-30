from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget


class Ui_orderSummary(object):
    def setupUi(self, orderSummary: QWidget) -> None:
        """
        Sets up the user interface for the order summary window.

        Args:
            orderSummary (QWidget): The main widget to which UI elements are added.
        """
        orderSummary.setObjectName("orderSummary")
        orderSummary.resize(370, 323)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(orderSummary.sizePolicy().hasHeightForWidth())
        orderSummary.setSizePolicy(sizePolicy)
        orderSummary.setMinimumSize(QtCore.QSize(370, 323))
        orderSummary.setMaximumSize(QtCore.QSize(370, 323))
        self.label = QtWidgets.QLabel(parent=orderSummary)
        self.label.setGeometry(QtCore.QRect(0, 0, 371, 31))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(parent=orderSummary)
        self.line.setGeometry(QtCore.QRect(0, 20, 401, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=orderSummary)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 190, 291, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backToMenuButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backToMenuButton.sizePolicy().hasHeightForWidth())
        self.backToMenuButton.setSizePolicy(sizePolicy)
        self.backToMenuButton.setObjectName("backToMenuButton")
        self.horizontalLayout.addWidget(self.backToMenuButton)
        self.confirmOrderButton = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirmOrderButton.sizePolicy().hasHeightForWidth())
        self.confirmOrderButton.setSizePolicy(sizePolicy)
        self.confirmOrderButton.setObjectName("confirmOrderButton")
        self.horizontalLayout.addWidget(self.confirmOrderButton)
        self.confirmationLabel = QtWidgets.QLabel(parent=orderSummary)
        self.confirmationLabel.setGeometry(QtCore.QRect(20, 230, 331, 71))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(14)
        self.confirmationLabel.setFont(font)
        self.confirmationLabel.setScaledContents(False)
        self.confirmationLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.confirmationLabel.setWordWrap(True)
        self.confirmationLabel.setObjectName("confirmationLabel")
        self.orderSummaryLabel = QtWidgets.QLabel(parent=orderSummary)
        self.orderSummaryLabel.setGeometry(QtCore.QRect(30, 40, 311, 141))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(13)
        self.orderSummaryLabel.setFont(font)
        self.orderSummaryLabel.setScaledContents(False)
        self.orderSummaryLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.orderSummaryLabel.setObjectName("orderSummaryLabel")

        self.retranslateUi(orderSummary)
        QtCore.QMetaObject.connectSlotsByName(orderSummary)

    def retranslateUi(self, orderSummary: QWidget) -> None:
        """
        Translates the UI elements of the order summary window.

        Args:
            orderSummary (QWidget): The main widget containing UI elements to be translated.
        """
        _translate = QtCore.QCoreApplication.translate
        orderSummary.setWindowTitle(_translate("orderSummary", "Form"))
        self.label.setText(_translate("orderSummary", "ORDER SUMMARY"))
        self.backToMenuButton.setText(_translate("orderSummary", "Back to Menu"))
        self.confirmOrderButton.setText(_translate("orderSummary", "Confirm Order"))
        self.confirmationLabel.setText(_translate("orderSummary", "TextLabel"))
        self.orderSummaryLabel.setText(_translate("orderSummary", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    orderSummary = QtWidgets.QWidget()
    ui = Ui_orderSummary()
    ui.setupUi(orderSummary)
    orderSummary.show()
    sys.exit(app.exec())
