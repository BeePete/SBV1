# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:38:12 2019

@author: Minh
"""

import win32api
import winsound
from threading import Thread

def showAlertDialog(title, text):
    
    def show_dialog(title, text):
        duration = 2000 #ms
        freq = 440 #Hz
        winsound.Beep(freq, duration)
        win32api.MessageBox(0, text, title, 0x00001000)
        
    t = Thread(target=show_dialog, args=(title, text, ))
    t.start()
    
    
if __name__ == "__main__":
    import time
    showAlertDialog("1", "")
    time.sleep(1)
    showAlertDialog("2", "")