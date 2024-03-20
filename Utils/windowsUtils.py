import subprocess
import keyboard
import pyautogui
import pygetwindow as gw


def isWindowActive(window):
    activeWindow = gw.getActiveWindow()
    if activeWindow is not None:
        return activeWindow.title == window
    return False


def isKeyPressed(key):
    return keyboard.is_pressed(key)


def enterAccountDetails(username, password):
    pyautogui.typewrite(username)
    pyautogui.press("tab")
    pyautogui.typewrite(password)
    pyautogui.press("enter")


def callSubprocess(path):
    subprocess.call(path)
