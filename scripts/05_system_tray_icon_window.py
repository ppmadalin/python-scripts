# coding: utf-8

"""
An example of script of how you can create a system tray icon using python

Requirements: pip install pystray
"""
import pystray
from pystray import Menu, MenuItem
from PIL import Image

class ShowSystemTryIcon:
    def __init__(self):
        self.icon = pystray.Icon("File Organization System")
        self.icon.menu = Menu(MenuItem("Exit", lambda: self.exit_action(self.icon)))
        self.icon.icon = Image.open("img/icon.jpg")
        self.icon.title = "Python"
        self.icon.run(self.setup(self.icon))

    def setup(self, icon):
        icon.visible = True

        # i = 0
        # while icon.visible:
        #     Do things here
        #     print(i)
        #     i += 1
        #     time.sleep(5)

    def exit_action(self, icon):
        icon.visible = False
        icon.stop()
        raise KeyboardInterrupt("Program stop...")
