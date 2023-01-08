import tkinter

from CalculationsClass import CalculationsClass
from ConsistencyWindow import ConsistencyWindow

class ResultsWindow:

    def __init__(self, calculations_matrix, alternatives_array):
        self.calculations_matrix = calculations_matrix
        self.alternatives_array = alternatives_array
        self.root = tkinter.Tk()
        self.root.geometry('800x600')
        self.root['bg'] = '#f48fb1'
        self.root.title("Results")


        self.results, self.consistencies = CalculationsClass(alternatives_array, calculations_matrix).comparison()

        results_text = ""
        for hp in self.results:
            results_text += hp[1]
            results_text += '\n'


        frame1 = tkinter.Frame(self.root)
        frame2 = tkinter.Frame(self.root)
        frame3 = tkinter.Frame(self.root)

        self.title_label = tkinter.Label(frame1, text='RESULTS', font=("Gill Sans MT", 32), bg='#f48fb1', pady=20, width=600)
        self.title_label.pack()
        self.ranking_label = tkinter.Label(frame2, text=results_text, font=("Gill Sans MT", 20), bg='#f48fb1', width=600)
        self.ranking_label.pack()
        self.consistency_button = tkinter.Button(frame3, text="Show consistency ratios", command=self._open_consistency_window, font=("Gill Sans MT", 20))
        self.consistency_button.pack()

        frame1.pack(side=tkinter.TOP, pady=10)
        frame2.pack(side=tkinter.TOP, pady=10)
        frame3.pack(side=tkinter.TOP, pady=10)

    def _open_consistency_window(self):
        self.root.destroy()
        ConsistencyWindow(self.consistencies)

    def run(self):
        self.root.mainloop()