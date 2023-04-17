from tkinter import *


def calc():
    mile = float(miles_input.get())
    km = round(mile * 1.609)
    kilometer_result.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)
miles = miles_input.get()

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

kilometer_result = Label(text=0)
kilometer_result.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calc)
calculate_button.grid(column=1, row=2)


window.mainloop()
