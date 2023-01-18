import customtkinter
import mysql.connector

cnx = mysql.connector.connect(user='root', password='123321123qwe',
                              host='localhost',
                              database='trypython')


def gg(id):
    cursor = cnx.cursor()
    query = (f"select * from students where idstudents ={id};")
    cursor.execute(query)
    gg = cursor.fetchall()
    return gg[0]


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x500")
root.title("My Library...!!")

frame = customtkinter.CTkFrame(master=root,
                               height=400,
                               width=400,
                               corner_radius=10)
frame.pack(padx=10, pady=40)


def button1_event():
    dialog = customtkinter.CTkInputDialog(
        text="Enter the student id", title="Test")
    id = dialog.get_input()
    res = gg(id)
    std = customtkinter.CTk()
    std.geometry("500x500")
    btn = customtkinter.CTkButton(
        master=std, text="Student info", fg_color="transparent", font=(("Roboto"), (40)))
    btn.pack(side="top", padx=40, pady=40)
    btn2 = customtkinter.CTkButton(
        master=std, text=f"Student name : {res[2]}", fg_color="transparent", font=(("Roboto"), (20)))
    btn2.pack(padx=50, pady=10)
    btn3 = customtkinter.CTkButton(
        master=std, text=f"Student class : {id}", fg_color="transparent", font=(("Roboto"), (20)))
    btn3.pack(padx=10, pady=10)
    btn4 = customtkinter.CTkButton(
        master=std, text=f"Student id : {id}", fg_color="transparent", font=(("Roboto"), (20)))
    btn4.pack(padx=10, pady=10)
    btn5 = customtkinter.CTkButton(
        master=std, text=f"Student borrows : {id}", fg_color="transparent", font=(("Roboto"), (20)))
    btn5.pack(padx=10, pady=10)
    btn10 = customtkinter.CTkButton(
        master=std, text=f"Delete this record", font=(("Roboto"), (20)))
    btn10.pack(padx=50, pady=30)
    std.mainloop()


button = customtkinter.CTkButton(
    master=frame, text="Student Info", width=150, height=50, command=button1_event)
button.place(relx=0.3, rely=0.1)

def button2_event():
    dialog = customtkinter.CTkInputDialog(
        text="Book name", title="Test")
    id = dialog.get_input()
    res = gg(id)
    std = customtkinter.CTk()
    std.geometry("500x500")
    btn = customtkinter.CTkButton(
        master=std, text="Student info", fg_color="transparent", font=(("Roboto"), (40)))
    btn.pack(side="top", padx=40, pady=40)
    btn2 = customtkinter.CTkButton(
        master=std, text=f"Student name : {res[2]}", fg_color="transparent", font=(("Roboto"), (20)))
    btn2.pack(padx=50, pady=10)
    btn3 = customtkinter.CTkButton(
        master=std, text=f"Student class : {id}", fg_color="transparent", font=(("Roboto"), (20)))
    btn3.pack(padx=10, pady=10)
    btn4 = customtkinter.CTkButton(
        master=std, text=f"Student id : {id}", fg_color="transparent", font=(("Roboto"), (20)))
    btn4.pack(padx=10, pady=10)
    btn5 = customtkinter.CTkButton(
        master=std, text=f"Student borrows : {id}", fg_color="transparent", font=(("Roboto"), (20)))
    btn5.pack(padx=10, pady=10)
    btn10 = customtkinter.CTkButton(
        master=std, text=f"Delete this record", font=(("Roboto"), (20)))
    btn10.pack(padx=50, pady=30)
    std.mainloop()


button2 = customtkinter.CTkButton(
    master=frame, text="Books search", width=150, height=50,command=button2_event)
button2.place(relx=0.3, rely=0.3)

button3 = customtkinter.CTkButton(
    master=frame, text="Add books", width=150, height=50,)
button3.place(relx=0.3, rely=0.5)

button4 = customtkinter.CTkButton(
    master=frame, text="Borrowed info", width=150, height=50,)
button4.place(relx=0.3, rely=0.7)

root.mainloop()
