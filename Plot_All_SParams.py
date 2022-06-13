import skrf as rf
import tkinter as tk
import tkinter.filedialog as fd
import matplotlib.pyplot as plt


# Tutorials for scikit-rf
# https://scikit-rf.readthedocs.io/en/latest/tutorials/index.html

def Main():
    print('Please select the S Parameter file(s) you\'d like to plot')
    try:
        filenames = Gui_file_path()
        linetypes = ['-','--','-.',':']

        for linetype,file in zip(linetypes,filenames):
            network = rf.Network(file)
            network.plot_s_db(linestyle=linetype)
            plt.show(block=False)

        input('\nPress enter to exit')       

    except Exception as e:
        print("Exception: ", e)


def Gui_file_path():
    root = tk.Tk()
    root.withdraw()
    filenames = fd.askopenfilenames(parent=root, title='Choose your file(s)')
    return filenames    


if __name__ == '__main__':
    Main()