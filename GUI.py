from customtkinter import *
from PIL import ImageTk, Image, ImageFilter
from tkinter import ttk
import mysql.connector

# Window creation and editing

set_appearance_mode("light")
set_default_color_theme("blue")

root= CTk()
root.geometry("1800x900")
root.configure(fg_color="white")

# Importing image

img1= CTkImage(Image.open("edit.png"), size=(20,20))
img2= CTkImage(Image.open("delete.png"), size=(20,20))
img3= CTkImage(Image.open("add.png"), size=(20,20))
img4= CTkImage(Image.open("view.png"), size=(20,20))
img5= CTkImage(Image.open("back.png"), size=(20,20))
img6= CTkImage(Image.open("guitar.png"), size=(50,50))

# Global declerations

count=1
fram= None
fram2 = None
lc=CTkLabel(master=fram)
l1 = CTkLabel(master=root, text=" XYZ company Database", image= img6,font=("Bell MT", 19), compound= LEFT).pack(padx=10, pady=50, side =TOP)

# Editing the tree

style = ttk.Style()
style.configure("Treeview", background="#FFFFFF", foreground="Black", fieldbackground="Black",font=("Bell MT", 20),rowheight=40)
style.map("Treeview", background=[('selected', 'blue')])

tree = ttk.Treeview()

# Establishing connection with database

db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='66165Nisch&18503',
    database='project_sample'
)
cursor = db_connection.cursor()

# Code for GUI

def front():
    global fra
    fra = CTkFrame(master=root, fg_color="#FFFFFF")
    fra.pack(pady=10, fill=BOTH, expand=TRUE)
    l1 = CTkLabel(master=fra, text= "Welcome", font=("Bell MT", 19))
    l1.pack(padx=20, pady=10)
    def a_login():
        fra.pack_forget()
        global fram
        fram= CTkFrame(master=root, fg_color="#FFFFFF")
        fram.pack(pady=20, fill= BOTH, expand=TRUE)
        g= CTkFrame(master=fram, fg_color="#FFFFFF")
        g.pack(pady=1, anchor=E)
        bt1 = CTkButton(master=g, image=img5, text="", font=("Bell MT", 19), width=1, command=back_P)
        bt1.pack(side=RIGHT, padx=1)
        l=CTkLabel(master=fram, text="Admin Login:", font=("Bell MT",19))
        l.pack(padx=20, pady=10)
        u= CTkEntry(master=fram, placeholder_text="Username", font=("Bell  MT", 19))
        u.pack(padx=20, pady=20)

        front.p1= CTkEntry(master=fram, placeholder_text="Password", font=("Bell MT", 19))
        front.p1.pack(padx=20, pady=20)
        front.p1.configure(show="*")

        b2= CTkButton(master=fram, text="Submit", font=("Bell MT", 19), command= lambda: conf(u, front.p1))
        b2.pack(padx=20, pady=20 )

        u.bind("<FocusIn>", lambda s: l.configure(text="Username:"))
        u.bind("<Return>", lambda s:front.p1.focus())
        front.p1.bind("<FocusIn>", lambda s: l.configure(text="Password:"))
        front.p1.bind("<Return>", lambda s:conf(u,front.p1))
    
    b1= CTkButton(master=fra, text="Admin", font=("Bell MT", 19), command= a_login )
    b1.pack(padx=20, pady=20 )

    b= CTkButton(master=fra, text="Login As Customer", font=("Bell MT", 19), command=normal)
    b.pack(padx=20, pady=20 )
    
