from tkinter import *

km = 0

def conv():
    miles = float(miles_input.get())
    km = (miles) * (1.6)
    km_text = Label(text=f"{km}", font=("italic", 40, "bold"))
    km_text.pack()

window = Tk()
window.title("Testing, Attention please!")
window.minsize(width=1000, height=700)

# text
mtkm = Label(text="Miles To Km Converter", font=("Italic", 40, "bold"))
mtkm.pack()

# user input
miles_input = Entry()
miles_input.pack()


# button
conv_btn = Button(text="Convert", command=conv)
conv_btn.pack()


window.mainloop()
