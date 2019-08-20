import tkinter.messagebox as mb
from tkinter import *


def say_result():
    import random

    fortune = ["大吉", "中吉", "小吉", "末吉", "吉", "凶", "大凶"]
    mb.showinfo("おみくじ", random.choice(fortune))


root = Tk()
root.title("おみくじ")
root.geometry("190x150")

desc_label = Label(text="下のボタンを押してください！")
desc_label.pack()

fortune_button = Button(
    text="おみくじを引く", width=10, height=4, command=say_result, bg="#f0e68c"
)
fortune_button.pack()

root.mainloop()
