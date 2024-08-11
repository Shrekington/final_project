import sys
from PyQt6.QtWidgets import QApplication
from assistant_app import AssistantApp

def main():
    app = QApplication(sys.argv)
    assistant = AssistantApp()
    assistant.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
