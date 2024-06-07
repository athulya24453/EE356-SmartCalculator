import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grapher import Grapher # type: ignore
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt

class Graph_Frame2D(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(bg="black",width=600,height=800)
        self.wm_attributes("-fullscreen", "True")
        self._create_widgets_2D()

    def _create_widgets_2D(self):
        # Create a frame for the plot and toolbar
        frame = ttk.Frame(self)
        frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create a Matplotlib figure
        self.fig = Figure(figsize=(5, 4), dpi=100,facecolor="black")
        self.ax = self.fig.add_subplot(111)
        self.ax.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])

        self.ax.set_facecolor("black")
        self.ax.spines['bottom'].set_color('white')
        self.ax.spines['left'].set_color('white')
        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        self.ax.yaxis.label.set_color('white')
        self.ax.xaxis.label.set_color('white')

        # Embed the Matplotlib figure in the Tkinter canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Add the Matplotlib toolbar
        toolbar_frame = ttk.Frame(self)
        toolbar_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        toolbar = NavigationToolbar2Tk(self.canvas, toolbar_frame)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create a button to update the plot
        self.update_button = ttk.Button(self, text="Update Plot", command=self.change_plot)
        self.update_button.pack(side=tk.BOTTOM)

    def change_plot(self):
        # Update the plot with new data
        self.destroy()

    def close(self):
        self.destroy()

class Graph_Frame3D(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config(bg="black",width=600,height=800)
        self.wm_attributes("-fullscreen", "True")
        self._create_widgets_3D()

    def _create_widgets_3D(self):
        # Create a frame for the plot and toolbar
        frame = ttk.Frame(self)
        frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create a Matplotlib figure
        self.fig = plt.figure(figsize=(5, 4), dpi=100, facecolor="black")
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40], [0, 1, 2, 3, 4])

        self.ax.set_facecolor("black")
        self.ax.spines['bottom'].set_color('white')
        self.ax.spines['left'].set_color('white')
        self.ax.spines['right'].set_color('white')
        self.ax.spines['top'].set_color('white')
        self.ax.tick_params(axis='x', colors='white')
        self.ax.tick_params(axis='y', colors='white')
        self.ax.tick_params(axis='z', colors='white')
        self.ax.yaxis.label.set_color('white')
        self.ax.xaxis.label.set_color('white')
        self.ax.zaxis.label.set_color('white')
        self.ax.xaxis.pane.fill = False
        self.ax.yaxis.pane.fill = False
        self.ax.zaxis.pane.fill = False

        # Embed the Matplotlib figure in the Tkinter canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        plt.close()

        # Add the Matplotlib toolbar
        toolbar_frame = ttk.Frame(self)
        toolbar_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
        toolbar = NavigationToolbar2Tk(self.canvas, toolbar_frame)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create a button to update the plot
        self.update_button = ttk.Button(self, text="Close", command=self.change_plot, width=10)
        self.update_button.pack(side=tk.BOTTOM)

    def change_plot(self):
        # Update the plot with new data
        self.destroy()




if __name__ == "__main__":
    app = Graph_Frame2D()
    app.protocol("WM_DELETE_WINDOW", app.close)
    app.mainloop()