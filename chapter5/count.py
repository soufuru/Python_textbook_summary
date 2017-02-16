# カウントアプリ
from tkinter import *

#メインウィンドウを作成
root = Tk()
root.title("カウント")
root.geometry("300x300")

number = 0
desc_label = Label(text=str(number))
desc_label.pack()

def count_up():
    global number
    number = number + 1
    global desc_label
    desc_label.text = str(number)

button = Button(
    text = "+",
    command = count_up
)
button.pack()



root.mainloop()
