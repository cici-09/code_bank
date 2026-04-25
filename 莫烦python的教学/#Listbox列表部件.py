#Listbox列表部件
import tkinter as tk

windows = tk.Tk()            #创建窗口
windows.title("my window")   #窗口名称
windows.geometry("400x300")  #窗口大小

e = tk.Entry(windows,show="*")                   #创建一个输入框
e.pack()

var1 = tk.StringVar()
l = tk.Label(windows,bg = 'yellow',width = 4,textvariable = var1)  #创建一个黄色标签
l.pack()

def print_selection():                                             #设定一个函数，用来显示选定的数字
    value = lb.get(lb.curselection())
    var1.set(value)
    
b1 = tk.Button(windows,text = 'print selection', width = 15 ,height = 2,
              command = print_selection)    
b1.pack()

var2 = tk.StringVar()
var2.set((11,22,33,44,55))
lb = tk.Listbox(windows, listvariable=var2)   #创建一个列表标签显示var2所存储的值

list_items = [1,2,3,4]

for item in list_items:
    lb.insert('end',item)            #在end的位置插入item

lb.insert(1,'first')                 #在1的位置插入first
lb.insert(2,"second")                #在2的位置插入second
#lb.delete()函数可以删除lb中的值
lb.pack()

windows.mainloop()