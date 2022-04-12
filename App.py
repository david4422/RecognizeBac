import tkinter as tk
from tkinter import *
from Blast import details, print_res
import threading

root = Tk()

class App(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.grid()
        self.create_body()

    def create_body(self):
        self.bacteriaEntered = Label(root, text= "Enter tht Bacteria")
        self.bacteriaEntered.grid(row=0,column=2)
        self.bacteria= Entry(root, width= 30, xscrollcommand= 200, borderwidth= 10)
        self.bacteria.grid(row=1,column=2)


        self.seg1Entered = Label(root, text= "Enter the first segment")
        self.seg1Entered.grid(row=1,column=1)
        self.seg1 = Entry(root, width= 30, borderwidth= 10)
        self.seg1.grid(row=2,column=1)


        self.seg2Entered= Label(root, text= "Enter the second segment")
        self.seg2Entered.grid(row=1,column=3)
        self.seg2= Entry(root, width= 30, borderwidth= 10)
        self.seg2.grid(row=2,column=3)

        self.myButton = Button(root, text="Show results", padx=50, pady=20, command=self.res, fg="blue", bg="gray")
        self.myButton.grid(row=3, column=2)

    def handle_error(self, error, top):
        eror = Label(top, text= error)
        eror.grid(row=5, column=2)

    def validate_input(self, input, top):
        allowed_chars = "GTAC"
        is_data_valid = True
        for character in input:
            if character not in allowed_chars:
                is_data_valid = False
                self.handle_error("Please use only the following letters: GATC", top)
        return is_data_valid

    def monitor(self, thread, top):
        if thread.is_alive():
            self.after(100, lambda: self.monitor(thread, top))
        else:
            res = open("blast_BE_isolate.xml", 'r')
            print_res(res, top)

    def handle_details(self, data, top ):
        details_thread = threading.Thread(target=details, args=[data])
        details_thread.start()
        self.monitor(details_thread, top)

    def res(self):
        top = Toplevel()
        data1 = self.seg1.get()
        data2 = self.seg2.get()
        data = data1.upper() + data2.upper()

        is_data_valid = self.validate_input(data, top)

        if is_data_valid:
            self.handle_details(data, top)



app = App(root)
app.mainloop()

