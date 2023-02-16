"""
BY: Miaow, Wanderson M.Pimenta
PROJECT MADE WITH: Qt Designer and PySide6
V: 1.0.0

This project can be used freely for all uses, as long as they maintain the
respective credits only in the Python scripts, any information in the visual
interface (GUI) can be modified without any implication.

There are limitations on Qt licenses if you want to use your products
commercially, I recommend reading them on the official website:
https://doc.qt.io/qtforpython/licenses.html
"""
from main import MainWindow
from modules.app_settings import Settings
from PySide6.QtCore import QAbstractTableModel, Qt


class AppFunctions(MainWindow):
    def set_theme_hack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """
        # SET MANUAL STYLES
        # self.ui.lineEdit.setStyleSheet("background-color: #6272a4;")
        # self.ui.pushButton.setStyleSheet("background-color: #6272a4;")
        # self.ui.plainTextEdit.setStyleSheet("background-color: #6272a4;")
        # self.ui.tableWidget.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        # self.ui.scrollArea.setStyleSheet("QScrollBar:vertical { background: #6272a4; } QScrollBar:horizontal { background: #6272a4; }")
        # self.ui.comboBox.setStyleSheet("background-color: #6272a4;")
        # self.ui.horizontalScrollBar.setStyleSheet("background-color: #6272a4;")
        # self.ui.verticalScrollBar.setStyleSheet("background-color: #6272a4;")
        # self.ui.commandLinkButton.setStyleSheet("color: #ff79c6;")


class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def data(self, index, role=...):
        if role == Qt.DisplayRole:
            return f"{self._data[index.row()][index.column()]:.2f}"

    def headerData(self, section, orientation, role=...):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return f"Channel {section + 1}"

            if orientation == Qt.Vertical:
                return str(section + 1)

    def rowCount(self, index=...):
        if index is not None:
            return len(self._data)

    def columnCount(self, index=...):
        return len(self._data[0])
