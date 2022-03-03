import tkinter as tk

window = tk.Tk()
window.title("calculadora")
window.geometry("500x500")


uzivatel_entry = tk.Entry(
    width=16,
)
uzivatel_entry.grid(column=0,row=0,columnspan=3)
btn_1 = tk.Button(
    text="1",
    width=5,
    height=2,
)
btn_1.grid(column=0, row=1)

btn_2 = tk.Button(
    text="2",
    width=5,
    height=2,
)
btn_2.grid(column=1, row=1)

btn_3 = tk.Button(
    text="3",
    width=5,
    height=2,
)
btn_3.grid(column=2, row=1)

btn_4 = tk.Button(
    text="4",
    width=5,
    height=2,
)
btn_4.grid(column=0, row=2)

btn_5 = tk.Button(
    text="5",
    width=5,
    height=2,
)
btn_5.grid(column=1, row=2)

btn_6 = tk.Button(
    text="6",
    width=5,
    height=2,
)
btn_6.grid(column=2, row=2)

btn_7 = tk.Button(
    text="7",
    width=5,
    height=2,
)
btn_7.grid(column=0, row=3)

btn_8 = tk.Button(
    text="8",
    width=5,
    height=2,
)
btn_8.grid(column=1, row=3)

btn_9 = tk.Button(
    text="9",
    width=5,
    height=2,
)
btn_9.grid(column=2, row=3)

btn_0 = tk.Button(
    text="0",
    width=11,
    height=2,
)
btn_0.grid(column=0, columnspan=2, row=4)
btn_coma = tk.Button(
    text=",",
    width=5,
    height=2,
)
btn_coma.grid(column=2, row=4)


window.mainloop()