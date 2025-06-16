'''
An app that converts temperature between F and C

v1: vasic functions that convert temperatures; no validation
'''

from tkinter import *

class Converter:
    '''Set up the GUI'''
    def __init__(self):

        # main window
        self.root = Tk()
        self.root.title("Temperature Converter")

        # container for frames
        self.container = Frame(self.root)
        self.container.grid(row=0, column=0, sticky="nsew")

        # dictionary to hold frames
        self.frames = {}

        self.frames["MainFrame"] = self.create_main_frame()
        self.frames["to_cFrame"] = self.create_to_c_frame()
        self.frames["to_fFrame"] = self.create_to_f_frame()

        # show the initial frame
        self.show_frame("MainFrame")

    def show_frame(self, name):
        '''display the required frame from the dictionary'''
        frame = self.frames[name]
        frame.tkraise() # move the frame to the top of the stack
    
    def create_main_frame(self):
        '''create the home screen of the app'''
        frame = Frame(self.container)

        # main heading
        self.MainFrame = ""

        # buttons: to c and to f
        self.to_c_button = Button(frame, text="to Centigrade", bg="yellow",
                                  font="Verdana 12 bold",
                                  command=lambda: self.show_frame("to_cFrame"))
        
        self.to_f_button = Button(frame, text="to Fahrenheit", bg="purple",
                                  font="Verdana 12 bold",
                                  command=lambda: self.show_frame("to_fFrame"))
        return Frame

def run(self):
    self.root.mainloop()

if __name__ == "__main__":
    app = Converter()
    app.run()
