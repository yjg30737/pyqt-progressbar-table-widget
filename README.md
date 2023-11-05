# pyqt-progressbar-table-widget
QProgressBar in each row of QTableWidget to show the progression of multi-thread

I should've used different module to demonstrate multi-threading other than pytube because pytube or any other YouTube related modules tend to be changed a lot. Oh well..

Again, you will see this a lot in my other modules :)

After all using AI with mutiple threads will be really beneficial and necessary.

## Note
This may look like a YouTube downloader, but it is not a GUI script made for downloading YouTube videos. It is a modified QTableWidget designed to show the progress of each task through multithreading, and the YouTube video download is just an example of its use.

## Method Overview
`ProgressBarTableWidget` class:
* setProgressItems(items) - Insert a list of string items into the QTableWidget in order. The first cell contains the string, and the second cell is populated with a QProgressBar
* runItemFromRow(r_idx) - Run the task for the target row


# Requirements
* PyQt5 >= 5.14
* pytube - for showing the multi-thread progression of downloading youtube videos

## Preview
![image](https://github.com/yjg30737/pyqt-progressbar-table-widget/assets/55078043/761e351f-4777-406b-bbd9-9ed478aa853f)

## TODO
* support single thread function (in order) as well 
* disable the run button when running multi-threads
* running in background
