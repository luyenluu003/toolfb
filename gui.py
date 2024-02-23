import sys

from PyQt5.QtWidgets import (QApplication, QFileDialog, QLabel, QMessageBox,
                             QPushButton, QTableWidget, QTableWidgetItem,
                             QVBoxLayout, QWidget)


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Chọn File'
        self.width = 400
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100,100,self.width, self.height)

        layout = QVBoxLayout(self)

        label = QLabel('Danh sách tài khoản', self)
        layout.addWidget(label)

        table = QTableWidget(self)
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(['Username', 'Password', 'Token'])
        layout.addWidget(table)

        button = QPushButton('Chọn File', self)
        button.setToolTip('Click để chọn Accounts')
        button.clicked.connect(self.on_click)
        layout.addWidget(button)

        self.show()

    def on_click(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Chọn file Accounts", "", "Text File (*.txt)", options=options)
        if fileName:
            self.read_accounts(fileName)

    def read_accounts(self, filePath):
        with open(filePath, 'r') as file:
            accounts = []
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 3:
                    accounts.append(parts)
                else:
                    QMessageBox.warning(self, 'Lỗi', f'Dòng không hợp lệ: {line}')

        table = self.findChild(QTableWidget)
        table.setRowCount(len(accounts))

        for row, account in enumerate(accounts):
            username = account[0]
            password = account[1]
            token = account[2]

            table.setItem(row, 0, QTableWidgetItem(username))
            table.setItem(row, 1, QTableWidgetItem(password))
            table.setItem(row, 2, QTableWidgetItem(token))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())