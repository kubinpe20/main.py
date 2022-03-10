import tkinter as tk

window = tk.Tk()
window.title("calculadora")
window.geometry("500x500")



def user_input():
    uzivatel_entry.get()
    vysledek = eval(uzivatel_entry.get())
    uzivatel_entry.delete(0, tk.END)
    uzivatel_entry.insert(tk.END, vysledek)
def delete():
    uzivatel_entry.delete(0, tk.END)

def set_text_0():
    uzivatel_entry.insert(tk.END, "1")

def set_text_1():
    uzivatel_entry.insert(tk.END, "2")

def set_text_2():
    uzivatel_entry.insert(tk.END, "3")

def set_text_3():
    uzivatel_entry.insert(tk.END, "4")

def set_text_4():
    uzivatel_entry.insert(tk.END, "5")

def set_text_5():
    uzivatel_entry.insert(tk.END, "6")

def set_text_6():
    uzivatel_entry.insert(tk.END, "7")

def set_text_7():
    uzivatel_entry.insert(tk.END, "8")

def set_text_8():
    uzivatel_entry.insert(tk.END, "9")

def set_text_9():
    uzivatel_entry.insert(tk.END, "0")

def set_text_10():
    uzivatel_entry.insert(tk.END, "/")

def set_text_11():
    uzivatel_entry.insert(tk.END, "*")

def set_text_12():
    uzivatel_entry.insert(tk.END, "+")

def set_text_13():
    uzivatel_entry.insert(tk.END, "-")

def set_text_14():
    uzivatel_entry.insert(tk.END, ",")


uzivatel_entry = tk.Entry(
    width=16,
)
uzivatel_entry.grid(column=0, row=0, columnspan=2)

btn_1 = tk.Button(
    text="1",
    width=5,
    height=2,
    command=set_text_0
)
btn_1.grid(column=0, row=1)

btn_2 = tk.Button(
    text="2",
    width=5,
    height=2,
    command=set_text_1
)
btn_2.grid(column=1, row=1)

btn_3 = tk.Button(
    text="3",
    width=5,
    height=2,
    command=set_text_2
)
btn_3.grid(column=2, row=1)

btn_4 = tk.Button(
    text="4",
    width=5,
    height=2,
    command=set_text_3
)
btn_4.grid(column=0, row=2)

btn_5 = tk.Button(
    text="5",
    width=5,
    height=2,
    command=set_text_4
)
btn_5.grid(column=1, row=2)

btn_6 = tk.Button(
    text="6",
    width=5,
    height=2,
    command=set_text_5
)
btn_6.grid(column=2, row=2)

btn_7 = tk.Button(
    text="7",
    width=5,
    height=2,
    command=set_text_6
)
btn_7.grid(column=0, row=3)

btn_8 = tk.Button(
    text="8",
    width=5,
    height=2,
    command=set_text_7
)
btn_8.grid(column=1, row=3)

btn_9 = tk.Button(
    text="9",
    width=5,
    height=2,
    command=set_text_8
)
btn_9.grid(column=2, row=3)

btn_0 = tk.Button(
    text="0",
    width=12,
    height=2,
    command=set_text_9
)
btn_0.grid(column=0, columnspan=2, row=4)

btn_coma = tk.Button(
    text=",",
    width=5,
    height=2,
    command=set_text_14
)
btn_coma.grid(column=2, row=4)

btn_division = tk.Button(
    text="/",
    width=5,
    height=2,
    command=set_text_10
)
btn_division.grid(column=4, row=1)

btn_multiplication = tk.Button(
    text="*",
    width=5,
    height=2,
    command=set_text_11
)
btn_multiplication.grid(column=4, row=2)

btn_addition = tk.Button(
    text="+",
    width=5,
    height=2,
    command=set_text_12
)
btn_addition.grid(column=4, row=3)

btn_subtraction = tk.Button(
    text="-",
    width=5,
    height=2,
    command=set_text_13
)
btn_subtraction.grid(column=4, row=4)

btn_result = tk.Button(
    text="=",
    width=5,
    height=2,
    command=user_input
)
btn_result.grid(column=5, row=4)

btn_result = tk.Button(
    text="AC",
    width=5,
    height=2,
    command=delete
)
btn_result.grid(column=5, row=1)

window.mainloop()
