import tkinter

class ConsistencyWindow:

    def __init__(self, consistencies):
        self.consistencies = consistencies
        self.root = tkinter.Tk()
        self.root.geometry('800x600')
        self.root['bg'] = '#f48fb1'
        self.root.title("Consistencies")

        results_text = ""
        for key, value in self.consistencies.items():
            results_text += key
            results_text += ": "
            results_text += str(value)
            results_text += '\n'

        frame1 = tkinter.Frame(self.root)
        frame2 = tkinter.Frame(self.root)

        self.title_label = tkinter.Label(frame1, text='CONSISTENCIES', font=("Gill Sans MT", 32), bg='#f48fb1', pady=20,
                                         width=600)
        self.title_label.pack()
        self.ranking_label = tkinter.Label(frame2, text=results_text, font=("Gill Sans MT", 20), bg='#f48fb1',
                                           width=600)
        self.ranking_label.pack()

        frame1.pack(side=tkinter.TOP, pady=10)
        frame2.pack(side=tkinter.TOP, pady=10)

    def run(self):
        self.root.mainloop()
