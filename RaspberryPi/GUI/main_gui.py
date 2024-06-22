import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import tkinter as tk
from GUI.start_gui import StartPage
from GUI.calculator_gui import Calculator_Frame
from GUI.grapher_gui import Graph_Frame2D, Graph_Frame3D, Graph_GUI
from GUI.simul_gui import Simultaneous_solver_Frame, Simultaneous_Frame
# from GUI.pdf_reader_GUI import PDFReader
from GUI.whiteboard_GUI import WhiteboardApp
from GUI.controls_gui import TransferFunctionFrame
from GUI.matrix_solver_gui import  MatrixOperationPage
if sys.platform == "linux":
    from GUI.cam_GUI import CameraApp
from GUI.loading_gui import Loading_GUI

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Multiple Frames Example")
        self.attributes('-fullscreen', True)

        self.configure(bg="#293C4A")

        self.container = tk.Frame(self)
        self.container.pack(fill="both")

        self.frames = {}
        self.current_frame = None

        self.show_frame("StartPage")

    def add_frame(self, frame_class, data=None):
        frame = frame_class(self.container, self, data) if data else frame_class(self.container, self)
        self.frames[frame_class.__name__] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, name, data=None):
        print(f"Switching to frame: {name}")
        if self.current_frame and self.current_frame != "StartPage":
            self.frames[self.current_frame].grid_remove()

        if name in self.frames:
            # Frame already exists, so just show it
            self.current_frame = name
            self.frames[name].grid()
        else:
            # Frame doesn't exist, create it and add to frames dictionary
            frame_class = globals()[name]
            self.add_frame(frame_class, data)
            self.current_frame = name

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()