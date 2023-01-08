import tkinter

from ResultsWindow import ResultsWindow

class AlternativesComparisonWindow:

    def __init__(self, calculations_matrix, alternatives_array):
        self.calculations_matrix = calculations_matrix
        self.alternatives_array = alternatives_array
        self.root = tkinter.Tk()
        self.attribute_index = 0
        self.first_index = 0
        self.second_index = 1
        self.root.geometry('900x300')
        self.root.title("Alternatives comparison")
        self.attributes = ['Wireless', 'Type', 'ANC', 'Price', 'Microphone', 'SPL', 'Impedance']

        frame1 = tkinter.Frame(self.root)
        frame2 = tkinter.Frame(self.root)
        frame3 = tkinter.Frame(self.root)

        self.categories_label = tkinter.Label(frame1, text=self._generate_comparison_text(),
                                              font=("Gill Sans MT", 18))
        self.categories_label.pack()

        self.choice_var = tkinter.StringVar()
        self.choice_var.set("1")

        self.comparison_1st_label = tkinter.Label(frame2, text=self._generate_first_label(),
                                                  font=("Gill Sans MT", 13))
        self.comparison_1st_label.grid(row=0, column=0)
        self.comparison_2nd_label = tkinter.Label(frame2, text=self._generate_second_label(),
                                                  font=("Gill Sans MT", 13))
        self.comparison_2nd_label.grid(row=0, column=18)

        self.comparison_options9left = tkinter.Radiobutton(frame2, text="9", variable=self.choice_var,
                                                           value="1/9").grid(row=0, column=1)
        self.comparison_options8left = tkinter.Radiobutton(frame2, text="8", variable=self.choice_var,
                                                           value="1/8").grid(row=0, column=2)
        self.comparison_options7left = tkinter.Radiobutton(frame2, text="7", variable=self.choice_var,
                                                           value="1/7").grid(row=0, column=3)
        self.comparison_options6left = tkinter.Radiobutton(frame2, text="6", variable=self.choice_var,
                                                           value="1/6").grid(row=0, column=4)
        self.comparison_options5left = tkinter.Radiobutton(frame2, text="5", variable=self.choice_var,
                                                           value="1/5").grid(row=0, column=5)
        self.comparison_options4left = tkinter.Radiobutton(frame2, text="4", variable=self.choice_var,
                                                           value="1/4").grid(row=0, column=6)
        self.comparison_options3left = tkinter.Radiobutton(frame2, text="3", variable=self.choice_var,
                                                           value="1/3").grid(row=0, column=7)
        self.comparison_options2left = tkinter.Radiobutton(frame2, text="2", variable=self.choice_var,
                                                           value="1/2").grid(row=0, column=8)
        self.comparison_options1 = tkinter.Radiobutton(frame2, text="1", variable=self.choice_var,
                                                       value="1").grid(row=0, column=9)
        self.comparison_options2right = tkinter.Radiobutton(frame2, text="2", variable=self.choice_var,
                                                            value="2").grid(row=0, column=10)
        self.comparison_options3right = tkinter.Radiobutton(frame2, text="3", variable=self.choice_var,
                                                            value="3").grid(row=0, column=11)
        self.comparison_options4right = tkinter.Radiobutton(frame2, text="4", variable=self.choice_var,
                                                            value="4").grid(row=0, column=12)
        self.comparison_options5right = tkinter.Radiobutton(frame2, text="5", variable=self.choice_var,
                                                            value="5").grid(row=0, column=13)
        self.comparison_options6right = tkinter.Radiobutton(frame2, text="6", variable=self.choice_var,
                                                            value="6").grid(row=0, column=14)
        self.comparison_options7right = tkinter.Radiobutton(frame2, text="7", variable=self.choice_var,
                                                            value="7").grid(row=0, column=15)
        self.comparison_options8right = tkinter.Radiobutton(frame2, text="8", variable=self.choice_var,
                                                            value="8").grid(row=0, column=16)
        self.comparison_options9right = tkinter.Radiobutton(frame2, text="9", variable=self.choice_var,
                                                            value="9").grid(row=0, column=17)

        self.next_button = tkinter.Button(frame3, text="Next", font=("Gill Sans MT", 15), command=self._submit)
        self.next_button.grid(row=1, columnspan=17)

        frame1.pack(side=tkinter.TOP, pady=10)
        frame2.pack(side=tkinter.TOP, pady=10)
        frame3.pack(side=tkinter.TOP, pady=10)

    def _generate_comparison_text(self):
        return "Compare alternatives based on... " + self.attributes[self.attribute_index]

    def _generate_first_label(self):
        return self.alternatives_array[self.first_index][0] + \
               " (" + self.alternatives_array[self.first_index][self.attribute_index+1]+ ")"

    def _generate_second_label(self):
        return self.alternatives_array[self.second_index][0] + \
               " (" + self.alternatives_array[self.second_index][self.attribute_index+1] + ")"

    def _get_chosen_value(self):
        text = self.choice_var.get()
        if '/' in text:
            numerator, denominator = text.split('/')
            return int(numerator) / int(denominator)
        return int(text)

    def _move_to_results_window(self):
        self.root.destroy()
        ResultsWindow(self.calculations_matrix, self.alternatives_array)

    def _submit(self):
        val = self._get_chosen_value()

        self.calculations_matrix[self.attributes[self.attribute_index]][self.first_index][self.second_index] = 1 / val
        self.calculations_matrix[self.attributes[self.attribute_index]][self.second_index][self.first_index] = val

        self.second_index += 1
        if self.second_index == len(self.alternatives_array):
            self.first_index += 1
            self.second_index = self.first_index + 1

        if self.first_index >= len(self.alternatives_array) - 1:
            self.attribute_index += 1
            self.first_index = 0
            self.second_index = 1

        if self.attribute_index >= len(self.attributes):
            self._move_to_results_window()
            return

        self.choice_var.set("1")
        self.categories_label.config(text=self._generate_comparison_text())
        self.comparison_1st_label.config(text=self._generate_first_label())
        self.comparison_2nd_label.config(text=self._generate_second_label())

    def run(self):
        self.root.mainloop()
