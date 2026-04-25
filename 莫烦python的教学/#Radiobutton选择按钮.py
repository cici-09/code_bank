#Radiobutton选择按钮
import tkinter as tk

windows = tk.Tk()            #创建窗口
windows.title("my window")   #窗口名称
windows.geometry("400x300")  #窗口大小


var = tk.StringVar()
l = tk.Label(windows,bg='yellow',width=16,text = 'empty')
l.pack()

def print_selection():
    l.config(text = 'you have select ' + var.get())


r1 = tk.Radiobutton(windows,text='Option B',
                    variable = var ,value='B',
                    command = print_selection)
r1.pack()
r2 = tk.Radiobutton(windows,text='Option C',
                    variable = var ,value='C',
                    command = print_selection)
r2.pack()
r3 = tk.Radiobutton(windows,text='Option A',
                    variable = var ,value='A',
                    command = print_selection)
r3.pack()



windows.mainloop()