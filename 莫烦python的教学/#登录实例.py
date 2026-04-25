#登录实例
import tkinter as tk 
import pickle
from PIL import ImageTk,Image
from tkinter import messagebox

window = tk.Tk()
window.title('qq登录系统模拟')
window.geometry('450x300')

#canvas
canvas = tk.Canvas(window,bg='white',height=200,width=500)      
im = Image.open("C:\\Users\\15397\\Pictures\\MIUI03.jpg")       
im = im.resize((450,100),Image.Resampling.LANCZOS)
image_file = ImageTk.PhotoImage(im)
image = canvas.create_image(0,0,anchor = 'nw',image=image_file)
canvas.pack(side='top')

#定义自由变量
var_user_name = tk.StringVar()
var_user_name.set('example@python.com')
var_user_pwd = tk.StringVar()

#设置账号标签和密码标签
Uer_l = tk.Label(window,text="User name").place(x=50,y=150)
psw_l = tk.Label(window,text="Password").place(x=50,y=190)

#设置账号输入框和密码输入框
entry_user_name = tk.Entry(window,textvariable=var_user_name)
entry_user_name.place(x = 160,y=150)

entry_user_pwd = tk.Entry(window,textvariable=var_user_pwd,show='*')
entry_user_pwd.place(x=160,y=190)

def user_login():
    user_name = var_user_name.get()
    user_pwd = var_user_pwd.get()
    try:
        with open('users_info.pickle','rb') as user_file:
            users_info = pickle.loads(user_file)
    except FileNotFoundError:
        with open('users_info.pickle','wb') as user_file:
            users_info = {'admin':'admin'}
            pickle.dump(users_info,user_file)
    
    if user_name in users_info:
        if user_pwd == users_info[user_name]:
            messagebox.showinfo(title = 'Welcome',message = 'How are you?' + user_name)
        else:
            messagebox.showerror(message = 'Error,your password is wrong,please try again.')
    else:
        is_sign_up = messagebox.askyesno('Welcome','You have not sign up yet.Sign up today')

    if is_sign_up:
        user_sign_up()



def user_sign_up():

    def sign_to_Lijin_Python():
        np = new_pwd.get()
        npf = new_pwd_confirm.get()
        nn = new_name.get()
        with open('users_info.pickle','rb') as user_file:
            exist_user_info = pickle.load(user_file)
        if np != npf :
            messagebox.showerror('Error','Password and confirm password must be the same!')
        elif nn in exist_user_info:
            messagebox.showerror('Error','The user has already signed up!')
        else:
            exist_user_info[nn] = np
            with open('users_info.pickle','wb') as user_file:
                pickle.dump(exist_user_info,user_file)
            messagebox.showinfo('Welcome','You have successfully signed uo! ')
            window_sign_up.destroy()


    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    new_name.set('example@python.com')
    tk.Label(window_sign_up,text = 'Users name:').place(x=10,y=10)
    entry_new_name = tk.Entry(window_sign_up,textvariable=new_name)
    entry_new_name.place(x=150,y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up,text='Password:').place(x=10,y=50)
    entry_user_pwd =tk.Entry(window_sign_up,textvariable=new_pwd,show='*')
    entry_user_pwd.place(x=150,y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up,text='Confirm password:').place(x=10,y=90)
    entry_new_pwd_confirm = tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show='*')
    entry_new_pwd_confirm.place(x=150,y=90)

    btn_confirm_sign_up = tk.Button(window_sign_up,text='Sign up',command = sign_to_Lijin_Python)
    btn_confirm_sign_up.place(x=150,y=130)


#login and sign up button
btn_login = tk.Button(window,text='Login',command = user_login)
btn_login.place(x=170,y=230)
btn_sign_up = tk.Button(window,text='sign up',command=user_sign_up)
btn_sign_up.place(x=270,y=230)


window.mainloop()