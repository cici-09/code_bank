#messagebox弹窗
import tkinter as tk
from tkinter import messagebox
#注意老版本是用tk.messagebox，而新版本则是可以直接messagebox.

window = tk.Tk()
window.title('my window')
window.geometry('400x300')

def hit_me():
    #messagebox.showinfo(title='Hi',message='hahahhaha')          #show弹窗有三种形式，分别是showinfo提醒，showwarning警告，以及showerror报错
    #messagebox.showwarning(title = 'hi',message='nonononon')     #每种弹窗有不同的图标
    #messagebox.showerror(title='Hi',message="It is a error")
    print(messagebox.askquestion(title='Hi',message='hahahaha'))  #ask弹窗则是询问窗口，可以返回值 True 或者 false

tk.Button(window,text='hit me',command=hit_me).pack()


window.mainloop()