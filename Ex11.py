from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

def open_Toplevel1():
    top1 = Toplevel(root)
    top1.title("Student Login")
    top1.geometry("300x200")

    username_label = Label(top1, text="Username")
    username_label.place(x=30, y=50)
    password_label = Label(top1, text="Password")
    password_label.place(x=30, y=90)

    e1 = tk.Entry(top1, width=20)
    e1.place(x=100, y=50)
    e2 = tk.Entry(top1, width=20, show="*")
    e2.place(x=100, y=90)

    def click():
        un = e1.get()
        ps = e2.get()
        if un == "DHONI" and ps == "D@1981":
            top1.destroy()
            open_Toplevel2()
        else:
            messagebox.showinfo("Login", "Login failed!")

    def clearText():
        e1.delete(0, 'end')
        e2.delete(0, 'end')

    submit_button = Button(top1, command=click, text="Submit",
                           activebackground="red", activeforeground="blue")
    submit_button.place(x=30, y=120)

    clr_button = Button(top1, command=clearText, text="Clear",
                        activebackground="red", activeforeground="blue")
    clr_button.place(x=90, y=120)

    cls_button = Button(top1, command=top1.destroy, text="Close",
                        activebackground="red", activeforeground="blue")
    cls_button.place(x=150, y=120)


def open_Toplevel2():
    top2 = Toplevel(root)
    top2.title("Course Registration")
    top2.geometry("400x500")

    Label(top2, text="Name").place(x=30, y=50)
    Label(top2, text="Username").place(x=30, y=90)
    Label(top2, text="Gender").place(x=30, y=130)
    Label(top2, text="Address").place(x=30, y=170)
    Label(top2, text="Course Selection").place(x=30, y=250)

    e3 = ttk.Entry(top2, width=20)
    e3.place(x=150, y=50)
    e4 = ttk.Entry(top2, width=20)
    e4.place(x=150, y=90)

    gender_var = tk.StringVar()
    radio_button1 = tk.Radiobutton(top2, text="Male", variable=gender_var, value="Male")
    radio_button1.place(x=150, y=130)
    radio_button2 = tk.Radiobutton(top2, text="Female", variable=gender_var, value="Female")
    radio_button2.place(x=220, y=130)

    t = Text(top2, height=3, width=25)
    t.place(x=150, y=170)

    scrollbar = Scrollbar(top2, orient='vertical')
    listbox = tk.Listbox(top2, height=3, selectmode=tk.SINGLE, yscrollcommand=scrollbar.set)
    listbox.insert(tk.END, "Java")
    listbox.insert(tk.END, "Python")
    listbox.insert(tk.END, "R Programming")
    listbox.insert(tk.END, "Image Processing")
    listbox.place(x=150, y=250)

    scrollbar.place(x=320, y=250, height=50)
    scrollbar.config(command=listbox.yview)

    def submit():
        messagebox.showinfo("Submission", "Registration successful!")

    def cancel():
        top2.destroy()

    submit_button = Button(top2, command=submit, text="Submit",
                           activebackground="green", activeforeground="white")
    submit_button.place(x=30, y=350)

    cancel_button = Button(top2, command=cancel, text="Cancel",
                           activebackground="red", activeforeground="white")
    cancel_button.place(x=120, y=350)


# === Main Window ===
root = Tk()
root.title("Aringar Anna Govt. Arts College")
root.geometry("400x350")

frm2 = Frame(root)
frm2.pack(fill=tk.BOTH, expand=True)

def clear_frame():
    frm2.destroy()

# === Menu Bar ===
mbar = Menu(root)
fmenu = Menu(mbar, tearoff=0)
fmenu.add_command(label="Registration", command=open_Toplevel2)
fmenu.add_command(label="Sign-in", command=open_Toplevel1)
fmenu.add_command(label="Clear", command=clear_frame)
fmenu.add_separator()
fmenu.add_command(label="Exit", command=root.destroy)
mbar.add_cascade(label="File", menu=fmenu)

emenu = Menu(mbar, tearoff=0)
emenu.add_command(label="Undo")
emenu.add_command(label="Redo")
mbar.add_cascade(label="Edit", menu=emenu)

root.config(menu=mbar)

# === Scale for Font Size ===
def on_Scale_changed(value):
    try:
        new_font_size = int(value)
        lbl.config(font=("Roboto", new_font_size))
    except ValueError:
        pass

lbl = Label(frm2, text="Welcome to GUI App", fg="blue", font=("Helvetica", 12))
lbl.pack()

Scale_1 = tk.Scale(frm2, from_=14, to=40, orient=tk.HORIZONTAL,
                   label="Increase / Decrease Font Size", command=on_Scale_changed)
Scale_1.pack()

root.mainloop()
