

import numpy as np
# pyqtgraph with PySide6 - Ensure that PyQt5/6 are not anywhere near the project
import PySide6
import pyqtgraph as pg


from qtgui.widget import run 
from model.model import Model

# 

#import tkinter as tk

def main():
    #pg.plot(np.array([1,2,3]), np.array([3,2,1]), pen='r') 
    #input()
    m = Model()
    run(m)
    

if __name__ == "__main__":
    main()
