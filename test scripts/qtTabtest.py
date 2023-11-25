import sys
import cv2
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QFormLayout,
    QGridLayout,
    QTabWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QDateEdit,
    QPushButton,
)
from PySide6.QtGui import QPixmap, QImage, QScreen, QColor, QPalette
from PySide6.QtCore import Qt


class FirstTab(QVBoxLayout):
    def __init__(self):
        super().__init__()

        layout2 = QVBoxLayout()
        # load image
        label = QLabel()
        image = QPixmap("./images/im1.jpg")
        label.setPixmap(image)

        layout2.addWidget(label)

        self.addLayout(layout2)


class SecondTab(QFormLayout):
    def __init__(self):
        super().__init__()

        self.addRow("Phone Number:", QLineEdit())
        self.addRow("Email Address:", QLineEdit())


class ThirdTab(QFormLayout):
    def __init__(self):
        super().__init__()

        self.addRow("First Name:", QLineEdit())
        self.addRow("Last Name:", QLineEdit())
        self.addRow("DOB:", QDateEdit())


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowTitle("PyQt QTabWidget")

        main_layout = QHBoxLayout(self)
        self.setLayout(main_layout)

        # create a tab widget
        tab = QTabWidget(self)

        # personal page
        personal_page = QWidget(self)
        personal_page.setLayout(ThirdTab())
        # contact pane
        contact_page = QWidget(self)
        contact_page.setLayout(SecondTab())
        # image pane
        image_page = QWidget(self)
        image_page.setLayout(FirstTab())

        # add pane to the tab widget
        tab.addTab(personal_page, "Personal Info")
        tab.addTab(contact_page, "Contact Info")
        tab.addTab(image_page, "wtf")

        main_layout.addWidget(tab)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
