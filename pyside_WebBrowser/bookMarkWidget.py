import json, os, warnings

from PySide2 import QtCore
from PySide2.QtCore import (QDir, QFileInfo, QModelIndex, QStandardPaths, Qt, QUrl)
from PySide2.QtGui import QIcon, QPixmap, QStandardItem, QStandardItemModel
from PySide2.QtWidgets import (QAction, QDockWidget, QMenu, QMessageBox, QToolBar, QTreeView, QWidget)

_utl_role = Qt.UserRole + 1

_default_bookmarks =[
    ['Toll Bar'],
    ['http://qt.io', 'Qt', ':/qt-project.org/qmessagebox/images/qtlogo-64.png'],
    ['https://download.qt.io/snapshots/ci/pyside/', 'Downloads'],
    ['https://doc-snapshots.qt.io/qtforpython/', 'Documentation'],
    ['https://bugreports.qt.io/projects/PYSIDE/', 'Bug Reports'],
    ['https://www.python.org/', 'Python', None],
    ['https://wiki.qt.io/PySide2', 'Qt for Python', None],
    ['Other Bookmarks']
]

def _config_dir():
    return '{}/QtForPythonBrowser'.format(QStandardPaths.writableLocation(QStandardPaths.ConfigLocation))

_bookmark_file = 'bookmarks.json'

def _create_folder_item(title):
    result = QStandardItem(title)
    