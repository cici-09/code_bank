import tkinter as tk

windows = tk.Tk()            #创建窗口
windows.title("my window")   #窗口名称
windows.geometry("200x100")  #窗口大小

var = tk.StringVar()         #设置一个变量

l = tk.Label(windows,textvariable = var,bg='green',font=('arial',12),width=15,
             height = 2)                    #这里注意textvariable，其余参数是tk.label自带的，可查文档

l.pack()

on_hit = False               #设置一个旗帜，以便控制hit——me函数

def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set("you hit me")
    else:
        on_hit = False
        var.set("")

b = tk.Button(windows,text = 'hit me', width = 15 ,height = 2,
              command = hit_me)    
b.pack()

windows.mainloop()