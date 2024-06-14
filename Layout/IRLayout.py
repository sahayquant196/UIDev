from tkinter import *
from tkinter.ttk import *
import datetime as dt
import os
from PIL import ImageTk,Image
import pyautogui as pg


'''
THESE FUNCTIONS DEFINE THE LAYOUT OF THE IR PRICER
'''
def openIRWindow(root):
    IRWindow = Toplevel(root)
    IRWindow.title('Interest Rate Pricer')
    IRWindow.geometry('400x400')