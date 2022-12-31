import tkinter


class CompareWindow:
    def __init__(self, alternatives_matrix):
        self.alternatives = alternatives_matrix
        self.attributes_num = [0, 1, 2, 3, 4, 5, 6]
        self.attributes = ['Wireless', 'Type', 'ANC', 'Microphone', 'Price', 'SPL', 'Impedance']

        self._compare_attributes()

    def _compare_attributes(self):
        self.attributes_root = tkinter.Tk()
        self.attributes_root.geometry('450x800')
        self.attributes_root.title('Compare Attributes')

        label = tkinter.Label(self.attributes_root, text="Compare attributes", font=("Gill Sans MT", 20))
        label.grid(row=0, column=0)

        submitButton = tkinter.Button(self.attributes_root, text="Next", font=("Gill Sans MT", 16),
                                      command=self._compare_hp)
        submitButton.grid(row=0, column=1)

        self.matrix_attributes = [[1 for _ in range(7)] for _ in range(7)]

        res = [(a, b) for idx, a in enumerate(self.attributes_num) for b in self.attributes_num[idx + 1:]]

        i = 1

        self.textbox_arr = []

        for el in res:
            label1 = tkinter.Label(self.attributes_root, text=self.attributes[el[0]] + " / " + self.attributes[el[1]],
                                   font=("Gill Sans MT", 15))
            label1.grid(column=0, row=i)

            text1 = tkinter.Text(self.attributes_root, height=1, width=20, font=("Gill Sans MT", 14))
            self.textbox_arr.append((text1, el))
            self.textbox_arr[len(self.textbox_arr) - 1][0].grid(column=1, row=i)

            i += 1

        self.attributes_root.mainloop()

    def _compare_hp(self):
        for t in self.textbox_arr:
            self.matrix_attributes[t[1][0]][t[1][1]] = float(t[0].get("1.0", "end-1c"))
            self.matrix_attributes[t[1][1]][t[1][0]] = 1 / float(t[0].get("1.0", "end-1c"))

        print(self.matrix_attributes)

        self.attributes_root.destroy()

        self.root_wireless = tkinter.Tk()
        self.root_wireless.geometry('600x800')
        self.root_wireless.title('Wireless')

        frame = tkinter.Frame(self.root_wireless)
        frame.pack(side=tkinter.TOP)

        label = tkinter.Label(frame, text='Fill below parameters:', font=("Gill Sans MT", 28))
        label.pack()

        self.root_wireless.mainloop()


CompareWindow([['SONY', 'no', 'earphones', 'no', '123', 'no', '10', '20'],
               ['JBL', 'no', 'earphones', 'no', '400', 'no', '15', '5'],
               ['Other', 'yes', 'in-ear', 'no', '200', 'no', '20', '10']])
