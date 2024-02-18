from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QRubberBand, QSizePolicy, QFileDialog
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt, QRect, QSize, QPoint
import sys
from json_handler import add_corner_to_json
from combination_getter import get_key_combination

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
  
        # this will hide the title bar
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.setStyleSheet("border : 3px solid blue;")
        #this will make the almost window transparent
        self.setWindowOpacity(0.31)
        #this will make the window fullscreen
        self.showFullScreen()
        
        self.pressed_keys = []
        
        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
        self.origin = QPoint()
        self.rect = None

        self.choosing_rect = True
        self.choosing_keys = False

    def get_file_path_from_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog  # Disable native dialog
        file_info = QFileDialog.getOpenFileUrl(self, "Select a File", options=options)

        try:
            if file_info:
                file_url = file_info[0]
                file_path = file_url.toLocalFile()
                return file_path
            else:
                print("No file selected.")
        except:
            print("No file selected.")

    def keyPressEvent(self, event):
        if not self.choosing_keys:
            if event.key() == Qt.Key_Escape:
                self.close()
        else:
            key = event.key()
            if key not in self.pressed_keys:
                self.pressed_keys.append(key)

    def keyReleaseEvent(self, event):
        # Remove released key from the list
        if self.choosing_keys:
            
            key = event.key()
            if key in self.pressed_keys:
                print('the chosen keys are: ', self.pressed_keys)
                self.pressed_keys = []
            
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.choosing_rect:
                self.origin = event.pos()
                self.rubberBand.setGeometry(QRect(self.origin, QSize()))
                self.rubberBand.show()


    def getRubberBandCoordinates(self):
        return self.rubberBand.geometry()
    
    def mouseMoveEvent(self, event):
        if not self.origin.isNull():
            if self.choosing_rect:
                self.rubberBand.setGeometry(QRect(self.origin, event.pos()).normalized())

    def mouseReleaseEvent(self, event):
        # Check if left mouse button is released
        if event.button() == Qt.LeftButton:
            if self.choosing_rect:
                rubber = self.getRubberBandCoordinates()
                self.choosing_rect = False
                self.rect = rubber
                self.rubberBand.hide()
                self.rubberBand.deleteLater() 
                self.menu_step()
    


    def menu_step(self):
        self.setWindowOpacity(0.8)
        self.setStyleSheet("")
        self.show_menu_buttons()


    def hide_buttons(self):
        for b in self.buttons:
            b.hide()

    def show_menu_buttons(self):
        # Create widget to hold buttons
        widget = QWidget(self)
        self.layout = QVBoxLayout(widget)

        # Create buttons
        button1 = QPushButton("Set command", self)
        button2 = QPushButton("Set shortcut", self)

        # Set button size policy to expanding
        button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Set button styles
        button1.setStyleSheet("background-color: blue; color: white; font-size: 24px;")
        button2.setStyleSheet("background-color: blue; color: white; font-size: 24px;")

        # Add buttons to layout
        self.layout.addWidget(button1)
        self.layout.addWidget(button2)

        # Set layout alignment
        self.layout.setAlignment(Qt.AlignCenter)

        # Set widget as central widget
        self.setCentralWidget(widget)
        # Connect button signals to functions
        button1.clicked.connect(self.set_command_button)
        button2.clicked.connect(self.set_shortcut_button)

        self.buttons = [button1, button2]



    def set_command_button(self):
        self.setWindowOpacity(0.01)
        self.hide_buttons()
        file_path = self.get_file_path_from_dialog()
        if file_path:
            add_corner_to_json(self.rect, file_path, 'command')

        self.close()


    def set_shortcut_button(self):
        self.setWindowOpacity(0.3)
        self.hide_buttons()
        add_corner_to_json(self.rect, get_key_combination(), 'shortcut')
        self.close()
    
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
window.show()
# start the app
sys.exit(App.exec())