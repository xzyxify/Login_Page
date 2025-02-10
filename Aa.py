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
    elif uname == "ADMIN" and password == "123":
        NewWn(uname)
    else:
        messagebox.showinfo("", "Incorrect Username or Password")

def NewWn(username):
    newWindow = Toplevel(wn)
    newWindow.title("Dashboard")
    newWindow.geometry("300x250")
    newWindow.config(bg="pink")

    Label(newWindow, text=f"Welcome, {username}!", font=("Arial", 12, "bold")).pack(pady=10)

    # ฟังก์ชันอัปเดตเวลาปัจจุบัน
    def update_time():
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        time_label.config(text=f"Current Time: {current_time}")
        newWindow.after(1000, update_time)

    # แสดงเวลาปัจจุบัน
    time_label = Label(newWindow, text="", font=("Arial", 10))
    time_label.pack(pady=5)
    update_time()

    # ฟังก์ชันเปลี่ยนสีพื้นหลัง
    def change_bg():
        colors = ["lightblue", "lightgreen", "lightyellow", "lightgray", "lightcoral"]
        newWindow.config(bg=random.choice(colors))

    # ปุ่มเปลี่ยนสีพื้นหลัง
    Button(newWindow, text="Change Background", command=change_bg).pack(pady=5)

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