from tkinter import *
from tkinter import messagebox
import datetime
import random

def Ok():
    uname = e1.get()
    password = e2.get()

    if uname == "" or password == "":
        messagebox.showinfo("", "Blank not allowed")
    elif len(password) < 4:
        messagebox.showinfo("", "Password must be at least 4 characters long")
    elif uname == "ADMIN" and password == "1234":
        NewWn(uname)
    else:
        messagebox.showinfo("", "Incorrect Username or Password")

def NewWn(username):
    newWindow = Toplevel(wn)
    newWindow.title("Dashboard")
    newWindow.geometry("300x300")
    newWindow.config(bg="pink")

    welcome_label = Label(newWindow, text=f"Welcome, {username}!", font=("Arial", 12, "bold"))
    welcome_label.pack(pady=10)

    # ฟังก์ชันอัปเดตเวลาปัจจุบัน
    def update_time():
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        time_label.config(text=f"Current Time: {current_time}")
        newWindow.after(1000, update_time)

    # แสดงเวลาปัจจุบัน
    time_label = Label(newWindow, text="", font=("Arial", 10))
    time_label.pack(pady=5)
    update_time()

    # แสดงวันที่ปัจจุบัน
    date_label = Label(newWindow, text=f"Current Date: {datetime.datetime.now().strftime('%Y-%m-%d')}", font=("Arial", 10))
    date_label.pack(pady=5)

    # ฟังก์ชันเช็คอิน
    def check_in():
        check_in_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        messagebox.showinfo("Check-In", f"Checked in at {check_in_time}")
        check_in_label.config(text=f"Last Check-In: {check_in_time}")

    # ปุ่มเช็คอิน
    Button(newWindow, text="Check-In", command=check_in).pack(pady=5)

    # แสดงเวลาเช็คอินล่าสุด
    check_in_label = Label(newWindow, text="Last Check-In: None", font=("Arial", 10))
    check_in_label.pack(pady=5)

    # ปุ่ม Logout
    def logout():
        newWindow.destroy()  # ปิดหน้าต่างที่สอง
    Button(newWindow, text="Logout", command=logout).pack(pady=5)

    # ปุ่ม Exit เพื่อปิดโปรแกรม
    Button(newWindow, text="Exit", command=wn.quit).pack(pady=5)

def create_label(window, text, x, y):
    Label(window, text=text).place(x=x, y=y)

def create_entry(window, show, x, y):
    entry = Entry(window, show=show)
    entry.place(x=x, y=y)
    return entry

#หน้าจอ Login
wn = Tk()
wn.config(bg="lightblue")
wn.title("Login")
wn.geometry("300x200")

create_label(wn, "Username", 10, 10)
create_label(wn, "Password", 10, 40)

e1 = create_entry(wn, "", 140, 10)
e2 = create_entry(wn, "*", 140, 40)

Button(wn, text='Login', command=Ok, height=2, width=13).place(x=10, y=100)

# ปุ่ม Clear เพื่อเคลียร์ข้อมูลในฟิลด์การกรอกข้อมูล
def clear_fields():
    e1.delete(0, END)
    e2.delete(0, END)

Button(wn, text='Clear', command=clear_fields, height=2, width=13).place(x=150, y=100)

wn.mainloop()