from tkinter import *
import os

def delete2():
    screen3.destroy()

def delete3():
    screen4.destroy()

def delete4():
    screen5.destroy()

def delete5():
    screen6.destroy()

def delete6():
    screen7.destroy()

def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Sucess")
    screen3.geometry("150x100")
    Label(screen3, text = "Login sucess :D").pack()
    Button(screen3, text = "Ok", command = delete2).pack()

def password_not_recognized():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Error")
    screen4.geometry("150x100")
    Label(screen4, text = "Password error").pack()
    Button(screen4, text = "Ok", command = delete3).pack()

def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Error")
    screen5.geometry("150x100")
    Label(screen5, text = "User not found").pack()
    Button(screen5, text = "Ok", command = delete4).pack()

def student_code_not_rocognized():
    global screen6
    screen6 = Toplevel(screen)
    screen6.title("Error")
    screen6.geometry("150x100")
    Label(screen6, text = "Student code error").pack()
    Button(screen6, text = "Ok", command = delete5).pack()

def phone_number_not_recognized():
    global screen7
    screen7 = Toplevel(screen)
    screen7.title("Error")
    screen7.geometry("150x100")
    Label(screen7, text = "Phone number error").pack()
    Button(screen7, text = "Ok", command = delete6).pack()

def register_user():
    username_info = username.get()
    password_info = password.get()
    student_code_info = student_code.get()
    phone_number_info = phone_number.get()

    file = open(username_info + ".sec", "w")
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.write(student_code_info + "\n")
    file.write(phone_number_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    student_code_entry.delete(0, END)
    phone_number_entry.delete(0, END)

    Label(screen1, text = "Registration sucess", fg = "green", font = ("Calibri", 11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    student_code1 = student_code_verify.get()
    phone_number1 = phone_number_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    student_code_entry1.delete(0, END)
    phone_number_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 + ".sec" in list_of_files:
        file1 = open(username1 + ".sec", "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            if student_code1 in verify:
                if phone_number1 in verify:
                    login_sucess()
                else:
                    phone_number_not_recognized()
            else:
                student_code_not_rocognized()
        else:
            password_not_recognized()
    else:
        user_not_found()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x350")

    global username
    global password
    global student_code
    global phone_number
    global username_entry
    global password_entry
    global student_code_entry
    global phone_number_entry

    username = StringVar()
    password = StringVar()
    student_code = StringVar()
    phone_number = StringVar()

    Label(screen1, text = "Please enter details bellow").pack()

    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Student Code * ").pack()
    student_code_entry = Entry(screen1, textvariable = student_code)
    student_code_entry.pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Phone Number * ").pack()
    phone_number_entry = Entry(screen1, textvariable = phone_number)
    phone_number_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = "10", height = "1", command = register_user).pack()
    

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x350")
    Label(screen2, text = "Please enter details for login").pack()
    Label(screen2, text = "").pack()

    global username_verify
    global password_verify
    global student_code_verify
    global phone_number_verify
    
    username_verify = StringVar()
    password_verify = StringVar()
    student_code_verify = StringVar()
    phone_number_verify = StringVar()
    
    global username_entry1
    global password_entry1
    global student_code_entry1
    global phone_number_entry1

    Label(screen2, text = "Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Password * ").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Student Code * ").pack()
    student_code_entry1 = Entry(screen2, textvariable = student_code_verify)
    student_code_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Phone Number * ").pack()
    phone_number_entry1 = Entry(screen2, textvariable = phone_number_verify)
    phone_number_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Security")
    Label(text = "Security 1.0", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", width = "30", height = "2", command = login).pack()
    Label(text = "").pack()
    Button(text = "Register", width = "30", height = "2", command = register).pack()
    
    screen.mainloop()

main_screen()