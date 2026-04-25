#Menubar菜单
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry("400x300")

l = tk.Label(window,text='',bg='yellow')
l.pack()

counter = 0
def do_job():
    global counter
    l.config(text='do'+ str(counter))
    counter += 1

menubar = tk.Menu(window)
filemenu = tk.Menu(menubar,tearoff = 0)
menubar.add_cascade(label='File',menu=filemenu)

filemenu.add_command(label='New',command = do_job)

filemenu.add_cascade(label='New',command=do_job)
filemenu.add_cascade(label="Open",command =do_job )
filemenu.add_cascade(label = 'Save',command = do_job)

filemenu.add_separator()
filemenu.add_cascade(label='Exit',command= window.quit)

window.config(menu = menubar)

window.mainloop()