from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #let you dump graph into tkinter
import matplotlib #graph
from matplotlib import pyplot as plt #graph
matplotlib.use('TkAgg')

def get_plot(x, y):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    canvas = FigureCanvasTkAgg(fig, master=root)
    plot_widget = canvas.get_tk_widget()
    return plot_widget

root = Tk()

graph = get_plot(range(5), range(5))
graph.pack()

root.mainloop()
