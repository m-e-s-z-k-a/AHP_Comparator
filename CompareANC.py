import tkinter

from CompareWindow import CompareWindow

class CompareANC:
    def __init__(self, alternatives_matrix):
        self.alternatives = alternatives_matrix

        self._compare_options()

    def _compare_options(self):
        self.options_root = tkinter.Tk()
        self.options_root.geometry('450x800')
        self.options_root.title('Compare ANC')

        label = tkinter.Label(self.options_root, text="Compare ANC", font=("Gill Sans MT", 20))
        label.grid(row=0, column=0)

        submitButton = tkinter.Button(self.options_root, text="Next", font=("Gill Sans MT", 16),
                                      command=self._compare_hp)
        submitButton.grid(row=0, column=1)

        self.options_root.mainloop()









