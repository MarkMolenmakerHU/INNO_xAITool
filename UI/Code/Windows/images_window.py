import functools

from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QWidget, QLabel, QGridLayout, QScrollArea, QVBoxLayout, QHBoxLayout, \
    QGraphicsOpacityEffect, QPushButton
from PyQt5.QtCore import Qt, pyqtSignal
from typing import Optional
import os


class Image(QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        QLabel.__init__(self, parent=parent)

    def mousePressEvent(self, event):
        self.clicked.emit()


class ImageSelectionWindow(QDialog):

    def image_click_handler(self, path, img):
        img.isIncluded = not img.isIncluded

        # creating a opacity effect
        opacity_effect = QGraphicsOpacityEffect()
        if img.isIncluded:
            opacity_effect.setOpacity(1)
            self.excluded_images.remove(path)
        else:
            opacity_effect.setOpacity(0.2)
            self.excluded_images.append(path)
        img.setGraphicsEffect(opacity_effect)

    def select_button_handler(self, path):
        print("Selected:" + path)
        print(self.excluded_images)

    def __init__(self, parent: Optional[QWidget]) -> None:
        super().__init__(parent, Qt.WindowCloseButtonHint)
        loadUi('UI/Design/images.ui', self)
        self.okButton.clicked.connect(self.close)

        self.excluded_images = []
        self.setWindowTitle('Images Selection')

        root = r'G:\temp\images'
        directories = [f.path for f in os.scandir(root) if f.is_dir()]

        for path in directories:
            directory = os.fsencode(path)

            # Create the gridlayout
            container = QWidget()
            images_layout = QGridLayout()
            x, y = 0, 0

            for file in os.listdir(directory):
                filename = os.fsdecode(file)
                if filename.endswith(".png") or filename.endswith(".jpg"):

                    image_label = Image(self)
                    file_path = path + '\\' + filename

                    image_label.isIncluded = True
                    image_label.clicked.connect(functools.partial(self.image_click_handler, file_path, image_label))

                    pixmap = QPixmap(file_path)
                    pixmap = pixmap.scaled(50, 50)

                    image_label.setPixmap(pixmap)
                    image_label.setMaximumSize(50, 50)

                    images_layout.addWidget(image_label, y, x)

                    y += 1
                    if y > 3:
                        y = 0
                        x += 1
                continue

            container.setLayout(images_layout)

            btn = QPushButton()
            btn.setText("Select: " + path)
            btn.clicked.connect(functools.partial(self.select_button_handler, path))

            scroll_area = QScrollArea()
            scroll_area.setWidget(container)

            scroll_layout = QVBoxLayout(self)
            scroll_layout.addWidget(scroll_area)
            scroll_layout.addWidget(btn)

            self.root_layout.layout().addLayout(scroll_layout)

        self.show()
