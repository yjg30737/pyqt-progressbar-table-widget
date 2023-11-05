from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QProgressBar, QVBoxLayout, \
    QWidget, QHeaderView, QPushButton

from youtubeDownloadThread import Thread

url_arr = [
'https://www.youtube.com/watch?v=EuS_bvQj--U&list=LL&index=9&pp=gAQBiAQB',
'https://www.youtube.com/watch?v=gyjE1qIPohA&list=LL&index=10&pp=gAQBiAQB',
'https://www.youtube.com/watch?v=fC9jISKU25E&list=LL&index=11&pp=gAQBiAQB',
'https://www.youtube.com/watch?v=jUs-ITmi_u4&list=LL&index=12&pp=gAQBiAQB',
'https://www.youtube.com/watch?v=Qw88zQTxq48&list=LL&index=13&pp=gAQBiAQB',
]


class ProgressBarTableWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        self.__items = []
        self.__threads = []

    def __initUi(self):
        cols = ['Name', 'Progress']
        # Add some header labels
        self.setColumnCount(len(cols))
        self.setHorizontalHeaderLabels(cols)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)

    def setProgressItems(self, items):
        self.__items = items
        for r_idx in range(len(self.__items)):
            self.setItem(r_idx, 0, QTableWidgetItem(self.__items[r_idx]))
            progressBar = QProgressBar(self)
            self.setCellWidget(r_idx, 1, progressBar)
            self.setItem(r_idx, 2, QTableWidgetItem('In Progress'))
        self.resizeColumnsToContents()

    def runItemFromRow(self, r_idx):
        item_text = self.item(r_idx, 0).text()
        t = Thread(item_text)
        self.__threads.append(t)
        t.started.connect(self.__started)
        t.finished.connect(self.__finished)

        # This ensures that the thread is removed from the list once it finishes
        t.finished.connect(lambda: self.__cleanupThread(t))

        progressbar = self.cellWidget(r_idx, 1)

        # Set maximum to file size for accurate progress bar scaling
        t.updateMaximumSize.connect(progressbar.setMaximum)
        t.progressUpdate.connect(progressbar.setValue)
        t.start()

    def __started(self):
        print('started')

    def __finished(self):
        print('finished')

    def __cleanupThread(self, thread):
        thread.deleteLater()  # Schedule the thread object for deletion
        self.__threads.remove(thread)  # Remove thread from the list


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        self.setWindowTitle('ProgressBar TableWidget!')

        self.__runBtn = QPushButton('Run!')
        self.__runBtn.clicked.connect(self.__run)

        self.__tableWidget = ProgressBarTableWidget()
        self.__tableWidget.setRowCount(len(url_arr))
        self.__tableWidget.setProgressItems(url_arr)

        lay = QVBoxLayout()
        lay.addWidget(self.__runBtn)
        lay.addWidget(self.__tableWidget)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)
        self.setCentralWidget(mainWidget)

    def __run(self):
        for r_idx in range(len(url_arr)):
            self.__tableWidget.runItemFromRow(r_idx)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
