#Scale尺度
import tkinter as tk

windows = tk.Tk()            #创建窗口
windows.title("my window")   #窗口名称
windows.geometry("400x300")  #窗口大小



l = tk.Label(windows,bg='yellow',width=16,text = 'empty')
l.pack()

def print_selection(v):
    l.config(text = 'you have select ' + v)

s = tk.Scale(windows,label='try me',from_=5,to=11,orient=tk.HORIZONTAL,
             length = 200,showvalue = 0,tickinterval=1,resolution=0.1,
              command = print_selection)
s.pack()


windows.mainloop()