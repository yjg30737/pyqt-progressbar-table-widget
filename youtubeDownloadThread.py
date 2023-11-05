from PyQt5.QtCore import QThread, pyqtSignal
from pytube import YouTube


class Thread(QThread):
    updateMaximumSize = pyqtSignal(int)
    progressUpdate = pyqtSignal(int)

    def __init__(self, url):
        super(Thread, self).__init__()
        self.__url = url

    def run(self):
        try:
            # This part can be modified based on application's purpose
            # YouTube downloader in this case
            yt = YouTube(self.__url, on_progress_callback=self.__progress_function)
            stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
            self.updateMaximumSize.emit(stream.filesize)
            # Start download
            stream.download()
        except Exception as e:
            raise Exception(e)

    def __progress_function(self, stream, chunk, bytes_remaining):
        progress = (stream.filesize - bytes_remaining)
        self.progressUpdate.emit(progress)