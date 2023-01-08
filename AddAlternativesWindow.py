import tkinter

from CategoriesComparisonWindow import CategoriesComparisonWindow

class AddAlternativesWindow:

    def __init__(self, calculations_matrix, alternatives_array):
        self.calculations_matrix = calculations_matrix
        self.alternatives_array = alternatives_array
        self.root = tkinter.Tk()
        self.root.geometry('800x600')
        self.root.title('Headphones')
        self.attributes = ['Wireless', 'Type', 'ANC', 'Price', 'Microphone', 'SPL', 'Impedance']
        self.root['bg'] = '#f48fb1'
        frame = tkinter.Frame(self.root)

        temp = ''
        for hp in self.alternatives_array:
            temp += hp[0]
            temp += '\n'
        if temp == '':
            temp = "No headphones added"

        label = tkinter.Label(frame, text='HEADPHONES', font=("Gill Sans MT", 32), bg='#f48fb1', pady=20, width=600)
        label.pack()

        self.headphones_label = tkinter.Label(frame, text=temp, font=("Gill Sans MT", 28), bg='#f48fb1', width=600)
        self.headphones_label.pack()

        finishButton = tkinter.Button(text="Finish", font=("Gill Sans MT", 20), command=self._finish_adding)
        finishButton.pack(side=tkinter.BOTTOM, pady=20)

        addButton = tkinter.Button(text="Add new headphones", command=self._open_adding_window, font=("Gill Sans MT", 20))
        addButton.pack(side=tkinter.BOTTOM)

        frame.pack(side=tkinter.TOP)

    def _submit(self):
        name = self.name_txt.get("1.0", "end-1c")
        wireless = self.wireless_txt.get("1.0", "end-1c")
        type = self.type_txt.get("1.0", "end-1c")
        anc = self.anc_txt.get("1.0", "end-1c")
        price = self.price_txt.get("1.0", "end-1c")
        micro = self.micro_txt.get("1.0", "end-1c")
        spl = self.spl_txt.get("1.0", "end-1c")
        impedance = self.impedance_txt.get("1.0", "end-1c")

        hp_array = [name, wireless, type, anc, price, micro, spl, impedance]

        temp = ''
        for hp in self.alternatives_array:
            temp += hp[0]
            temp += '\n'

        self.headphones_label.config(text=temp)
        self.root_add.destroy()

    def _open_adding_window(self):
        self.root_add = tkinter.Tk()
        self.root_add.geometry('600x800')
        self.root_add.title('Headphones')

        frame = tkinter.Frame(self.root_add)
        frame.pack(side=tkinter.TOP)

        label = tkinter.Label(frame, text='Fill below parameters:', font=("Gill Sans MT", 28))
        label.pack()

        self.name_label = tkinter.Label(frame, text="Name", font=("Gill Sans MT", 20))
        self.name_label.pack()
        self.name_txt = tkinter.Text(frame, height=1, width=20, font=("Gill Sans MT", 14))
        self.name_txt.pack()

        self.wireless_label = tkinter.Label(frame, text="Wireless ('yes' or 'no')", font=("Gill Sans MT", 20))
        self.wireless_label.pack()
        self.wireless_txt = tkinter.Text(frame, height=1, width=20, font=("Gill Sans MT", 14))
        self.wireless_txt.pack()

        self.type_label = tkinter.Label(frame, text="Type ('headphones', 'earphones' or 'in-ear')",
                                        font=("Gill Sans MT", 20))
        self.type_label.pack()
        self.type_txt = tkinter.Text(frame, height=1, width=20, font=("Gill Sans MT", 14))
        self.type_txt.pack()

        self.anc_label = tkinter.Label(frame, text="Active Noise Cancellation ('yes' or 'no')",
                                       font=("Gill Sans MT", 20))
        self.anc_label.pack()
        self.anc_txt = tkinter.Text(frame, height=1, width=20, font=("Gill Sans MT", 14))
        self.anc_txt.pack()

        self.price_label = tkinter.Label(frame, text="Price", font=("Gill Sans MT", 20))
        self.price_label.pack()
        self.price_txt = tkinter.Text(frame, height=1, width=20, font=("Gill Sans MT", 14))
        self.price_txt.pack()

        self.micro_label = tkinter.Label(frame, text="Microphone ('yes' or 'no')", font=("Gill Sans MT", 20))
        self.micro_label.pack()
        self.micro_txt = tkinter.Text(frame, height=1, width=20, font=("Gill Sans MT", 14))
        self.micro_txt.pack()

        self.spl_label = tkinter.Label(frame, text="SPL (dB)", font=("Gill Sans MT", 20))
        self.spl_label.pack()
        self.spl_txt = tkinter.Text(frame, height=1, width=20, font=("Gill Sans MT", 14))
        self.spl_txt.pack()

        self.impedance_label = tkinter.Label(frame, text="Impedance", font=("Gill Sans MT", 20))
        self.impedance_label.pack()
        self.impedance_txt = tkinter.Text(frame, height=1, width=20, font=("Gill Sans MT", 14))
        self.impedance_txt.pack()

        submitButton = tkinter.Button(frame, text="OK", font=("Gill Sans MT", 20), command=self._submit)
        submitButton.pack(side=tkinter.BOTTOM, pady=20)

        self.root_add.mainloop()

    def _prepare_calculations_matrix(self):
        number_of_options = len(self.alternatives_array)
        for attribute in self.attributes:
            self.calculations_matrix[attribute] = [[1 for i in range (number_of_options)] for j in range (number_of_options)]
        self.calculations_matrix["criteria_between_eo"] = [[1 for i in range(len(self.attributes))] for j in range(len(self.attributes))]

    def _finish_adding(self):
        self._prepare_calculations_matrix()
        self.root.destroy()
        CategoriesComparisonWindow(self.calculations_matrix, self.alternatives_array,)

    def run(self):
        self.root.mainloop()

