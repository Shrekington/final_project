import sys
from PyQt6.QtWidgets import QApplication,  QLabel, QWidget
from PyQt6.QtGui import QKeyEvent, QPixmap
from PyQt6.QtCore import Qt

class AssistantApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle('MAX')
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Load the image
        image_path = "assets/images/mascot.png"
        pixmap = QPixmap(image_path)

        # Create label and set the pixmap
        label = QLabel(self)
        label.setPixmap(pixmap)
        label.setStyleSheet("background: transparent;")

        # Set the size of the window to match the image
        self.resize(pixmap.width(), pixmap.height())

        # Position the window in the bottom right corner of the screen
        screen = QApplication.primaryScreen().availableGeometry()
        x_position = screen.width() - self.width()
        y_position = screen.height() - self.height()
        self.move(x_position, y_position)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Escape:
            self.close()

def main():
    app = QApplication(sys.argv)
    assistant = AssistantApp()
    assistant.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
