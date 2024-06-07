# -*- encoding: utf-8 -*-
import os
import sys
import argparse
import time

from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QSplashScreen, QVBoxLayout, QProgressBar

from demoapp.app_info import __appname__
from demoapp.views.mainwindow import MainWindow


class MySplashScreen(QSplashScreen):
    # 鼠标点击事件
    def mousePressEvent(self, event):
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t", "--test", action="store_true", help="test app"
    )

    args = parser.parse_args()

    # config_from_args = args.__dict__
    # config_file_or_yaml = config_from_args.pop("config")
    # config = get_config(config_file_or_yaml, config_from_args)

    # language = config.get("language", QtCore.QLocale.system().name())
    # translator = QtCore.QTranslator()
    # loaded_language = translator.load(
    #     ":/languages/translations/" + language + ".qm"
    # )

    app = QtWidgets.QApplication(sys.argv)
    app.processEvents()

    app.setApplicationName(__appname__)
    # app.setWindowIcon(new_icon("icon"))

    # if loaded_language:
    #     app.installTranslator(translator)
    # else:
    #     logger.warning("Failed to load translation for %s. Using default language.", language)

    splash = MySplashScreen()
    # splash.setPixmap(QtGui.QPixmap(r"./ui/assets/SplashScreen_0.4.0.png"))
    splash.setFont(QtGui.QFont('Segoe UI', 11))
    splash.showMessage(
        "Welcome to Demo App",
        QtCore.Qt.AlignmentFlag.AlignCenter | QtCore.Qt.AlignmentFlag.AlignBottom,
        QtGui.QColor(175, 80, 0)
    )
    splash_layout = QVBoxLayout(splash)
    splash.setLayout(splash_layout)

    pbar = QProgressBar(splash)
    # pbar.setStyleSheet("QProgressBar {\n"
    #                    "    border: 2px solid grey;\n"
    #                    "    border-radius: 5px;\n"
    #                    "    text-align: center;\n"
    #                    "    font-size:12px;\n"
    #                    "}\n"
    #                    "QProgressBar::chunk {\n"
    #                    "    background-color: QLinearGradient(x1:0,y1:0,x2:2,y2:0,stop:0 #666699,stop:1  #DB7093);\n"
    #                    "}")
    pbar.setFixedHeight(15)
    # pbar.setFormat('Loaded  %p%'.format(pbar.value() - pbar.minimum()))
    pbar.setTextVisible(False)
    pbar.setMaximum(100)
    pbar.setMinimum(0)

    splash_layout.addWidget(pbar, alignment=QtCore.Qt.AlignmentFlag.AlignBottom)
    splash_layout.addSpacing(20)
    splash.show()

    pbar.setValue(15)

    win = MainWindow(
        app,
        config=None,
        filename=None,
        output_file=None,
        output_dir=None,
    )
    win.setMinimumSize(960, 720)
    time.sleep(1)
    pbar.setValue(60)

    time.sleep(1)
    pbar.setValue(99)

    splash.finish(win)
    splash.deleteLater()
    splash_layout.deleteLater()
    pbar.deleteLater()

    win.showMaximized()
    win.raise_()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
