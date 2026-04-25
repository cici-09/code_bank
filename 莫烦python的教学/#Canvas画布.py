#Canvas画布
import tkinter as tk
from PIL import ImageTk,Image

window = tk.Tk()
window.title('my window')
window.geometry("400x300")

canvas = tk.Canvas(window,bg='white',height=100,width=200)       #注意这里canvas只能读取gif格式的图片
im = Image.open("C:\\Users\\15397\\Pictures\\MIUI03.jpg")        #但是配合使用PIL库则可以使用png格式的图片
im = im.resize((100,100),Image.Resampling.LANCZOS)
image_file = ImageTk.PhotoImage(im)
image = canvas.create_image(0,0,anchor = 'nw',image=image_file)
x0,y0,x1,y1 = 50,50,80,80
line = canvas.create_line(x0,y0,x1,y1)
oval = canvas.create_oval(x0,y0,x1,y1,fill='red')
canvas.pack()

def off_it():
    canvas.move(oval,0,2)

def up_it():
    canvas.move(oval,0,-2)

b1 = tk.Button(window,text='off',command=off_it)
b1.pack()

b2 = tk.Button(window,text='up',command = up_it )
b2.pack()



window.mainloop()