def admin():
    fram.pack_forget()
    global fram2
    front.p1.unbind("<Return>")
    fram2=CTkFrame(master=root, fg_color="#FFFFFF")
    fram2.pack(fill=BOTH)

    g= CTkFrame(master=fram2, fg_color="#FFFFFF")
    g.pack(pady=1, anchor=E)

    l1= CTkLabel(master=fram2, text="Welcome Admin", font=("Bell MT", 19))
    l1.pack(padx=60, anchor=N)

    bt1 = CTkButton(master=g, image=img5, text="", font=("Bell MT", 19), width=1, command=back)
    bt1.pack(side=RIGHT, padx=1)

    fr= CTkFrame(master=fram2, height=10, width=1, fg_color="#FFFFFF")
    fr.pack(padx=60, pady=20 , anchor=N)
    
    l2= CTkLabel(master=fr, text="Musician", font=("Bell MT", 19)).pack(side=LEFT, padx=10)
    
    b1 = CTkButton(master=fr, image=img1, text="", width=1, command=lambda : edit("M")).pack(side=RIGHT, padx=1)
    b2 = CTkButton(master=fr, image=img2, text="", width=1, command=lambda : delete("M")).pack(side=RIGHT, padx=1)
    b3 = CTkButton(master=fr, image=img3, text="", width=1, command=lambda : add("M")).pack(side=RIGHT, padx=1)
    b4 = CTkButton(master=fr, image=img4, text="", width=1, command=lambda : view("M", "A")).pack(side=RIGHT, padx=1)

    fra= CTkFrame(master=fram2, height=10, width=1, fg_color="#FFFFFF")
    fra.pack(padx=60, pady=20 , anchor=N)
    
    l3= CTkLabel(master=fra, text="Song", font=("Bell MT", 19)).pack(side=LEFT, padx=10)
    
    c1 = CTkButton(master=fra, image=img1, text="", width=1, command=lambda : edit("S")).pack(side=RIGHT, padx=1)
    c2 = CTkButton(master=fra, image=img2, text="", width=1, command=lambda : delete("S")).pack(side=RIGHT, padx=1)
    c3 = CTkButton(master=fra, image=img3, text="", width=1, command=lambda : add("S")).pack(side=RIGHT, padx=1)
    c4 = CTkButton(master=fra, image=img4, text="", width=1, command=lambda : view("S", "A")).pack(side=RIGHT, padx=1)

    f= CTkFrame(master=fram2, height=10, width=1, fg_color="#FFFFFF")
    f.pack(padx=60, pady=20 , anchor=N)
    
    l4= CTkLabel(master=f, text="Instrument", font=("Bell MT", 19)).pack(side=LEFT, padx=10)
    
    d1 = CTkButton(master=f, image=img1, text="", width=1, command=lambda : edit("I")).pack(side=RIGHT, padx=1)
    d2 = CTkButton(master=f, image=img2, text="", width=1, command=lambda : delete("I")).pack(side=RIGHT, padx=1)
    d3 = CTkButton(master=f, image=img3, text="", width=1, command=lambda : add("I")).pack(side=RIGHT, padx=1)
    d4 = CTkButton(master=f, image=img4, text="", width=1, command=lambda : view("I", "A")).pack(side=RIGHT, padx=1)

    fa= CTkFrame(master=fram2, height=10, width=1, fg_color="#FFFFFF")
    fa.pack(padx=60, pady=20 , anchor=N)
    
    l5= CTkLabel(master=fa, text="Album", font=("Bell MT", 19)).pack(side=LEFT, padx=10)
    
    e1 = CTkButton(master=fa, image=img1, text="", width=1, command=lambda : edit("A")).pack(side=RIGHT, padx=1)
    e2 = CTkButton(master=fa, image=img2, text="", width=1, command=lambda : delete("A")).pack(side=RIGHT, padx=1)
    e3 = CTkButton(master=fa, image=img3, text="", width=1, command=lambda : add("A")).pack(side=RIGHT, padx=1)
    e4 = CTkButton(master=fa, image=img4, text="", width=1, command=lambda : view("A", "A")).pack(side=RIGHT, padx=1)


def normal():
    fra.pack_forget()
    global framn
    framn=CTkFrame(master=root, fg_color="#FFFFFF")
    framn.pack(fill=BOTH)

    g= CTkFrame(master=framn, fg_color="#FFFFFF")
    g.pack(pady=1, anchor=E)

    l1= CTkLabel(master=framn, text="Welcome Customer", font=("Bell MT", 19))
    l1.pack(padx=60, anchor=N)

    bt1 = CTkButton(master=g, image=img5, text="", font=("Bell MT", 19), width=1, command=back_N)
    bt1.pack(side=RIGHT, padx=1)

    bt2 = CTkButton(master=framn, text="Musician", font=("Bell MT", 19),command=lambda: view("M", "N")).pack(padx=20, pady=20)
    bt3 = CTkButton(master=framn, text="Album", font=("Bell MT", 19),command=lambda: view("A", "N")).pack(padx=20, pady=20)
    bt4 = CTkButton(master=framn, text="Song", font=("Bell MT", 19),command=lambda: view("S", "N")).pack(padx=20, pady=20)
    bt5 = CTkButton(master=framn, text="Instrument", font=("Bell MT", 19),command=lambda: view("I", "N")).pack(padx=20, pady=20)

