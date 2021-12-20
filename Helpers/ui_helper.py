from PyQt5.QtWidgets import QLabel, QPushButton
from UI.Code.Components.modal import Modal


def bind_selectable(stacked_widget, scroll_contents, select_action):
    def show_description(event):
        Modal(stacked_widget, "Dit is wat extra info over de dataset.")

    def show_info(event):
        Modal(stacked_widget, "Dit zijn wat use cases met de dataset.")

    def select_option(i, child, title):
        return lambda event: select_action(event, i, child, title)

    for i, child in enumerate(scroll_contents.children()[1:]):
        title = child.findChild(QLabel, f'titleLabel{i}').text()

        select_button = child.findChild(QPushButton, f'selectButton{i}')
        select_button.clicked.connect(select_option(i, child, title))

        description_button = child.findChild(QPushButton, f'descriptionButton{i}')
        description_button.clicked.connect(show_description)

        info_label = child.findChild(QLabel, f'infoLabel{i}')
        info_label.mousePressEvent = show_info
