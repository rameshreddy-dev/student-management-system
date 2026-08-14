import tkinter as tk
from tkinter import messagebox


def add_student():
    name = name_entry.get()
    roll_no = roll_entry.get()

    if name == "" or roll_no == "":
        result_label.config(
            text="Please enter all details."
        )
        return

    student_list.insert(
        tk.END,
        f"{name} - {roll_no}"
    )

    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)

    result_label.config(
        text="Student added successfully!"
    )


def delete_student():
    selected = student_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Select a student first."
        )
        return

    student_list.delete(selected[0])

    result_label.config(
        text="Student deleted successfully!"
    )


def update_student():
    selected = student_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Select a student first."
        )
        return

    name = name_entry.get()
    roll_no = roll_entry.get()

    if not name or not roll_no:
        messagebox.showwarning(
            "Warning",
            "Enter a name and roll number."
        )
        return

    student_list.delete(selected[0])

    student_list.insert(
        selected[0],
        f"{name} - {roll_no}"
    )

    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)

    messagebox.showinfo(
        "Success",
        "Student updated successfully."
    )


window = tk.Tk()

window.title(
    "Student Management System"
)

window.geometry("500x450")


name_label = tk.Label(
    window,
    text="Student Name"
)

name_label.pack()


name_entry = tk.Entry(
    window
)

name_entry.pack()


roll_label = tk.Label(
    window,
    text="Roll Number"
)

roll_label.pack()


roll_entry = tk.Entry(
    window
)

roll_entry.pack()


# Add Student button
add_button = tk.Button(
    window,
    text="Add Student",
    command=add_student
)

add_button.pack()


# Delete Student button
delete_button = tk.Button(
    window,
    text="Delete Student",
    command=delete_student
)

delete_button.pack()


# Update Student button
update_button = tk.Button(
    window,
    text="Update Student",
    command=update_student
)

update_button.pack()


student_list = tk.Listbox(
    window,
    width=50,
    height=10
)

student_list.pack()


result_label = tk.Label(
    window,
    text=""
)

result_label.pack()


window.mainloop()