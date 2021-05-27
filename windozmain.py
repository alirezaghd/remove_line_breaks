
import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QClipboard
from PySide6.QtUiTools import QUiLoader



class windozmain(QMainWindow):
    def __init__(self):
        super(windozmain, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.ui.btn.clicked.connect(self.remove)

        self.ui.btn_copy.clicked.connect(self.copy)

    def remove(self):
        add = ""
        s = self.ui.tb_1.toPlainText().split('\n')
        for sen in s:
            add += sen
            add += ' '
        self.ui.tb_2.setText(str(add))

    def copy(self):

        self.ui.tb_2.selectAll()
        self.ui.tb_2.copy()



if __name__ == "__main__":
    app = QApplication([])
    window = windozmain()
    sys.exit(app.exec_())
