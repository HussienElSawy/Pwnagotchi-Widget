import sys
import time
import requests
from io import BytesIO
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer

class ImageRefresher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pwnagotchi UI")
        self.setFixedSize(720, 420) 
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 720, 420)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setScaledContents(True)

        self.label.setFont(QFont("Courier", 14))

        self.base_url = "http://10.0.0.2:8080/ui"
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_image)
        self.timer.start(1000)  # every 1 second

        self.update_image()

    def connectivity_check(self):
        try:
            requests.get(self.base_url, timeout=2)
            return True
        except requests.ConnectionError:
            return False
        
    def update_image(self):
        timestamped_url = f"{self.base_url}?{int(time.time()*1000)}"
        try:
            response = requests.get(timestamped_url, timeout=3)
            pixmap = QPixmap()
            pixmap.loadFromData(BytesIO(response.content).read())
            self.label.setPixmap(pixmap)
        except Exception as e:
            self.label.setText(f"Couldn't Connect to Pwnagotchi UI")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageRefresher()
    window.show()
    sys.exit(app.exec_())