def view(val,x):
    if x == "A":
        fram2.pack_forget()
    elif x == "N":
        framn.pack_forget()
    else:
        print("Error")
    global fram3
    fram3= CTkFrame(master=root, height=400, fg_color="#FFFFFF")
    fram3.pack(fill=BOTH, expand=True)

    f3=CTkFrame(master=fram3, fg_color="#FFFFFF")
    f3.pack(anchor=E)

    bt1 = CTkButton(master=f3, image=img5, text="", font=("Bell MT", 19), width=1, command=lambda: back_2(x))
    bt1.pack(side=RIGHT, padx=1)

    frag=CTkFrame(master=fram3, fg_color="#FFFFFF", height=100, width=400)
    frag.pack(fill=BOTH, padx=20 , pady=20, anchor=N)

    fra = CTkFrame(master=fram3, fg_color="#FFFFFF")
    fra.pack(fill=BOTH, padx=20)

    lb = CTkLabel(master=frag, text="", font=("Bell MT", 19))
    lb.pack(fill=X, pady=20, padx=20)

    if val== "M":
        
        lb.configure(text="Musician's data")
        h1 = CTkLabel(master=frag, text="SSN", font=("Bell MT", 19)).pack(pady=5, padx=12, side= LEFT, expand=True)
        h2 = CTkLabel(master=frag, text="Name", font=("Bell MT", 19)).pack(pady=5, padx=12, side= LEFT, expand=True)
        h3 = CTkLabel(master=frag, text="Address", font=("Bell MT", 19)).pack(pady=5, padx=12, side= LEFT, expand=True)
        h4 = CTkLabel(master=frag, text="Telephone", font=("Bell MT", 19)).pack(pady=5, padx=12, side= LEFT, expand=True)
        m_tree(fra)
        V_M()

    elif val== "S":
        lb.configure(text="Song's data")
        h1 = CTkLabel(master=frag, text="Song_ID", font=("Bell MT", 19)).pack(pady=5, padx=20, side= LEFT, expand=True)
        h2 = CTkLabel(master=frag, text="Title", font=("Bell MT", 19)).pack(pady=5, padx=20, side= LEFT, expand=True)
        h3 = CTkLabel(master=frag, text="Author", font=("Bell MT", 19)).pack(pady=5, padx=20, side= LEFT, expand=True)
        s_tree(fra)
        V_S()
    
    elif val== "A":
        lb.configure(text="Album's data")
        h1 = CTkLabel(master=frag, text="ID", font=("Bell MT", 19)).pack(pady=5, padx=5, side= LEFT, expand=True)
        h2 = CTkLabel(master=frag, text="Title", font=("Bell MT", 19)).pack(pady=5, padx=5, side= LEFT, expand=True)
        h3 = CTkLabel(master=frag, text="CopyrightDate", font=("Bell MT", 19)).pack(pady=5, padx=5, side= LEFT, expand=True)
        h4 = CTkLabel(master=frag, text="Format", font=("Bell MT", 19)).pack(pady=5, padx=5, side= LEFT, expand=True)
        h5 = CTkLabel(master=frag, text="Album_identifier", font=("Bell MT", 19)).pack(pady=5, padx=5, side= LEFT, expand=True)
        h6 = CTkLabel(master=frag, text="Producer", font=("Bell MT", 19)).pack(pady=5, padx=5, side= LEFT, expand=True)
        a_tree(fra)
        V_A()
    
    elif val== "I":
        lb.configure(text="Instrument's data")
        h1 = CTkLabel(master=frag, text="Instrument.ID", font=("Bell MT", 19)).pack(pady=5, padx=12, side= LEFT, expand=True)
        h2 = CTkLabel(master=frag, text="Name", font=("Bell MT", 19)).pack(pady=5, padx=12, side= LEFT, expand=True)
        h3 = CTkLabel(master=frag, text="Musicial_Key", font=("Bell MT", 19)).pack(pady=5, padx=12, side= LEFT, expand=True)
        i_tree(fra)
        V_I()

