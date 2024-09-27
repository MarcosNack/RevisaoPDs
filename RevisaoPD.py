from PySide6.QtWidgets import QApplication
import sys
from controllers.interfaces import MainReviewPD


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainReviewPD()
    window.show()
    sys.exit(app.exec())