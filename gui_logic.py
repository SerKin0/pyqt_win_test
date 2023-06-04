from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from gui import Ui_Dialog


class GuiProgram(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.data = None
        self.setupUi(dialog)
        self.pushButton.clicked.connect(self.downloadFile)

    def downloadPath(self):
        wb_patch = QtWidgets.QFileDialog.getExistingDirectory(None, "Выберите папку для загрузки")
        print(wb_patch)

    def downloadFile(self):
        # Сохраняем данные из .txt файла в переменную, которую далее распакуем
        fname = QFileDialog.getOpenFileName(None, "Open File", ".", "Text Files (*.txt);;All Files (*)")[0]

        if not fname:                           # Если файл не был загружен, то ...
            print("Ошибка чтения файла")        # Выводим сообщение об ошибке в консоль и в виде окна
            QMessageBox.warning(None, "Ошибка загрузки", "Файл не загружен.")
        else:
            with open(fname, 'r', encoding='utf-8') as fh:
                self.data = fh.readlines()
                print(*self.data, sep='')