def add(val):
    fram2.pack_forget()
    global fram4, ae1, ae2, ae3, ae4, ae5, ae6
    fram4= CTkFrame(master=root, height=400, fg_color="#FFFFFF")
    fram4.pack(fill=BOTH, expand=True)

    f3=CTkFrame(master=fram4, fg_color="#FFFFFF")
    f3.pack(anchor=E)

    bt1 = CTkButton(master=f3, image=img5, text="", font=("Bell MT", 19), width=1, command=back_3)
    bt1.pack(side=RIGHT, padx=1)
    
    lb = CTkLabel(master=fram4, text="", font=("Bell MT", 19))
    lb.pack(fill=X,padx=20, pady=20)

    fra = CTkFrame(master=fram4, fg_color="#FFFFFF")
    fra.pack(fill=BOTH, padx=20, expand=TRUE)
    
    frag=CTkFrame(master=fram4, fg_color="#FFFFFF")
    frag.pack(expand=True, fill =BOTH)

    bt2 = CTkButton(master=frag, text="ADD", font=("Bell MT", 22), width=1)

    if val=="M":
        ae1= CTkEntry(master=frag, placeholder_text="SSN", font=("Bell MT", 19))
        ae1.pack(pady=10,side=LEFT, expand=TRUE)
        ae2= CTkEntry(master=frag, placeholder_text="Name", font=("Bell MT", 19))
        ae2.pack(pady=10,side=LEFT ,expand=TRUE)
        ae3= CTkEntry(master=frag, placeholder_text="Address", font=("Bell MT", 19))
        ae3.pack(pady=10,side=LEFT ,expand=TRUE)
        ae4= CTkEntry(master=frag, placeholder_text="Telephone", font=("Bell MT", 19))
        ae4.pack(pady=10,side=LEFT ,expand=TRUE)
        lb.configure(text="Musician")
        m_tree(fra)
        bt2.pack(padx= 30, side = LEFT)
        bt2.configure(command=A_M)
        V_M()

    elif val=="A":
        ae1= CTkEntry(master=frag, placeholder_text="ID", font=("Bell MT", 19), width=60)
        ae1.pack(pady=10, side=LEFT,expand=True)
        ae2= CTkEntry(master=frag, placeholder_text="Title", font=("Bell MT", 19), width=80)
        ae2.pack(pady=10, side=LEFT,expand=True)
        ae3= CTkEntry(master=frag, placeholder_text="CopyrightDate", font=("Bell MT", 19), width=105)
        ae3.pack(pady=10, side=LEFT,expand=True)
        ae4= CTkEntry(master=frag, placeholder_text="Format", font=("Bell MT", 19), width=50)
        ae4.pack(pady=10, side=LEFT,expand=True)
        ae5= CTkEntry(master=frag, placeholder_text="Album_identifier", font=("Bell MT", 19))
        ae5.pack(pady=10,side=LEFT, expand=True)
        ae6= CTkEntry(master=frag, placeholder_text="Producer", font=("Bell MT", 19))
        ae6.pack(pady=10,side=LEFT, expand=True)
        lb.configure(text="Album")
        a_tree(fra)
        bt2.pack(padx= 30, side = LEFT)
        bt2.configure(command=A_A)
        V_A()

    elif val=="S":
        ae1= CTkEntry(master=frag, placeholder_text="Song_ID", font=("Bell MT", 19))
        ae1.pack(padx=10, side=LEFT, expand=True)
        ae2= CTkEntry(master=frag, placeholder_text="Title", font=("Bell MT", 19))
        ae2.pack(pady=10, expand=True, side=LEFT)
        ae3= CTkEntry(master=frag, placeholder_text="Author", font=("Bell MT", 19))
        ae3.pack(pady=10, expand=True, side=LEFT)
        lb.configure(text="Song")
        s_tree(fra)
        bt2.pack(padx= 30, side = LEFT)
        bt2.configure(command=A_S)
        V_S()

    elif val=="I":
        ae1= CTkEntry(master=frag, placeholder_text="Instrument.ID", font=("Bell MT", 19))
        ae1.pack(pady=10, expand=True, side=LEFT)
        ae2= CTkEntry(master=frag, placeholder_text="Name", font=("Bell MT", 19))
        ae2.pack(pady=10, expand=True, side=LEFT)
        ae3= CTkEntry(master=frag, placeholder_text="Musicial_Key", font=("Bell MT", 19))
        ae3.pack(pady=10, expand=True, side=LEFT)
        lb.configure(text="Instrument")
        i_tree(fra)
        bt2.pack(padx= 30, side = LEFT)
        bt2.configure(command=A_I)
        V_I()

