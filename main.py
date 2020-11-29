import tkinter as tk
import mysql.connector as connector
from tkinter import messagebox

class homeWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master,bg='pale turquoise')
        self.label1 = tk.Label(self.frame, text='Create a new account or log in', bg='DeepSkyBlue2', font="Helvetica 16 italic bold", relief='groove',pady=10)
        self.label1.grid(padx=70,pady=30)
        self.button1 = tk.Button(self.frame, text='Sign in', bg='sky blue', font=['fixedsys',17,], borderwidth=5, command=self.sign_in)
        self.button1.grid(row=1,padx=75, pady=15)
        self.button2 = tk.Button(self.frame, text='Sign up', bg='sky blue', font=['fixedsys',17], borderwidth=5, command=self.sign_up)
        self.button2.grid(row=2,padx=75)
        self.frame.grid()

    def sign_in(self):
        self.newWindow = tk.Toplevel(self.master,bg='pale turquoise', relief='sunk', borderwidth=5)
        positionRight = int(self.newWindow.winfo_screenwidth()/2 - 525/2)
        positionDown = int(self.newWindow.winfo_screenheight()/2 - 350/2)
        self.newWindow.title('Sign in')
        self.newWindow.geometry("450x300")
        self.newWindow.geometry("+{}+{}".format(positionRight, positionDown))
        self.app = loginWindow(self.newWindow)

    def sign_up(self):
        self.newWindow = tk.Toplevel(self.master,bg='pale turquoise', relief='sunk', borderwidth=5)
        positionRight = int(self.newWindow.winfo_screenwidth()/2 - 525/2)
        positionDown = int(self.newWindow.winfo_screenheight()/2 - 350/2)
        self.newWindow.title('Sign up')
        self.newWindow.geometry("450x300")
        self.newWindow.geometry("+{}+{}".format(positionRight, positionDown))
        self.app = registerWindow(self.newWindow)

class loginWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.configure(bg='pale turquoise')
        self.label1 = tk.Label(self.frame, text='Sign in', bg='DeepSkyBlue2', font="Helvetica 18 italic bold",pady=10,relief='groove',padx=5)
        self.label2 = tk.Label(self.frame, text='Username', bg='sky blue', font=['fixedsys',17],relief='groove',pady=4)
        self.label3 = tk.Label(self.frame, text='Password', bg='sky blue', font=['fixedsys',17],relief='groove',pady=4)
        self.entry1 = tk.Entry(self.frame, relief='groove',font=('Helvetica 16'))
        self.entry2 = tk.Entry(self.frame, relief='groove',font=('Helvetica 16'))
        self.button1 = tk.Button(self.frame,borderwidth=3,text='Enter',font='Helvetica 16 bold', bg='sky blue',command=self.login)
        self.button2 = tk.Button(self.frame,borderwidth=3,text='Return',font='Helvetica 16 bold', bg='sky blue',command=self.close)
        self.label1.grid(row=0,pady=25,columnspan=2,padx=170)
        self.label2.grid(pady=10,row=1,column=0,sticky='w',padx=25)
        self.label3.grid(pady=10,row=2,column=0,sticky='w',padx=25)
        self.entry1.grid(row=1,column=1,sticky='w',ipady=7)
        self.entry2.grid(row=2,column=1,sticky='w',ipady=7)
        self.button1.grid(row=3,column=0,sticky='e')
        self.button2.grid(row=3,column=1,sticky='w', padx=20,pady=10)
        self.frame.grid()

    def close(self):
        self.master.destroy()

    def login(self):
        connection = connector.connect(host="localhost", user="root", passwd="password", database="project")
        cursor = connection.cursor()
        cursor.execute("select * from user;")
        db = dict()
        result = cursor.fetchall()
        for entry in result:
            user,passwd = entry
            db[user] = passwd
        username = self.entry1.get()
        password = self.entry2.get()
        if username in db.keys():
            if password == db[username]:
                self.close()
                messagebox.showinfo("Success!","User successfully authenticated!")
            else:
                messagebox.showerror("Error","Incorrect password!")
        else:
            messagebox.showerror("Error","Incorrect username!")
        cursor.close()
        connection.close()

class registerWindow:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.configure(bg='pale turquoise')
        self.label1 = tk.Label(self.frame, text='Sign up', bg='DeepSkyBlue2', font="Helvetica 18 italic bold",pady=10,relief='groove',padx=5)
        self.label2 = tk.Label(self.frame, text='Username', bg='sky blue', font=['fixedsys',17],relief='groove',pady=4)
        self.label3 = tk.Label(self.frame, text='Password', bg='sky blue', font=['fixedsys',17],relief='groove',pady=4)
        self.entry1 = tk.Entry(self.frame, relief='groove',font=('Helvetica 16'))
        self.entry2 = tk.Entry(self.frame, relief='groove',font=('Helvetica 16'))
        self.button1 = tk.Button(self.frame,borderwidth=3,text='Enter',font='Helvetica 16 bold', bg='sky blue',command=self.register)
        self.button2 = tk.Button(self.frame,borderwidth=3,text='Return',font='Helvetica 16 bold', bg='sky blue',command=self.close)
        self.label1.grid(row=0,pady=25,columnspan=2,padx=170)
        self.label2.grid(pady=10,row=1,column=0,sticky='w',padx=25)
        self.label3.grid(pady=10,row=2,column=0,sticky='w',padx=25)
        self.entry1.grid(row=1,column=1,sticky='w',ipady=7)
        self.entry2.grid(row=2,column=1,sticky='w',ipady=7)
        self.button1.grid(row=3,column=0,sticky='e')
        self.button2.grid(row=3,column=1,sticky='w', padx=20,pady=10)
        self.frame.grid()

    def close(self):
        self.master.destroy()

    def register(self):
        connection = connector.connect(host="localhost", user="root", passwd="password", database="project")
        cursor = connection.cursor()
        cursor.execute("select * from user;")
        db = dict()
        result = cursor.fetchall()
        for entry in result:
            user,passwd = entry
            db[user] = passwd
        username = self.entry1.get()
        password = self.entry2.get()
        if username not in db.keys():
            if len(password) >= 8:
                cursor.execute("insert into user (user,password) values ('%s','%s')" % (username, password))
                connection.commit()
                self.master.destroy()
                messagebox.showinfo("Success","User successfully registered")
            else:
                messagebox.showerror("Error",
"""
Password too small!
Use a password with a length of at least 8 characters.
""")
        else:
            messagebox.showerror("Error",
"""
Username exists!
Try another username.
""")
        cursor.close()
        connection.close()

def main(): #runs mainloop
    root = tk.Tk()
    app = homeWindow(root)
    root.geometry("450x300")
    root.title("User Portal")
    root.configure(bg='pale turquoise', borderwidth=5,relief='sunk')
    positionRight = int(root.winfo_screenwidth()/2 - 525/2)
    positionDown = int(root.winfo_screenheight()/2 - 350/2)
    root.geometry("+{}+{}".format(positionRight, positionDown))
    root.resizable(0,0)
    root.mainloop()

if __name__ == '__main__':
    main()
