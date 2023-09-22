from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton

class QRCodeGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Create the input fields and labels
        messageLabel = QLabel('Message:', self)
        self.messageInput = QLineEdit(self)
        keyLabel = QLabel('Private Key:', self)
        self.keyInput = QLineEdit(self)
        
        # Create the output field
        self.qrCodeOutput = QTextEdit(self)
        self.qrCodeOutput.setReadOnly(True)
        
        # Create the buttons
        generateButton = QPushButton('Generate QR Code', self)
        generateButton.clicked.connect(self.generateQRCode)
        clearButton = QPushButton('Clear', self)
        clearButton.clicked.connect(self.clear)
        
        # Create the layouts
        inputLayout = QHBoxLayout()
        inputLayout.addWidget(messageLabel)
        inputLayout.addWidget(self.messageInput)
        inputLayout.addWidget(keyLabel)
        inputLayout.addWidget(self.keyInput)
        
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(generateButton)
        buttonLayout.addWidget(clearButton)
        
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(inputLayout)
        mainLayout.addWidget(self.qrCodeOutput)
        mainLayout.addLayout(buttonLayout)
        
        self.setLayout(mainLayout)
    
    def generateQRCode(self):
        message = self.messageInput.text()
        key = self.keyInput.text()
        # Generate QR code using PyNaCl and display it in the qrCodeOutput field
        pass
    
    def clear(self):
        self.messageInput.setText('')
        self.keyInput.setText('')
        self.qrCodeOutput.setText('')

app = QApplication([])
window = QRCodeGenerator()
window.show()
app.exec_()
