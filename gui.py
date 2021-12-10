import tkinter
from tkinter import ttk


class GridGm:

    def __init__(self, master):

        master.title('PyMeet2020')
        self.label_1 = ttk.Label(master, text="what's your name", background='light blue').grid(row=0, sticky='e', padx=5, pady=5)
        self.label_2 = ttk.Label(master, text="your email", background="olive").grid(row=1, sticky='e', padx=5, pady=5)
        self.label_3 = ttk.Label(master, text="programming language", background="orange").grid(row=2, sticky='e', padx=5, pady=5)

        self.entry_1 = ttk.Entry(master).grid(row=0,column=1, padx=5, pady=5, sticky='ew', columnspan=3)
        self.entry_2 = ttk.Entry(master).grid(row=1,column=1, padx=5, pady=5, sticky='ew', columnspan=3)
        self.entry_3 = ttk.Entry(master).grid(row=2,column=1, padx=5, pady=5, sticky='ew', columnspan=3)

        self.text_1 = tkinter.Text(master, width=30, height=5).grid(row=3, column=1, padx=5, pady=5, columnspan=3)

        self.button_1 = ttk.Button(text="reserve now").grid(row=4, column=1, sticky='w')
        self.check_1 = ttk.Checkbutton(text="arriving early").grid(row=4, column=2, padx=5, pady=5)
        self.check_2 = ttk.Checkbutton(text="need breakfast").grid(row=4, column=3, padx=5, pady=5)



if __name__ == '__main__':
    master = tkinter.Tk()
    GridGm(master)
    master.mainloop()

