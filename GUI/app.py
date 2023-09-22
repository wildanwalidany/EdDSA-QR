from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QVBoxLayout, QPushButton

class Dialog(QDialog):
    def __init__(self):
        super().__init__()

        # Create the dialog's GUI
        self.label = QLabel('Enter your name:')
        self.input = QLineEdit()
        self.button = QPushButton('OK')
        self.button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.button)

        self.setLayout(layout)

app = QApplication([])

dialog = Dialog()
result = dialog.exec_()

if result == QDialog.Accepted:
    print(f'Your name is {dialog.input.text()}')

app.exec_()
