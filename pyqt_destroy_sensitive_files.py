from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QFileDialog
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit, QComboBox
from PyQt6.QtCore import Qt
from pathlib import Path

def open_files():
    global filenames
    filenames , _  = QFileDialog.getOpenFileNames(window, 'Select files')
    message.setText('\n'.join(filenames))

def destroy_files():
    for file in filenames:
        path = Path(file)
        with open(path, 'wb') as file:
            file.write(b'')
        path.unlink()
    message.setText('Destruction Succesful')

app = QApplication([])
window = QWidget()
window.setWindowTitle("Destroy Sensitive Files")
layout = QVBoxLayout()

description = QLabel('Select the files you want to destroy. The files will be <font color="red">permanently</font> deleted.') 
layout.addWidget(description)

open_btn = QPushButton('Open files')
open_btn.setFixedWidth(100)
layout.addWidget(open_btn, alignment=Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(open_files)

destroy_btn = QPushButton('Destroy files')
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn, alignment=Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(destroy_files)

message = QLabel('')
layout.addWidget(message)

window.setLayout(layout)
window.show()

app.exec()
