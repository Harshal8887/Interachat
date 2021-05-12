from tkinter import *
from tkinter import messagebox as mb
import mysql.connector as sql
import app
import _thread


def login():
    try:
        reg.destroy()
    except:
        pass
    global log
    log = Tk()
    log.title('Interachat')
    # log.iconbitmap('E:/project/minor/Chat Application/resources/chat.PNG')
    # photo = PhotoImage(file="")
    # log.iconphoto(False, photo)
    log.geometry('310x300+220+170')
    log.configure(bg='#213a3b')
    log.resizable(0, 0)

    log_label = Label(log, text='Login', width=30, height=2, font=(
        'Arial White', 20, 'bold'), bg='#213a3b', fg='#fff')
    log_label.pack()

    u = Label(log, text='username', font=(
        'Arial Black', 11), bg='#213a3b', fg='#fff')
    u.place(x=7, y=90)

    user_entry = Entry(log, font=('Arial Black', 10, 'bold'),
                       width=20, bg='#fff',)
    user_entry.place(x=105, y=95)

    p = Label(log, text='password', font=(
        'Arial Black', 11, 'bold'), bg='#213a3b', fg='#fff')
    p.place(x=7, y=150)

    pass_entry = Entry(log, show='*', font=('Arial Black',
                                            10, 'bold'),  width=20, bg='#fff')
    pass_entry.place(x=105, y=155)

    resp = Label(log, text='', font=('Arial Black', 10, 'bold'), bg='#213a3b')
    resp.place(x=30, y=250)

    def log_func(*args):

        data_base = sql.connect(host='sql6.freemysqlhosting.net	', port=3306,
                                user='sql6411925', passwd='wiRyjzBarQ', database='sql6411925')
        c = data_base.cursor()

        user = user_entry.get()
        password = pass_entry.get()

        try:
            c.execute(
                f'select Password from log_details where Username = "{user}" ')

            b = c.fetchall()

            for i in b:
                passw = i[0]

            if password == passw:
                c.execute(
                    f'select name from log_details where Username= "{user}"')
                b = c.fetchall()[0][0]
                # username_name = b
                resp.configure(
                    text=f'Login Successful\n Welcome {b} ', fg='green')
                log.destroy()
                f = open('isLog.txt', 'w')
                # for development purpose
                # to_write = 'logged in,'+b
                to_write = 'logged off'
                f.write(to_write)
                f.close()
                app.ChatApplication()

            else:
                resp.configure(text='Wrong Password', fg='red')

        except UnboundLocalError:
            resp.configure(text=f'Username {user} Does Not Exist', fg='red')

    submit = Button(log, text='Login', font=('Arial Black', 11, 'bold'),
                    width=12, bg='#41a8ae', command=log_func, bd=0, fg='white')
    submit.place(x=10, y=220)

    # Label(log, text='Create new Account',bg='#213a3b',fg='white').place(x=10,y=220)

    Button(log, text='Sign Up', font=('Arial Black', 11, 'bold'), width=12,
           bg='#41a8ae', bd=0, fg='white', command=register).place(x=155, y=220)

    log.bind('<Return>', log_func)

    log.mainloop()


def register():
    try:
        log.destroy()
    except:
        pass

    global reg
    reg = Tk()
    reg.title('Intrachat')
    # photo = PhotoImage(file="resources/chat1.png")
    # reg.iconphoto(False, photo)
    reg.configure(bg='#213a3b')
    reg.geometry('450x450+220+170')
    reg.resizable(0, 0)

    reg_label = Label(reg, text='Register', fg='white', width=20,
                      height=3, font=('Arial Black', 20, 'bold'), bg='#213a3b')
    reg_label.pack()

    n = Label(reg, text='Name', font=('Arial Black',
                                      11, 'bold'), bg='#213a3b', fg='#fff')
    n.place(x=85, y=150)

    name_entry = Entry(reg, font=('Arial Black', 10, 'bold'),
                       width=22, bg='#e8ffff')
    name_entry.place(x=150, y=155)

    u = Label(reg, text='Username', font=(
        'Arial Black', 12, 'bold'), bg='#213a3b', fg='#fff')
    u.place(x=45, y=200)

    user_entry = Entry(reg, font=('Arial Black', 10, 'bold'),
                       width=22, bg='#e8ffff')
    user_entry.place(x=150, y=205)

    p = Label(reg, text='Set Password', font=(
        'Arial Black', 12, 'bold'), bg='#213a3b', fg='#fff')
    p.place(x=15, y=250)

    pass_entry = Entry(reg, show='*', font=('Arial Black',
                                            10, 'bold'),  width=22, bg='#e8ffff')
    pass_entry.place(x=150, y=255)

    def reg_func(*args):

        data_base = sql.connect(host='sql6.freemysqlhosting.net	', port=3306,
                                user='sql6411925', passwd='wiRyjzBarQ', database='sql6411925')

        c = data_base.cursor()

        name = name_entry.get().title()
        user = user_entry.get()
        password = pass_entry.get()

        if name != '' and user != '' and password != '':

            c.execute('select Username from log_details')

            l = c.fetchall()
            ex_t = False

            for i in l:
                if user == i[0]:
                    ex_t = True
                    break
                else:
                    ex_t = False

            if ex_t == True:

                mb.showerror('Register', f'{user} Already Exist.')
            else:
                c.execute(
                    f'insert into log_details values("{name}","{user}","{password}")')

                data_base.commit()
                name_entry.delete(0, END)
                user_entry.delete(0, END)
                pass_entry.delete(0, END)
                global username_name
                username_name = name
                reg.destroy()
                f = open('isLog.txt', 'w')
                # to_write = 'logged in,'+username_name
                # for development purpose
                to_write = 'logged off'
                f.write(to_write)
                f.close()
                app.ChatApplication()

        else:
            mb.showerror('UniChat', 'Please Fill All The Fields.')

    submit = Button(reg, text='Submit', font=('Arial Black', 11, 'bold'),
                    bd=0, width=18, bg='#41a8ae', command=reg_func, fg='white')
    submit.place(x=150, y=320)

    Label(reg, text='Already have an account', font=('Arial Black',
                                                     10, 'bold'), bg='#213a3b', fg='white').place(x=10, y=410)

    Button(reg, text='Login', font=('Arial Black', 10, 'bold', 'underline'),
           bg='#213a3b', fg='white', bd=0, command=login).place(x=193, y=408)

    reg.bind('<Return>', reg_func)

    reg.mainloop()
