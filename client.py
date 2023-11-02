import sys
import socket
import string
import os
from PySide6 import QtCore
from PySide6.QtCore import QThread
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QGraphicsDropShadowEffect

from ui import *

GLOBAL_STATE = False


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"XO", None))
        self.ui.wl.setVisible(False)
        self.ui.pages.setCurrentWidget(self.ui.connect_page)
        self.ip = ''
        self.port = 0

        self.win = 0
        self.loose = 0

        self.ui.ip_line.textEdited.connect(lambda: self.ui.connect_label.setText(''))

        # BUTTONS
        # ///////////////////////////////////////////////////////////////////////////////////////////////////
        self.ui.close_button.clicked.connect(lambda: self.close())
        self.ui.minimize_button.clicked.connect(lambda: self.showMinimized())
        self.ui.connect_button.clicked.connect(lambda: self.connect_to_game())

        # MOVE WINDOW FUNCTION
        # ///////////////////////////////////////////////////////////////////////////////////////////////////

        def move_window(event):
            if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
                pos = self.pos()
                glpos = event.globalPosition().toPoint()
                self.move(pos + glpos - self.dragPos.toPoint())
                self.dragPos = event.globalPosition()
                event.accept()

        self.ui.centralwidget.mouseMoveEvent = move_window
        self.show()

    # DROP SHADOW
    # ///////////////////////////////////////////////////////////////////////////////////////////////////
    def drop_shadow(self, widget: QWidget):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        widget.setGraphicsEffect(self.shadow)

        self.drop_shadow(self.ui.connect_button)
        self.drop_shadow(self.ui.ip_line)

    def button_click(self):
        btn = self.sender()
        btn_name = btn.objectName()

        if btn_name in [f'c_{x}' for x in range(1, 10)]:
            return btn_name

    def set_state_game_buttons(self, state: bool):
        for button in [self.ui.c_1, self.ui.c_2, self.ui.c_3, self.ui.c_4, self.ui.c_5,self.ui.c_6, self.ui.c_7, self.ui.c_8, self.ui.c_9]:
            button.setDisabled(False) if state else button.setDisabled(True)

    def check_ip(self, ip: str):
        for char in ip:
            if char not in string.digits + '.':
                self.ui.connect_label.setText('Incorrect IP')
                return False
        return True

    def connect_to_game(self):
        self.ip = self.ui.ip_line.text()

        if self.check_ip(self.ip):
            self.client_thread = ClientThread(self.ui)
            self.client_thread.start()

    def start_game(self):
        self.ui.wl.setVisible(True)
        self.ui.xo_label.setMaximumWidth(0)
        self.ui.pages.setCurrentWidget(self.ui.game_page)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition()


