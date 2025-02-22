import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# เก็บข้อมูลผู้ใช้
users = []

# ฟังก์ชันแสดงหน้าจอเข้าสู่ระบบ
def show_login():
    # ลบ widget ทั้งหมดใน root
    for widget in root.winfo_children():
        widget.destroy()
    
    # สร้าง label และ entry สำหรับการเข้าสู่ระบบ
    tk.Label(root, text="Log in", font=("Arial", 24)).pack(pady=10)
    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()
    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()
    
    # ฟังก์ชันสำหรับการเข้าสู่ระบบ
    def sign_in():
        username = username_entry.get()
        password = password_entry.get()
        for user in users:
            if user['username'] == username and user['password'] == password:
                show_welcome(username)
                return
        messagebox.showerror("Error", "Username or password is incorrect")
        password_entry.delete(0, tk.END)
    
    # ฟังก์ชันสำหรับการสมัครสมาชิก
    def sign_up():
        show_sign_up()
    
    # ปุ่มเข้าสู่ระบบและสมัครสมาชิก
    tk.Button(root, text="Sign In", command=sign_in).pack(pady=5)
    tk.Button(root, text="Sign Up", command=sign_up).pack(pady=5)

# ฟังก์ชันแสดงหน้าจอสมัครสมาชิก
def show_sign_up():
    # ลบ widget ทั้งหมดใน root
    for widget in root.winfo_children():
        widget.destroy()
    
    # สร้าง label และ entry สำหรับการสมัครสมาชิก
    tk.Label(root, text="Sign Up", font=("Arial", 24)).pack(pady=10)
    tk.Label(root, text="Username").pack()
    username_entry = tk.Entry(root)
    username_entry.pack()
    tk.Label(root, text="Password").pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()
    tk.Label(root, text="Confirm Password").pack()
    confirm_password_entry = tk.Entry(root, show="*")
    confirm_password_entry.pack()
    tk.Label(root, text="Email").pack()
    email_entry = tk.Entry(root)
    email_entry.pack()
    
    # ฟังก์ชันยืนยันการสมัครสมาชิก
    def confirm():
        username = username_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        email = email_entry.get()
        for user in users:
            if user['username'] == username:
                messagebox.showerror("Error", "Username already exists")
                return
        if password != confirm_password:
            messagebox.showerror("Error", "Password do not match")
            password_entry.delete(0, tk.END)
            confirm_password_entry.delete(0, tk.END)
            return
        elif username == "" or password == "" or email == "":
            if username == "" or password == "":
                messagebox.showerror("Error", "Username and password cannot be empty")  
            elif email == "":
                messagebox.showerror("Error", "Email cannot be empty")
            return
        elif password == confirm_password:
            users.append({"username": username, "password": password, "email": email})
            messagebox.showinfo("success", "Sign up successful")
            show_login()
            return
            
        else:
            messagebox.showerror("Error", "Sign up failed")
            return
        
            
        
            
    # ฟังก์ชันยกเลิกการสมัครสมาชิก
    def cancel():
        if messagebox.askyesno("Confirm", "Confirm to cancel?"):
            show_login()
    
    # ปุ่มยืนยันและยกเลิกการสมัครสมาชิก
    tk.Button(root, text="Confirm", command=confirm).pack(pady=5)
    tk.Button(root, text="Cancel", command=cancel).pack(pady=5)

# ฟังก์ชันแสดงหน้าจอต้อนรับ
def show_welcome(username):
    # ลบ widget ทั้งหมดใน root
    for widget in root.winfo_children():
        widget.destroy()
    
    # สร้าง label แสดงข้อความต้อนรับและชื่อผู้ใช้
    tk.Label(root, text="Welcome", font=("Arial", 24)).pack(pady=10)
    tk.Label(root, text=username, font=("Arial", 16, "bold")).pack()
    tk.Label(root, text=datetime.now().strftime("%Y-%m-%d %H:%M:%S")).pack()
    
    # ฟังก์ชันเช็คอิน
    def check_in():
        check_in_button.config(text=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    # ฟังก์ชันแสดงข้อมูลผู้ใช้
    def show_info():
        for user in users:
            if user['username'] == username:
                messagebox.showinfo("Information", f"Username: {user['username']}\nPassword: {user['password']}\nEmail: {user['email']}")
    
    # ฟังก์ชันออกจากระบบ
    def log_out():
        show_login()
    
    # ปุ่มเช็คอิน แสดงข้อมูล และออกจากระบบ
    check_in_button = tk.Button(root, text="Check In", command=check_in)
    check_in_button.pack(pady=5)
    tk.Button(root, text="Information", command=show_info).pack(pady=5)
    tk.Button(root, text="Log Out", command=log_out).pack(pady=5)

# สร้างหน้าต่างหลักของโปรแกรม
root = tk.Tk()
root.title("Login System")
root.geometry("300x400")

# แสดงหน้าจอเข้าสู่ระบบเมื่อเริ่มต้นโปรแกรม
show_login()

# เริ่ม
root.mainloop()