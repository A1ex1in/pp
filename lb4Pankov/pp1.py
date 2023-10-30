from PyQt5 import QtWidgets
from gui import Ui_MainWind
from PyQt5.QtGui import QPixmap
import sys
import function

class mywindow(QtWidgets.QMainWindow):
    def __init__(self, picture_path = None):
        self.picture_path = picture_path
        super(mywindow, self).__init__()
        self.ui = Ui_MainWind()
        self.ui.setupUi(self)
        self.ui.pushButton_1.clicked.connect(self.browse_folder)
        self.ui.pushButton_2.clicked.connect(self.encrypt)
        self.ui.pushButton_3.clicked.connect(self.decrypt)

    def browse_folder(self):
        self.ui.textEdit.clear()
        self.ui.label_x.clear()
        self.ui.label_y.clear()

        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_3.setEnabled(True)

        self.picture_path = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл", '.', 'Изображение (*.png)')
        pixmap = QPixmap(self.picture_path[0])
        pixmap = pixmap.scaled(200, 200, aspectRatioMode=1)
        self.ui.label_x.setPixmap(pixmap)

    def encrypt(self):
        self.ui.pushButton_2.setEnabled(False)
        self.save, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Выберете куда сохранить файл", '.', 'Изображение (*.png)')

        self.im = function.cod(self.picture_path[0], self.ui.textEdit.toPlainText(), self.save)

        pixmap = QPixmap(self.im)
        pixmap = pixmap.scaled(200, 200, aspectRatioMode=1)
        self.ui.label_y.setPixmap(pixmap)

    def decrypt(self):
        self.ui.pushButton_3.setEnabled(False)
        self.txt = function.decod(self.picture_path[0])
        self.ui.textEdit.setPlainText(self.txt)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()