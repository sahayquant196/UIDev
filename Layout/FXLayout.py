from tkinter import *
from tkinter.ttk import *
import datetime as dt
import os
from PIL import ImageTk,Image
import pyautogui as pg


'''
THESE FUNCTIONS DEFINE THE LAYOUT OF THE FX PRICER
'''
def openFXWindow(root):
    FXWindow = Toplevel(root)
    FXWindow.title('FX Pricer')
    FXWindow.geometry('400x400')