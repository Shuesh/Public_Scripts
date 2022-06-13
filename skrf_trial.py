import skrf as rf
import tkinter as tk
import tkinter.filedialog as fd
import matplotlib.pyplot as plt



def Main():
    print('Please select the S Parameter file(s) you\'d like to plot')
    filenames = Gui_file_path()
    linetypes = ['-','--','-.',':']



def Gui_file_path():
    root = tk.Tk()
    root.withdraw()
    filenames = fd.askopenfilenames(parent=root, title='Choose your file(s)')
    return filenames    



if __name__ == '__main__':
    Main()