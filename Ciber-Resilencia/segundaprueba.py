import tkinter
import matplotlib

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

# from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

import numpy as np
from math import *


def prSetTxt(pTxt, pVal):
    pTxt.delete(0, len(pTxt.get()))
    pTxt.insert(0, pVal)


class PlotWin:

    def createWindow(self):
        self.window = tkinter.Tk()

        self.window.title("Ciber-Resilencia")
        self.window.geometry("430x250+100+200")

        self.lbl02 = tkinter.Label(self.window, text="Poder nacional= ")
        self.lbl02.place(x=10, y=50)

        self.lbl03 = tkinter.Label(self.window, text="Fase del Ciber ataque = ")
        self.lbl03.place(x=10, y=90)

        self.lbl04 = tkinter.Label(self.window, text="= ")
        self.lbl04.place(x=10, y=130)

        self.txt02 = tkinter.Entry(self.window, bg="lightgray", width=17)

        self.txt02.place(x=160, y=48)
        prSetTxt(self.txt02, '4')

        self.txt03 = tkinter.Entry(self.window, bg="lightgray", width=17)

        self.txt03.place(x=160, y=88)
        prSetTxt(self.txt03, '5')

        self.txt04 = tkinter.Entry(self.window, bg="lightgray", width=17)

        self.txt04.place(x=160, y=128)
        prSetTxt(self.txt04, '6')

        self.btn01 = tkinter.Button(self.window, text="Muestra", command=self.btn01_click)

        self.btn01.place(x=350, y=10, width=75)

        self.window.mainloop()

    def showPlot(self, largo, ancho, alto):
        X, Y = np.meshgrid(np.arange(0, largo + 1), np.arange(0, ancho + 1))
        Z = 0 * X
        A, B = np.meshgrid(np.arange(0, alto + 1), np.arange(0, ancho + 1))
        C = 0 * A
        D, F = np.meshgrid(np.arange(0, largo + 1), np.arange(0, alto + 1))
        G = 0 * D

        lFig = Figure(figsize=(5, 4), dpi=100)
        lAxis = Axes3D(lFig)
        lAxis.set_xlim(xmin=0, xmax=10)
        lAxis.set_ylim(ymin=0, ymax=10)
        lAxis.set_zlim(zmin=0, zmax=10)

        lAxis.plot_surface(X, Y, Z, alpha=0.5)  # Plano Horizontal
        lAxis.plot_surface(X, Y, Z + alto, alpha=0.5)  # Plano Horizontal con altura

        lAxis.plot_surface(C, B, A, alpha=0.5)  # Plano Vertical
        lAxis.plot_surface(C + largo, B, A, alpha=0.5)  # Plano Vertical con longitud

        lAxis.plot_surface(D, G, F, alpha=0.5)  # Plano Vertical
        lAxis.plot_surface(D, G + ancho, F, alpha=0.5)  # Plano Vertical con longitud

        XVec = np.arange(int(pRangoI), int(pRangoF), float(Steps))
        XSize = XVec.size
        YVec = np.arange(int(pRangoI), int(pRangoF), float(Steps))
        YSize = YVec.size

        ZMat = np.zeros((XSize, YSize))

        for XIdx in range(0, XSize):
            for YIdx in range(0, YSize):
                X = XVec[XIdx]
                Y = YVec[YIdx]

                Z = eval(pFunc)
                ZMat[XIdx, YIdx] = Z

        XVecG, YVecG = np.meshgrid(XVec, YVec)

        lFig = Figure(figsize=(5, 4), dpi=100)
        lAxis = Axes3D(lFig)
        lAxis.plot_surface(XVecG, YVecG, ZMat, rstride=1, cstride=1, cmap='cividis')


        lWin = tkinter.Tk()
        lWin.title("Modelo de Ciber Resilencia")
        canvas = FigureCanvasTkAgg(lFig, master=lWin)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    def btn01_click(self):
        self.showPlot(int(self.txt02.get()), int(self.txt03.get()), int(self.txt04.get()))


myPlotWin = PlotWin()
myPlotWin.createWindow()