def edit(val):
    fram2.pack_forget()
    global fram5, h1, h2, h3, h4, h5
    fram5= CTkFrame(master=root, height=400, fg_color="#FFFFFF")
    fram5.pack(fill=BOTH, expand=True)

    f4=CTkFrame(master=fram5, fg_color="#FFFFFF")
    f4.pack(anchor=E)

    bt1 = CTkButton(master=f4, image=img5, text="", font=("Bell MT", 19), width=1, command=back_4)
    bt1.pack(side=RIGHT, padx=1)

    fra = CTkFrame(master=fram5, fg_color="#FFFFFF")
    fra.pack(fill=BOTH, padx=20, expand=TRUE)

    frag=CTkFrame(master=fram5, fg_color="#FFFFFF", height=100, width=400)
    frag.pack(fill=BOTH, padx=20 , pady=20, anchor=N)

    lb = CTkLabel(master=frag, text="", font=("Bell MT", 19))
    lb.pack(fill=X, pady=20, padx=20)

    bt2 = CTkButton(master=frag, text="UPDATE", font=("Bell MT", 19), width=1)
    bt2.pack(side=BOTTOM,padx=1, pady=30)
    
    if val== "M":
        m_tree(fra)
        lb.configure(text="Select the data to update:")
        h1 = CTkEntry(master=frag, placeholder_text="Name", font=("Bell MT", 19))
        h1.pack(pady=5, padx=12, side= LEFT, expand=True)
        h2 = CTkEntry(master=frag, placeholder_text="Address", font=("Bell MT", 19))
        h2.pack(pady=5, padx=12, side= LEFT, expand=True)
        h3 = CTkEntry(master=frag, placeholder_text="Telephone", font=("Bell MT", 19))
        h3.pack(pady=5, padx=12, side= LEFT, expand=True)
        bt2.configure(command=U_M)
        V_M()
    
    elif val== "A":
        a_tree(fra)
        lb.configure(text="Select the data to update:")
        h1 = CTkEntry(master=frag, placeholder_text="Title", font=("Bell MT", 19), width=70)
        h1.pack(pady=5, padx=5, side= LEFT, expand=True)
        h2 = CTkEntry(master=frag, placeholder_text="CopyrightDate", font=("Bell MT", 19), width=100)
        h2.pack(pady=5, padx=5, side= LEFT, expand=True)
        h3 = CTkEntry(master=frag, placeholder_text="Format", font=("Bell MT", 19), width=100)
        h3.pack(pady=5, padx=5, side= LEFT, expand=True)
        h4 = CTkEntry(master=frag, placeholder_text="Album_identifier", font=("Bell MT", 19))
        h4.pack(pady=5, padx=5, side= LEFT, expand=True)
        h5 = CTkEntry(master=frag, placeholder_text="Producer", font=("Bell MT", 19), width=100)
        h5.pack(pady=5, padx=5, side= LEFT, expand=True)
        bt2.configure(command=U_A)
        V_A()
    
    elif val== "I":
        i_tree(fra)
        lb.configure(text="Select the data to update:")
        h1 = CTkEntry(master=frag, placeholder_text="Name", font=("Bell MT", 19))
        h1.pack(pady=5, padx=12, side= LEFT, expand=True)
        h2 = CTkEntry(master=frag, placeholder_text="Musicial_Key", font=("Bell MT", 19))
        h2.pack(pady=5, padx=12, side= LEFT, expand=True)
        bt2.configure(command=U_I)
        V_I()
        
    elif val== "S":
        s_tree(fra)
        lb.configure(text="Select the data to update:")
        h1 = CTkEntry(master=frag, placeholder_text="Title", font=("Bell MT", 19))
        h1.pack(pady=5, padx=20, side= LEFT, expand=True)
        h2 = CTkEntry(master=frag, placeholder_text="Author", font=("Bell MT", 19))
        h2.pack(pady=5, padx=20, side= LEFT, expand=True)
        bt2.configure(command=U_S)
        V_S()

