import tkinter as tk
from tkinter.ttk import *
import sqlite3
import customtkinter 
from tkinter import ttk
from tkinter import messagebox
from CTkTable import *

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Creates the main application window
app = customtkinter.CTk()
app.title("School Management System")
app.geometry('1000x580')

# Creating the functions

# Add student function
def add_student():
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()
    attendance = attendance_entry.get()
    course = course_entry.get()
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade, attendance, course) VALUES (?, ?, ?, ?, ?)", (name, age, grade, attendance, course))
    conn.commit()
    conn.close()


# Add course function    
def add_course():
    name = course_name_entry.get()
    description = course_description_entry.get()
    
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO courses (name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    conn.close()

#Delete function
def delete_student():
    student_id = entry_id.get()
    try:
    
        connection = sqlite3.connect('school.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM students WHERE id=?', (student_id,))
        connection.commit()

        messagebox.showinfo('Success', f'Student with ID {student_id} deleted successfully.')
    except sqlite3.Error as e:
        messagebox.showerror('Error', f'Error deleting student: {e}')
    finally:
        
        connection.close()


def delete_course():
    course_id = entry_id.get()
    try:
    
        connection = sqlite3.connect('school.db')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM courses WHERE id=?', (course_id,))
        connection.commit()

        messagebox.showinfo('Success', f'Student with ID {course_id} deleted successfully.')
    except sqlite3.Error as e:
        messagebox.showerror('Error', f'Error deleting student: {e}')
    finally:
        
        connection.close()


# Creating the frames
frame1 = customtkinter.CTkFrame(app, width=350, height=330)
frame1.place(x=10, y=10)

frame2 = customtkinter.CTkFrame(app, width=350, height=180)
frame2.place(x=10, y=350)

frame3 = customtkinter.CTkFrame(app, width=180, height=180)
frame3.place(x=370, y=10)

frame4 = customtkinter.CTkFrame(app, width=180, height=180)
frame4.place(x=560, y=10)


# Creates student input fields
name_label = customtkinter.CTkLabel(app, text="Name:", bg_color="#2B2B2B")
name_label.grid(row=0, column=0, padx=20, pady= 20)
name_entry = customtkinter.CTkEntry(app)
name_entry.grid(row=0,column=1, pady=20)

age_label = customtkinter.CTkLabel(app, text="Age:",bg_color="#2B2B2B")
age_label.grid(row=1, column=0,)
age_entry = customtkinter.CTkEntry(app)
age_entry.grid(row=1, column=1)


grade_label = customtkinter.CTkLabel(app, text="Grade:", bg_color="#2B2B2B")
grade_label.grid(row=2, column=0, pady=20)
grade_entry = customtkinter.CTkEntry(app)
grade_entry.grid(row=2, column=1)


attendance_label = customtkinter.CTkLabel(app, text="Attendance:", bg_color="#2B2B2B")
attendance_label.grid(row=3, column=0, )
attendance_entry = customtkinter.CTkEntry(app)
attendance_entry.grid(row=3, column=1)


course_label = customtkinter.CTkLabel(app, text="Course:", bg_color="#2B2B2B")
course_label.grid(row=4, column=0, pady=20)
course_entry = customtkinter.CTkEntry(app)
course_entry.grid(row=4, column=1)


add_student_button = customtkinter.CTkButton(app, text="Add Student", command=lambda: (add_student()), bg_color="#2B2B2B",)
add_student_button.grid(row=5, column=1, pady=30)





# Creates course input fields
course_name_label = customtkinter.CTkLabel(app, text="Course Name:", bg_color="#2B2B2B")
course_name_label.grid(row=7, column=0, pady=20,)
course_name_entry = customtkinter.CTkEntry(app)
course_name_entry.grid(row=7, column=1, pady=20)


course_description_label = customtkinter.CTkLabel(app, text="Course Description:", bg_color="#2B2B2B")
course_description_label.grid(row=8, column=0, padx=20)
course_description_entry = customtkinter.CTkEntry(app, )
course_description_entry.grid(row=8, column=1, padx=20 )


add_course_button = customtkinter.CTkButton(app, text="Add Course", command=add_course)
add_course_button.grid(row=9, column=1, padx=20, pady=30)



#Delete student box
label_id = customtkinter.CTkLabel(app, text='Enter Student ID:', bg_color="#2B2B2B")
label_id.place(x=415, y=20)

entry_id = customtkinter.CTkEntry(app)
entry_id.place(x=390, y=70)

delete_button = customtkinter.CTkButton(app, text='Delete Student', command=delete_student, )
delete_button.place(x=390, y=120)

#Delete course box
label_id = customtkinter.CTkLabel(app, text='Enter Course ID:', bg_color="#2B2B2B")
label_id.place(x=600, y=20)

entry_id = customtkinter.CTkEntry(app)
entry_id.place(x=580, y=70)

delete_button = customtkinter.CTkButton(app, text='Delete Course', command=delete_course, )
delete_button.place(x=580, y=120)

# Creating the students table
table = ttk.Treeview(app, columns= ("id","name", "age", "grade", "attendance", "course"),show='headings')
table.heading('id', text="Student ID")
table.heading('name', text="Full Name")
table.heading('age', text="Age")
table.heading('grade', text="Grade")
table.heading('attendance', text="Attendance")
table.heading('course', text="Course")

# Editing table columns
table.column("id", width=100)
table.column("name", width=100)
table.column("age", width=100)
table.column("grade", width=100)
table.column("attendance", width=100)
table.column("course", width=100)

# Styling the table
style = ttk.Style(app)
style.theme_use("clam")
style.configure("Treeview", background="black", fieldbackground="black", foreground="white")

table.place(x=370, y=200,)


# Putting the Records in the table
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Retrieve data from the database
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

# Insert the data into the TreeView widget
for row in rows:
    table.insert("", "end", values=row)

# Close the database connection
conn.close()


















app.mainloop()



