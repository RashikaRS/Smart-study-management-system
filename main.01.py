from tkinter import *
from tkinter import messagebox
from datetime import datetime
root = Tk()
root.title("Smart Study Management System")
root.geometry("1000x800")
root.configure(bg="lightcyan")
title = Label(root,
              text="Smart Study Management System",
              font=("Arial", 24, "bold"),
              bg="lightcyan",
              fg="darkblue")
title.pack(pady=10)
today = datetime.now().strftime("%d-%m-%Y %H:%M")

date_label = Label(root,
                   text="Date: " + today,
                   bg="lightcyan",
                   font=("Arial", 12))
date_label.pack(pady=5)
def login():
    name = name_entry.get()

    if name == "":
        messagebox.showerror("Error", "Enter username")
    else:
        messagebox.showinfo("Welcome", "Hello " + name)
        welcome_label.config(text="Welcome " + name)

name_label = Label(root, text="Username", bg="lightcyan")
name_label.pack()

name_entry = Entry(root)
name_entry.pack()

pass_label = Label(root, text="Password", bg="lightcyan")
pass_label.pack()

password_entry = Entry(root, show="*")
password_entry.pack()

lg = Button(root, text="LOGIN", command=login, bg="green", fg="white")
lg.pack(pady=10)

welcome_label = Label(root, text="", bg="lightcyan", font=("Arial", 12, "bold"))
welcome_label.pack()
cards = Frame(root, bg="lightcyan")
cards.pack(pady=15)

task_count = 0
quiz_score = 0
notes_count = 0
frame1 = Frame(cards, bg="lightblue", width=200, height=100)
frame1.pack(side=LEFT, padx=10)
frame1.pack_propagate(False)

Label(frame1, text="Study Hours", bg="lightblue").pack()
Label(frame1, text="25", font=("Arial", 18, "bold"), bg="lightblue")
frame2 = Frame(cards, bg="lightgreen", width=200, height=100)
frame2.pack(side=LEFT, padx=10)
frame2.pack_propagate(False)

Label(frame2, text="Tasks Done", bg="lightgreen").pack()
task_count_label = Label(frame2, text="0", font=("Arial", 18, "bold"), bg="lightgreen")
task_count_label.pack()
frame3 = Frame(cards, bg="lightyellow", width=200, height=100)
frame3.pack(side=LEFT, padx=10)
frame3.pack_propagate(False)

Label(frame3, text="Quiz Score", bg="lightyellow").pack()
quiz_score_label = Label(frame3, text="0", font=("Arial", 18, "bold"), bg="lightyellow")
quiz_score_label.pack()
frame4 = Frame(cards, bg="lightpink", width=200, height=100)
frame4.pack(side=LEFT, padx=10)
frame4.pack_propagate(False)

Label(frame4, text="Notes Count", bg="lightpink").pack()
notes_count_label = Label(frame4, text="0", font=("Arial", 18, "bold"), bg="lightpink")
notes_count_label.pack()
planner = Frame(root, bg="lightcyan")
planner.pack(pady=10)

Label(planner, text="Today's Task", bg="lightcyan", font=("Arial", 12, "bold")).pack()

task_entry = Entry(planner, width=40)
task_entry.pack(pady=5)

task_container = Frame(planner, bg="lightcyan")
task_container.pack()

def add_task():
    global task_count

    task_name = task_entry.get()

    if task_name == "":
        messagebox.showwarning("Warning", "Enter task")
        return

    Label(task_container,
          text="• " + task_name,
          bg="lightcyan",
          anchor="w").pack(fill="x")

    task_count += 1
    task_count_label.config(text=str(task_count))

    task_entry.delete(0, END)

Button(planner, text="Add Task", command=add_task, bg="black", fg="white").pack(pady=5)
Label(root, text="Notes Section", bg="lightcyan", font=("Arial", 12, "bold")).pack(pady=5)
notesbox = Text(root, width=50, height=6)
notesbox.pack()
def save_note():
    global notes_count

    note = notesbox.get("1.0", END)

    if note.strip() == "":
        messagebox.showwarning("Warning", "Write something")
        return

    notes_count += 1
    notes_count_label.config(text=str(notes_count))

    messagebox.showinfo("Saved", "Note saved!")

Button(root, text="Save Note", command=save_note, bg="black", fg="white").pack(pady=5)
Label(root, text="Quiz Section", bg="lightcyan", font=("Arial", 12, "bold")).pack(pady=5)
Label(root, text="Python is a __ language?", bg="lightcyan").pack()
answer = StringVar()
def check_answer():
    global quiz_score

    selected = answer.get()

    if selected == "programming":
        messagebox.showinfo("Result", "Correct Answer")
        quiz_score += 1
        quiz_score_label.config(text=str(quiz_score))
    else:
        messagebox.showerror("Result", "Wrong Answer")

Radiobutton(root, text="Programming", variable=answer, value="programming", bg="lightcyan").pack()
Radiobutton(root, text="Database", variable=answer, value="database", bg="lightcyan").pack()
Radiobutton(root, text="Browser", variable=answer, value="browser", bg="lightcyan").pack()
Button(root, text="Submit", command=check_answer, bg="black", fg="white").pack(pady=5)
Button(root,
       text="EXIT",
       command=root.destroy,
       bg="red",
       fg="white").pack(pady=10)
root.mainloop()