class ClientThread(QThread, MainWindow):
    def __init__(self, ui):
        super(ClientThread, self).__init__()
        self.ui = ui
        self.ip = self.ui.ip_line.text()
        self.buttons_list = [f'c_{x}' for x in range(1, 10)]
        self.enabled_buttons = self.buttons_list.copy()
        self.first = True

        self.win = 0
        self.loose = 0
        self.cells_count = 0

        self.cells = []
        self.end_game_list = []

        for cell in [self.ui.c_1, self.ui.c_2, self.ui.c_3, self.ui.c_4, self.ui.c_5, self.ui.c_6,
                     self.ui.c_7, self.ui.c_8, self.ui.c_9]:
            cell.clicked.connect(self.send_data)

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.client:
            try:
                self.client.connect((self.ip, 9000))
            except (ConnectionRefusedError, TimeoutError, OSError):
                self.ui.connect_label.setText('Server is not response')
            else:
                self.start_game()

            while True:
                try:
                    data = self.client.recv(1024).decode('utf-8')
                    if data:
                        if data == 'false_buttons':
                            self.set_state_game_buttons(False)
                        elif data == 'loose':
                            self.loose += 1
                            self.ui.wl.setText(f'W: {self.win}   L: {self.loose}')
                            self.ui.pages.setCurrentWidget(self.ui.loose_page)
                        elif data == 'draw':
                            self.ui.pages.setCurrentWidget(self.ui.draw_page)
                        elif data == 'new_game':
                            self.new_game()
                        elif 'key' in data:
                            data = data.split()
                            data.remove('key')
                            self.disable_icons(data)
                        else:
                            self.disable_buttons(data)
                            self.enable_buttons()
                            getattr(self.ui, data).setIcon(QIcon(u":/img/images/img/X.png"))

                except OSError:
                    self.client.close()

    def send_data(self):
        btn = MainWindow.sender(self)
        btn_name = btn.objectName()
        if btn_name in self.buttons_list:
            self.client.send(btn_name.encode('utf-8'))
        self.disable_buttons(btn_name)
        self.set_state_game_buttons(False)
        getattr(self.ui, btn_name).setIcon(QIcon(u":/img/images/img/O.png"))
        self.cells.append(btn_name)
        self.game(self.cells)

    def disable_buttons(self, *button: str):
        if button:
            self.enabled_buttons.remove(button[0])
        return self.enabled_buttons

    def enable_buttons(self):
        for button in self.enabled_buttons:
            getattr(self.ui, button).setDisabled(False)

    def end_game(self, end_game_lst):
        self.set_state_game_buttons(False)
        self.client.send('false_buttons'.encode('utf-8'))
        if self.cells_count == 3:
            self.disable_icons(end_game_lst)
            self.client.send(f'{" ".join(self.end_game_list)} key'.encode('utf-8'))
            QTest.qWait(2000)
            self.client.send('loose'.encode('utf-8'))
            self.ui.pages.setCurrentWidget(self.ui.win_page)
            self.win += 1
            self.ui.wl.setText(f'W: {self.win}   L: {self.loose}')
        else:
            QTest.qWait(2000)
            self.client.send('draw'.encode('utf-8'))
            self.ui.pages.setCurrentWidget(self.ui.draw_page)
        QTest.qWait(2000)
        self.client.send('new_game'.encode('utf-8'))
        self.new_game()

    def new_game(self):
        if self.first:
            self.first = False
        else:
            self.first = True
        self.ui.pages.setCurrentWidget(self.ui.game_page)
        self.enabled_buttons = self.buttons_list.copy()
        self.cells.clear()
        self.set_state_game_buttons(self.first)

        for button in self.buttons_list:
            getattr(self.ui, button).setIcon(QIcon(u""))

    def disable_icons(self, end_game_lst):
        finish_list = self.buttons_list.copy()
        for button in end_game_lst:
            finish_list.remove(button)

        for button in finish_list:
            getattr(self.ui, button).setIcon(QIcon(u""))

    def game(self, cells):
        c1 = ['c_1', 'c_2', 'c_3']
        c2 = ['c_4', 'c_5', 'c_6']
        c3 = ['c_7', 'c_8', 'c_9']
        c4 = ['c_1', 'c_4', 'c_7']
        c5 = ['c_2', 'c_5', 'c_8']
        c6 = ['c_3', 'c_6', 'c_9']
        c7 = ['c_1', 'c_5', 'c_9']
        c8 = ['c_3', 'c_5', 'c_7']

        for cell_lists in [c1, c2, c3, c4, c5, c6, c7, c8]:
            self.cells_count = 0
            for cell in cell_lists:
                if cell in cells:
                    self.cells_count += 1
                if self.cells_count == 3:
                    self.end_game_list = cell_lists.copy()
                    self.end_game(self.end_game_list)
                    return
        if len(self.enabled_buttons) == 0:
            self.end_game(self.end_game_list)


if __name__ == "__main__":

    def resource_path(relative_path):
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    ico = resource_path("icon.ico")
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(ico))
    window = MainWindow()
    sys.exit(app.exec())