def delete(val):
    fram2.pack_forget()
    global fram6
    fram6= CTkFrame(master=root, height=400, fg_color="#FFFFFF")
    fram6.pack(fill=BOTH, expand=True)

    f5=CTkFrame(master=fram6, fg_color="#FFFFFF")
    f5.pack(anchor=E)

    bt1 = CTkButton(master=f5, image=img5, text="", font=("Bell MT", 19), width=1, command=back_5)
    bt1.pack(side=RIGHT, padx=1)
    
    frag=CTkFrame(master=fram6, fg_color="#FFFFFF", height=100, width=400)
    frag.pack(fill=BOTH, padx=20 , pady=20, anchor=N)
    
    fra = CTkFrame(master=fram6, fg_color="#FFFFFF")
    fra.pack(fill=BOTH, padx=20, expand=TRUE)

    lb = CTkLabel(master=frag, text="", font=("Bell MT", 19))
    lb.pack(fill=X,padx=20)

    bt2 = CTkButton(master=fram6, text="DELETE", font=("Bell MT", 19), width=1)
    bt2.pack(padx=1,pady=20)

    if val== "M":
        lb.configure(text="Select the data to delete:")
        h1 = CTkLabel(master=frag, text="SSN", font=("Bell MT", 19))
        h1.pack(pady=5, padx=12, side= LEFT, expand=True)
        h2 = CTkLabel(master=frag, text="Name", font=("Bell MT", 19))
        h2.pack(pady=5, padx=12, side= LEFT, expand=True)
        h3 = CTkLabel(master=frag, text="Address", font=("Bell MT", 19))
        h3.pack(pady=5, padx=12, side= LEFT, expand=True)
        h4 = CTkLabel(master=frag, text="Telephone", font=("Bell MT", 19))
        h4.pack(pady=5, padx=12, side= LEFT, expand=True)
        m_tree(fra)
        bt2.configure(command=D_M)
        V_M()
    
    elif val== "A":
        lb.configure(text="Select the data to delete:")
        h1 = CTkLabel(master=frag, text="ID", font=("Bell MT", 19)).pack(pady=5, padx=5, side= LEFT, expand=True)
        h2 = CTkLabel(master=frag, text="Title", font=("Bell MT", 19)).pack(pady=5, padx=5, side= LEFT, expand=True)
        h3 = CTkLabel(master=frag, text="CopyrightDate", font=("Bell MT", 19)).pack(pady=5, padx=5, side= LEFT, expand=True)
        h4 = CTkLabel(master=frag, text="Format", font=("Bell MT", 19)).pack(pady=5, padx=5, side= LEFT, expand=True)
        h6 = CTkLabel(master=frag, text="Album_identifier", font=("Bell MT", 19)).pack(pady=5, padx=5, side= LEFT, expand=True)
        h5 = CTkLabel(master=frag, text="Producer", font=("Bell MT", 19)).pack(pady=5, padx=5, side= LEFT, expand=True)
        a_tree(fra)
        bt2.configure(command=D_A)
        V_A()
    
    elif val== "I":
        lb.configure(text="Select the data to delete:")
        h1 = CTkLabel(master=frag, text="Instrument.ID", font=("Bell MT", 19)).pack(pady=5, padx=0, side= LEFT, expand=True)
        h2 = CTkLabel(master=frag, text="Name", font=("Bell MT", 19)).pack(pady=5, padx=10, side= LEFT, expand=True)
        h3 = CTkLabel(master=frag, text="Musicial_Key", font=("Bell MT", 19)).pack(pady=5, padx=12, side= LEFT, expand=True)
        i_tree(fra)
        bt2.configure(command=D_I)
        V_I()
        
    elif val== "S":
        lb.configure(text="Select the data to delete:")
        h3 = CTkLabel(master=frag, text="Song_ID", font=("Bell MT", 19)).pack(pady=5, padx=20, side= LEFT, expand=True)
        h1 = CTkLabel(master=frag, text="Title", font=("Bell MT", 19)).pack(pady=5, padx=20, side= LEFT, expand=True)
        h2 = CTkLabel(master=frag, text="Author", font=("Bell MT", 19)).pack(pady=5, padx=20, side= LEFT, expand=True)
        s_tree(fra)
        bt2.configure(command=D_S)
        V_S()

