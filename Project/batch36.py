from tkinter import*

# root=Tk()
# root.title("VoteWarica")
# root.iconbitmap ("vote.ico")
# root.geometry('580x580')
# # root.resizable(0,0)
# root.maxsize(width=700,height=600)
# redbutton=Button(root, text='left',fg='green')
# redbutton.pack(side= LEFT)
# greenbutton=Button(root, text='right',fg='black')
# greenbutton.pack(side= RIGHT)
# bluebutton=Button(root, text='top',fg='blue')
# bluebutton.pack(side= TOP)
# blackbutton=Button(root, text='bottom',fg='red')
# blackbutton.pack(side= BOTTOM)
# name= Label(root,text= "Name"). grid(row=2, column=7)
# e1 = Entry(root).grid(row=2, column=8)
# password= Label(root,text="Password"). grid(row=3, column=7)
# e2= Entry(root).grid(row=3, column=8)
# Forget= Label(root,text="Forget Password?"). grid(row=4, column=8)

# Login=Button(root,text="Login"). grid(row=6, column=8)
top=Tk()
top.title("VoteWarica")
top.iconbitmap ("icon.ico")
top.minsize(width=550,height=400)
top.maxsize(width=550,height=400)
top.configure(bg='darkblue')
label= Label(top, text="VoteWarica",font=("Arial Bold",50),fg='white',bg='darkblue').place(x=110,y=60)
name = Label(top, text="Name",fg='white',bg='darkblue').place(x=110,y=140)
password = Label(top, text="Password",fg='white',bg='darkblue').place(x=110,y=180)
login = Button(top, text="LogIn").place(x=140,y=240)
forget = Button(top, text="Forget Password?").place(x=120,y=280)
e1=Entry(top).place(x=110,y=160)
e2=Entry(top).place(x=110,y=200)
mainloop()
