from tkinter import *

window = Tk()
window.title("Converter")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

label1 = Label(text="Miles")
label1.config(padx=30, pady=20)
label2 = Label(text="is equal to")
label2.config(padx=30, pady=20)
label3 = Label(text="Km")
label3.config(padx=30, pady=20)
result_label = Label(text="")
result_label.config(padx=30, pady=20)


def calculate():
    km = float(entry.get()) * 16 / 10
    result_label.config(text=f"{km}")


button = Button(text="Calculate", command=calculate)

entry = Entry()

label1.grid(column=3, row=1)
label2.grid(column=1, row=2)
label3.grid(column=3, row=2)
button.grid(column=2, row=4)
entry.grid(column=2, row=1)
result_label.grid(column=2, row=2)


window.mainloop()