# Codes for Mysql

def V_M():
    cursor.execute("SELECT * FROM Musician")
    data = cursor.fetchall()

    for row in data:
        tree.insert("", "end", values=row)

def V_A():
    cursor.execute("SELECT * FROM Album")
    data = cursor.fetchall()

    for row in data:
        tree.insert("", "end", values=row)

def V_S():
    cursor.execute("SELECT * FROM Song")
    data = cursor.fetchall()

    for row in data:
        tree.insert("", "end", values=row)

def V_I():
    cursor.execute("SELECT * FROM Instrument")
    data = cursor.fetchall()

    for row in data:
        tree.insert("", "end", values=row)
        
def A_M():
    cursor.execute("INSERT INTO Musician (SSN, Name, Address, PhoneNumber) VALUES (%s, %s, %s, %s)", (ae1.get(), ae2.get(), ae3.get(), ae4.get()))
    db_connection.commit()
    tree.delete(*tree.get_children())
    V_M()

def A_A():
    cursor.execute("INSERT INTO Album (Album_ID, Title, CopyrightDate, Format, Album_Identifier, Producer_SSN) VALUES (%s, %s, %s, %s, %s, %s)", (ae1.get(), ae2.get(), ae3.get(), ae4.get(), ae5.get(), ae6.get()))
    db_connection.commit()
    tree.delete(*tree.get_children())
    V_A()

def A_S():
    cursor.execute("INSERT INTO Song (Song_ID, Title, Author) VALUES (%s, %s, %s)", (ae1.get(), ae2.get(), ae3.get()))
    db_connection.commit()
    tree.delete(*tree.get_children())
    V_S()

def A_I():
    cursor.execute("INSERT INTO Instrument (InstrumentID, Name, Musical_Key) VALUES (%s, %s, %s)", (ae1.get(), ae2.get(), ae3.get()))
    db_connection.commit()
    tree.delete(*tree.get_children())
    V_I()

def D_M():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        row_data = item['values']
        primary_key = row_data[0]
        cursor.execute("DELETE FROM Musician WHERE SSN=%s", (primary_key,))
        db_connection.commit()
        tree.delete(selected_item)
        tree.delete(*tree.get_children())
        V_M()

def D_A():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        row_data = item['values']
        primary_key = row_data[0]
        cursor.execute("DELETE FROM Album WHERE Album_ID=%s", (primary_key,))
        db_connection.commit()
        tree.delete(selected_item)
        tree.delete(*tree.get_children())
        V_A()

def D_S():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        row_data = item['values']
        primary_key = row_data[0]
        cursor.execute("DELETE FROM Song WHERE Song_ID=%s", (primary_key,))
        db_connection.commit()
        tree.delete(selected_item)
        tree.delete(*tree.get_children())
        V_S()

def D_I():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        row_data = item['values']
        primary_key = row_data[0]
        cursor.execute("DELETE FROM Instrument WHERE InstrumentID=%s", (primary_key,))
        db_connection.commit()
        tree.delete(selected_item)
        tree.delete(*tree.get_children())
        V_I()

def U_M():
    selected_item = tree.selection()
    item = tree.item(selected_item)
    row_data = item['values']
    SSN = row_data[0]
    cursor.execute("UPDATE Musician SET Name=%s, Address=%s, PhoneNumber=%s WHERE SSN=%s",(h1.get(), h2.get(), h3.get(), SSN))
    db_connection.commit()
    tree.delete(*tree.get_children())
    V_M()

def U_A():
    selected_item = tree.selection()
    item = tree.item(selected_item)
    row_data = item['values']
    Album_ID = row_data[0]
    cursor.execute("UPDATE Album SET Title=%s, CopyrightDate=%s, Format=%s, Album_Identifier=%s, Producer_SSN=%s WHERE Album_ID=%s",(h1.get(), h2.get(), h3.get(), h4.get(), h5.get(),Album_ID))
    db_connection.commit()
    tree.delete(*tree.get_children())
    V_A()

