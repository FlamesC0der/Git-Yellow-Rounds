import sys
import random

from PyQt6.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow


class ART(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.art_drawed = False
        self.init_ui()

    def init_ui(self):
        self.drawButton.clicked.connect(self.draw)

    def draw(self):
        if not self.art_drawed:
            self.art.setText(
                f"DRAWING; random color: {random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)}")
            self.art_drawed = True


if __name__ == "__main__":
    print("""\x1b[31m=================================================\x1b[0m
\x1b[32mThis program was created with \x1b[0m\x1b[31m♡\x1b[0m\x1b[32m by \x1b[0m\x1b[34mFlamesC0der\x1b[0m

https://github.com/FlamesC0der\x1b[0m
\x1b[31m=================================================\x1b[0m""")
    app = QApplication(sys.argv)
    ex = ART()
    ex.show()
    sys.exit(app.exec())
