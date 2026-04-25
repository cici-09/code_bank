#Entry 和 Text 的运用
#基于上一个文件的改进

import tkinter as tk

windows = tk.Tk()            #创建窗口
windows.title("my window")   #窗口名称
windows.geometry("400x300")  #窗口大小

e = tk.Entry(windows,show="*")                   #创建一个输入框
e.pack()

def insert_point():
    var = e.get()
    t.insert("insert",var)

def insert_end():
    var = e.get()
    t.insert("end",var)

b1 = tk.Button(windows,text = 'insert point', width = 15 ,height = 2,
              command = insert_point)    
b1.pack()

b2 = tk.Button(windows,text = 'insert end',
               command = insert_end)    
b2.pack()

t = tk.Text(windows,height=2)    #创建一个文本框
t.pack()

windows.mainloop()