def U_I():
    selected_item = tree.selection()
    item = tree.item(selected_item)
    row_data = item['values']
    InstrumentID = row_data[0]
    cursor.execute("UPDATE Instrument SET Name=%s, Musical_key=%s WHERE InstrumentID=%s",(h1.get(), h2.get(), InstrumentID))
    db_connection.commit()
    tree.delete(*tree.get_children())
    V_I()

def U_S():
    selected_item = tree.selection()
    item = tree.item(selected_item)
    row_data = item['values']
    Song_ID = row_data[0]
    cursor.execute("UPDATE Song SET Title=%s, Author=%s WHERE Song_ID=%s",(h1.get(), h2.get(), Song_ID))
    db_connection.commit()
    tree.delete(*tree.get_children())
    V_S()

def m_tree(val):
    scrollbar = ttk.Scrollbar(master=val, orient="vertical")
    scrollbar.pack(side="right",fill="y")
    global tree
    tree = ttk.Treeview(val, columns=("SSN", "Name", "Address", "TelePhone"), show="headings", yscrollcommand=scrollbar.set)
    tree.heading("SSN", text="SSN")
    tree.heading("Name", text="Name")
    tree.heading("Address", text="Address")
    tree.heading("TelePhone", text="TelePhone")
    tree.column("SSN", width=100)
    tree.pack(fill="both",expand=True)

def a_tree(val):
    scrollbar = ttk.Scrollbar(master=val, orient="vertical")
    scrollbar.pack(side="right",fill="y")
    global tree
    tree = ttk.Treeview(val, columns=("ID", "Title", "CopyrightDate", "Format", "Album_identifier", "Producer"), show="headings", yscrollcommand=scrollbar.set)
    tree.heading("ID", text="ID")
    tree.heading("Title", text="Title")
    tree.heading("CopyrightDate", text="CopyrightDate")
    tree.heading("Format", text="Format")
    tree.heading("Producer", text="Producer")
    tree.heading("Album_identifier", text="Album_identifier")
    tree.column("ID", width=50)
    tree.column("Title", width=80)
    tree.column("CopyrightDate", width=160)
    tree.column("Format", width=110)
    tree.column("Album_identifier", width=120)
    tree.pack(fill="both",expand=True)

def i_tree(val):
    scrollbar = ttk.Scrollbar(master=val, orient="vertical")
    scrollbar.pack(side="right",fill="y")
    global tree
    tree = ttk.Treeview(val, columns=("Instrument.ID", "Name", "Musicial_Key"), show="headings", yscrollcommand=scrollbar.set)
    tree.heading("Instrument.ID", text="Instrument.ID")
    tree.heading("Name", text="Name")
    tree.heading("Musicial_Key", text="Musicial_Key")
    tree.pack(fill="both",expand=True)

def s_tree(val):
    scrollbar = ttk.Scrollbar(master=val, orient="vertical")
    scrollbar.pack(side="right",fill="y")
    global tree
    tree = ttk.Treeview(val, columns=("Song_ID","Title", "Author"), show="headings", yscrollcommand=scrollbar.set)
    tree.heading("Title", text="Title")
    tree.heading("Author", text="Author")
    tree.heading("Song_ID", text="Song_ID")
    tree.pack(fill="both",expand=True)

def conf(x,y):
    global count
    global lc
    if count >1:
        lc.pack_forget()
    count+=1
    if x.get()=="Nischal":
        if y.get()=="Ojha":
            admin()
        else:
            lc=CTkLabel(master=fram,text="Invalid password", font=("Bell, MT", 19))
            lc.pack(padx=10, pady=20)
    else:
        lc=CTkLabel(master=fram,text="Invalid username", font=("Bell, MT", 19))
        lc.pack(padx=10, pady=20)
    # admin()

def back_N():
    framn.pack_forget()
    front()   
def back_P():
    fram.pack_forget()
    front()
def back():
    fram2.pack_forget()
    front()
def back_2(a):
    fram3.pack_forget()
    if a == "A":
        admin()
    elif a == "N":
        normal()
    else:
        print("Error")
def back_3():
    fram4.pack_forget()
    admin()
def back_4():
    fram5.pack_forget()
    admin()
def back_5():
    fram6.pack_forget()
    admin()

front()
root.mainloop()
