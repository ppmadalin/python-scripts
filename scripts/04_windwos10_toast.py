# coding: utf-8

"""
An example of windwos 10 toast notification using windows10

Requirement: pip install win10toast 
"""
from win10toast import ToastNotifier


class ShowNotificationToast:
    def __init__(self, title, msg):
        self.toaster = ToastNotifier()
        self.title = title
        self.msg = msg

    def show(self):
        self.toaster.show_toast(
            self.title, self.msg, icon_path=None, duration=5, threaded=True
        )
        while self.toaster.notification_active():
            time.sleep(0.1)
