import tkinter as tk

root = tk.Tk()
root.title("Calculadora")
root.geometry("500x300")

label_1 = tk.Label(root, text="Põe um numero ai")
label_1.pack(pady=20)

number_1 = tk.Entry(root)
number_1.pack(pady=20)

label_2 = tk.Label(root, text="Põe outro numero ai")
label_2.pack(pady=20)

number_2 = tk.Entry(root)
number_2.pack(pady=20)

label_3 = tk.Label(root, text="")
label_3.pack(pady=20)


def adicionar():
    res = int(number_1.get()) + int(number_2.get())
    label_3.config(text=res)


def subtrair():
    res = int(number_1.get()) - int(number_2.get())
    label_3.config(text=res)


def multiplicar():
    res = int(number_1.get()) * int(number_2.get())
    label_3.config(text=res)


def dividir():
    res = int(number_1.get()) / int(number_2.get())
    label_3.config(text=res)


button_4 = tk.Button(root, text="Adicionar", command=adicionar)
button_3 = tk.Button(root, text="Subtrair", command=subtrair)
button_2 = tk.Button(root, text="Multiplicar", command=multiplicar)
button_1 = tk.Button(root, text="Dividir", command=dividir)
button_1.pack(pady=10)
button_2.pack(pady=10)
button_3.pack(pady=10)
button_4.pack(pady=10)

root.mainloop()