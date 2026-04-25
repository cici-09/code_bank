#checkbutton勾选项
import tkinter as tk

windows = tk.Tk()            #创建窗口
windows.title("my window")   #窗口名称
windows.geometry("400x300")  #窗口大小



l = tk.Label(windows,bg='yellow',width=16,text = 'empty')
l.pack()

def print_selection():
    if (var1.get()==1) and (var2.get()==0):
        l.config(text='I love only Python')
    elif (var1.get()==0) and (var2.get()==1):
        l.config(text='I love only C++')
    elif (var1.get()==0) and (var2.get()==0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')

var1 = tk.IntVar()
var2 = tk.IntVar()

c1 = tk.Checkbutton(windows,text='Python',variable=var1,onvalue=1,offvalue=0,
                    command = print_selection)
c2 = tk.Checkbutton(windows,text='C++',variable = var2,onvalue=1,offvalue=0,
                    command=print_selection)
c1.pack()
c2.pack()



windows.mainloop()