import pathlib
import pygubu
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "nameBrowserApp.ui"


class NamebrowserappApp:
    def __init__(self, master=None):
        # build ui
        self.topFrame = ttk.Frame(master)
        self.controlFrame = ttk.Frame(self.topFrame)
        self.nameLabel = ttk.Label(self.controlFrame)
        self.nameLabel.configure(text='Name:', width='7')
        self.nameLabel.grid(column='0', row='0', sticky='w')
        self.nameEntry = ttk.Entry(self.controlFrame)
        self.nameEntry.configure(font='TkDefaultFont', width='20')
        _text_ = '''John'''
        self.nameEntry.delete('0', 'end')
        self.nameEntry.insert('0', _text_)
        self.nameEntry.grid(column='1', row='0', sticky='w')
        self.nameEntry.bind('<KeyRelease>', self.nameEntered, add='')
        self.genderLabel = ttk.Label(self.controlFrame)
        self.genderLabel.configure(text='Gender: ', width='8')
        self.genderLabel.grid(column='2', row='0', sticky='w')
        self.genderCombo = ttk.Combobox(self.controlFrame)
        self.genderCombo.configure(width='8')
        self.genderCombo.grid(column='3', row='0', sticky='w')
        self.genderCombo.bind('<<ComboboxSelected>>', self.genderSelected, add='')
        self.controlFrame.configure(height='200', padding='0 0 600 0', width='1000')
        self.controlFrame.grid(column='0', padx='5', pady='5', row='0', sticky='w')
        self.tableBar = ttk.Frame(self.topFrame)
        self.tableView = ttk.Treeview(self.tableBar)
        self.tableView.grid(column='0', row='0', sticky='nsew')
        self.tableBar.configure(height='200', padding='0 0 0 5', width='1000')
        self.tableBar.grid(column='0', padx='5', row='1', sticky='nsew')
        self.tableBar.rowconfigure('0', weight='1')
        self.tableBar.columnconfigure('0', weight='1')
        self.topFrame.configure(height='200', width='1000')
        self.topFrame.grid(column='0', row='0', sticky='nsew')
        self.topFrame.rowconfigure('1', weight='1')
        self.topFrame.columnconfigure('0', weight='1')

        # Main widget
        self.mainwindow = self.topFrame
    
    def run(self):
        self.mainwindow.mainloop()

    def (self, event=None):
        pass

    def nameEntered(self, event=None):
        pass

    def genderSelected(self, event=None):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    app = NamebrowserappApp(root)
    app.run()


