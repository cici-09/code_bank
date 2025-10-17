#基于tkinter的二项分布计算器
from math import comb
import tkinter as tk


windows = tk.Tk()
windows.title("二项分布计算器")
windows.geometry('800x500')

def binomial_distribution():
    """
    n: 试验次数
    p: 单次试验成功的概率
    k: 成功的次数
    返回值: 成功k次的概率
    """
    n = n_entry.get()
    n = int(n)

    k = k_entry.get()
    k = int(k)

    p = p_entry.get()
    p = float(p)

    answer = comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    answer_text.insert('insert',answer)



n_label = tk.Label(windows,width=50,text='n:')
n_label.place(x=100,y=50)
n_entry = tk.Entry(windows)
n_entry.place(x=300,y=50)

p_label = tk.Label(windows,width=50,text='p:')
p_label.place(x=100,y=100)
p_entry = tk.Entry(windows)
p_entry.place(x=300,y=100)

k_label = tk.Label(windows,width=50,text='k:')
k_label.place(x=100,y=150)
k_entry = tk.Entry(windows)
k_entry.place(x=300,y=150)

answer_label = tk.Label(windows,width=50,text='Answer:')
answer_label.place(x=85,y=250)
answer_text = tk.Text(windows,width=20,height=2)
answer_text.place(x=300,y=250)

b1 = tk.Button(windows,text = 'answer_counter',command=binomial_distribution)
b1.place(x=295,y=200)



windows.mainloop()