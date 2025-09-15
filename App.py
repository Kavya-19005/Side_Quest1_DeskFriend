import sys
import itertools
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFrame, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont, QPalette, QBrush, QLinearGradient, QColor
from PyQt5.QtCore import QTimer, Qt, QPoint

# Characters and messages
characters = [
    (r"C:\Users\kavya\Desktop\Programming\Side_Q_Bday\2025 sep 20\Pepper-removebg-preview.png", "🐾 Welcome home!"),
    (r"C:\Users\kavya\Desktop\Programming\Side_Q_Bday\2025 sep 20\kavya-removebg-preview.png", "✨ Rest well, you deserve it."),
]

class ReassuranceApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Home Box")
        self.setFixedSize(480, 480)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        # Warm gradient background
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor("#ffccff"))  # Pink of some sort
        gradient.setColorAt(1.0, QColor("#d9ffb3"))  # Some kinda green
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(palette)
        self.setAutoFillBackground(True)

        # Main layout (vertical)
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(12, 12, 12, 12)
        main_layout.setSpacing(8)

        # --- Top bar with close button ---
        top_bar = QHBoxLayout()
        top_bar.addStretch()

        self.close_btn = QPushButton("✖")
        self.close_btn.setFixedSize(28, 28)
        self.close_btn.setStyleSheet("""
            QPushButton {
                background-color: #e6d3b3;
                color: #4b2e15;
                border: 2px solid #8b5a2b;
                border-radius: 6px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #d6bfa9;
            }
        """)
        self.close_btn.clicked.connect(self.close)
        top_bar.addWidget(self.close_btn)

        main_layout.addLayout(top_bar)

        # --- Character image ---
        self.img_label = QLabel(self)
        self.img_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.img_label)

        # --- Dialog bubble ---
        self.dialog_box = QFrame(self)
        self.dialog_box.setStyleSheet("""
            QFrame {
                background-color: #fff8dc;
                border: 2px solid #8b5a2b;
                border-radius: 12px;
            }
        """)
        dialog_layout = QVBoxLayout()
        dialog_layout.setContentsMargins(12, 8, 12, 8)

        self.text_label = QLabel("", self.dialog_box)
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setWordWrap(True)
        self.text_label.setFont(QFont("Georgia", 13))
        self.text_label.setStyleSheet("color: #4b2e15;")
        dialog_layout.addWidget(self.text_label)
        self.dialog_box.setLayout(dialog_layout)

        main_layout.addWidget(self.dialog_box, alignment=Qt.AlignCenter)

        self.setLayout(main_layout)

        # Iterator for cycling
        self.cycle = itertools.cycle(characters)
        self.update_content()

        # Timer to switch images/messages
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_content)
        self.timer.start(5000)

        # For dragging
        self.dragging = False
        self.offset = QPoint()

    def update_content(self):
        img_path, message = next(self.cycle)
        pixmap = QPixmap(img_path).scaled(240, 240, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.img_label.setPixmap(pixmap)
        self.text_label.setText(message)

    # --- Drag to move ---
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReassuranceApp()
    window.show()
    sys.exit(app.exec_())
