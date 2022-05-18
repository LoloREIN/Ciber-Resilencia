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

        self.lbl02 = tkinter.Label(self.window, text="Fases de un evento\n disruptivo = ")
        self.lbl02.place(x=10, y=50)

        self.lbl03 = tkinter.Label(self.window, text="Ciberseguridad = ")
        self.lbl03.place(x=10, y=90)

        self.lbl04 = tkinter.Label(self.window, text="Poder Nacional = ")
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

        self.btn01.place(x=350, y=30, width=75)

        self.btn02 = tkinter.Button(self.window, text="Corte", command=self.btn02_click)

        self.btn02.place(x=350, y=70, width=75)

        self.window.mainloop()

    def showPlot(self, largo, ancho, alto):
        if largo > 9:
            largo = 10
        if ancho > 9:
            ancho = 10
        if alto > 9:
            alto = 10
        if largo < 2:
            largo = 1
        if ancho < 2:
            ancho = 1
        if alto < 2:
            alto = 1
        X, Y = np.meshgrid(np.arange(0, largo + 1), np.arange(0, ancho + 1))
        Z = 0 * X
        A, B = np.meshgrid(np.arange(0, alto + 1), np.arange(0, ancho + 1))
        C = 0 * A
        D, F = np.meshgrid(np.arange(0, largo + 1), np.arange(0, alto + 1))
        G = 0 * D
        fontx = {'family': 'serif',
                 'color': 'Red',
                 'weight': 'normal',
                 'size': 11,
                 }
        fonty = {'family': 'serif',
                 'color': 'Blue',
                 'weight': 'normal',
                 'size': 11,
                 }
        fontz = {'family': 'serif',
                 'color': 'Green',
                 'weight': 'normal',
                 'size': 11,
                 }
        lFig = Figure(figsize=(5, 4), dpi=100)
        lAxis = Axes3D(lFig, auto_add_to_figure=False)

        lAxis.set_xlabel("Fases de un evento disruptivo", fontdict=fontx)
        lAxis.set_ylabel("Ciberseguridad", fontdict=fonty)
        lAxis.set_zlabel("Poder Nacional", fontdict=fontz)
        lAxis.set_xlim(xmin=0, xmax=10)
        lAxis.set_ylim(ymin=0, ymax=10)
        lAxis.set_zlim(zmin=0, zmax=10)

        lAxis.plot_surface(X, Y, Z, alpha=.8, color="Green")  # Plano Horizontal
        lAxis.plot_surface(X, Y, Z + alto, alpha=.8, color="Green")  # Plano Horizontal con altura

        lAxis.plot_surface(C, B, A, alpha=.8, color="Blue")  # Plano Vertical
        lAxis.plot_surface(C + largo, B, A, alpha=.8, color="Blue")  # Plano Vertical con longitud

        lAxis.plot_surface(D, G, F, alpha=.8, color="Red")  # Plano Vertical
        lAxis.plot_surface(D, G + ancho, F, alpha=.8, color="Red")  # Plano Vertical con longitud
        lFig.add_axes(lAxis)

        lWin = tkinter.Tk()
        lWin.title("Modelo de Ciber Resilencia")
        canvas = FigureCanvasTkAgg(lFig, master=lWin)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    def WindowCut(self):
        largo = 10
        ancho = 10
        alto = .25
        XVec = np.arange(0, 10, .2)
        XSize = XVec.size
        YVec = np.arange(0, 10, .2)
        YSize = YVec.size

        ZMat = np.zeros((XSize, YSize))
        O, P = np.meshgrid(np.arange(0, largo + 1), np.arange(0, ancho + 1))
        Q = 0 * O
        A, B = np.meshgrid(np.arange(0, alto + 1), np.arange(0, ancho + 1))
        C = 0 * A
        D, F = np.meshgrid(np.arange(0, largo + 1), np.arange(0, alto + 1))
        G = 0 * D
        for XIdx in range(0, XSize):
            for YIdx in range(0, YSize):
                X = XVec[XIdx]
                Y = YVec[YIdx]

                Z = eval("cos(X)*sin(Y)*cos(Y)*sin(X)")
                ZMat[XIdx, YIdx] = Z

        XVecG, YVecG = np.meshgrid(XVec, YVec)
        fontx = {'family': 'serif',
                 'color': 'Red',
                 'weight': 'normal',
                 'size': 11,
                 }
        fonty = {'family': 'serif',
                 'color': 'Blue',
                 'weight': 'normal',
                 'size': 11,
                 }
        fontz = {'family': 'serif',
                 'color': 'Green',
                 'weight': 'normal',
                 'size': 11,
                 }
        lFig = Figure(figsize=(5, 4), dpi=100)
        lAxis = Axes3D(lFig, auto_add_to_figure=False)
        lAxis.set_xlabel("Fases de un evento disruptivo", fontdict=fontx)
        lAxis.set_xticklabels([])
        lAxis.set_ylabel("Ciberseguridad", fontdict=fonty)
        lAxis.set_yticklabels([])
        lAxis.set_zlabel("Poder Nacional", fontdict=fontz)
        lAxis.set_zticklabels([])

        lAxis.set_xlim(xmin=0, xmax=largo)
        lAxis.set_ylim(ymin=0, ymax=ancho)
        lAxis.set_zlim(zmin=-alto, zmax=alto)
        lAxis.plot_surface(XVecG, YVecG, ZMat, rstride=1, cstride=1, cmap='plasma')
        lAxis.plot_surface(O, P, Q-alto, alpha=.2, color="Green")  # Plano Horizontal
        lAxis.plot_surface(O, P, Q + alto, alpha=.2, color="Green")  # Plano Horizontal con altura

        lAxis.plot_surface(C, B, A/2-alto, alpha=.2, color="Blue")  # Plano Vertical
        lAxis.plot_surface(C + largo, B, A/2-alto, alpha=.2, color="Blue")  # Plano Vertical con longitud

        lAxis.plot_surface(D, G, F/2-alto, alpha=.2, color="Red")  # Plano Vertical
        lAxis.plot_surface(D, G + ancho, F/2-alto, alpha=.2, color="Red")  # Plano Vertical con longitud
        lFig.add_axes(lAxis)
        lWin = tkinter.Tk()
        lWin.title("Ciber-ResilenciaReal")
        canvas = FigureCanvasTkAgg(lFig, master=lWin)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


    def btn01_click(self):
        self.showPlot(int(self.txt02.get()), int(self.txt03.get()), int(self.txt04.get()))

    def btn02_click(self):
        self.WindowCut()


myPlotWin = PlotWin()
myPlotWin.createWindow()
