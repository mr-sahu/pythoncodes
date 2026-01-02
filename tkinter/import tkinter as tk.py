
# Tk()Main Window Properties

#  root = tk.Tk()
# Creates the main window.

# root.title("My App")
# Sets window title.

#  root.geometry("500x400")
# Sets window size → width x height

#  root.configure(bg="color")
# Sets background color.

#  root.resizable(False, False)
# Disable window resizing.

##****************** common widget properties ************************

## These properties apply to most widgets like Label, Button, Entry, Frame etc.
# 1. text  ---->text="Hello"
# 1. font  ---->font=("Arial", 14, "bold")
# 1. fg / foreground   ---->fg="yellow"
# 1. fg / background   ---->bg="yellow"
# 1. padx / pady    ---->padx=10, pady=5
# 1. width / height ----->  Size of widget (in characters, not pixels).




## ************************ Geometry Managers *******************************************
# 1.pack()
#Simple vertical/horizontal layout.
# used as =======>   widget.pack(side="left", padx=10, pady=10)

# 2.grid()
#STable-like layout.
# used as =======>   widget.grid(row=0, column=1)


# 3.place()
#Exact (x, y) position.
# used as =======>   widget.place(x=50, y=40)



# 4.pack()
#Simple vertical/horizontal layout.
# used as =======>   widget.pack(side="left", padx=10, pady=10)

# import tkinter as tk
# root=tk.Tk()
# root.title("Button")
# mybutton=tk.Button(root,text="Save",foreground="White",background="Red",padx=5,pady=5)
# mybutton.pack(padx=20,pady=50)
# root.mainloop()


##  *************************************show message box........****************************
# from tkinter import messagebox
# messagebox.showinfo("Title", "Message")


# ******************** frame wiidget ******************************

# import tkinter as tk
# root=tk.Tk()
# root.title("Frame")

# my_Frames=tk.Frame(background="Red",height=100,width=100)
# my_Frames.pack()
# inside_Text=tk.Label(my_Frames,text="Inside of Frame",bg="Yellow")
# inside_Text.pack()
# root.mainloop()
# ***************************  entry widget **************************

# import tkinter as tk
# root=tk.Tk()
# root.title("Entry Widget") # entry widget is just like textfield

# enty=tk.Entry(root,width=30)
# enty.pack()
# root.mainloop()


# show how entry widget get text

# import tkinter as tk
# root=tk.Tk()

# ent=tk.Entry(width=30)
# ent.pack()
# def entryText():
#     print("you typed",ent.get())

# btn=tk.Button(root,text="Get text",command=entryText) 
# btn.pack()
# root.mainloop()


# # practice


# import tkinter as tk
# root=tk.Tk()
# textField=tk.Entry(width=30)
# textField.pack()
# def saveData():
#     print("you type.... ",textField.get())
# bttn=tk.Button(root,text="Save",command=saveData,padx=5,pady=5)
# bttn.pack()
# root.mainloop()


# #************************* text widget *************************** type 1
# import tkinter as tk
# root=tk.Tk()
# root.title("Text widget")
# txt=tk.Text(root,width=20,height=10)
# txt.pack()
# root.mainloop()

# # type 2 **********************************************************************
# import tkinter as tk
# root=tk.Tk()
# txt1=tk.Text(root,width=50,height=10)
# txt1.insert('1.0',"Hello this is text inside text place holder")
# txt1.pack()
# root.mainloop()

# # type 3 ***************scroll bar ***************************************************************
# import tkinter as tk
# root=tk.Tk()

# frm1=tk.Frame(root)
# frm1.pack()
# scrl=tk.Scrollbar(frm1)
# scrl.pack(side="right",fill="y")
# txt2=tk.Text(frm1,width=30,height=10,yscrollcommand=scrl.set)
# txt2.insert("1.0","This is for scroll bar at right side")
# txt2.pack()
# scrl.config(command=txt2.yview)
# root.mainloop()




#********* practice scroll bar*****************************




# import tkinter as tk
# root=tk.Tk()
# frm2=tk.Frame(root)
# frm2.pack()
# scr2=tk.Scrollbar(frm2)
# scr2.pack(side="right",fill="y")
# txt3=tk.Text(frm2,width=30,height=10,yscrollcommand=scr2.set)
# txt3.insert("1.0","This is practice for scrollbar inside frame")
# txt3.pack()

# scr2.config(command=txt3.yview)
# root.mainloop()

# ****************************list box widget***************************************************

# import tkinter as tk
# root=tk.Tk()
# lstBox=tk.Listbox(root)
# lstBox.pack()
# lstBox.insert(1,"mango")
# lstBox.insert(2,"banana")
# lstBox.insert(3,"cherry")
# root.mainloop()


#**************** list box practice ******************************


# import tkinter as tk
# root=tk.Tk()
# lst1=tk.Listbox(root)
# lst1.pack()
# lst1.insert(1,"Lucknow")
# lst1.insert(2,"Tokyo")
# lst1.insert(3,"Berline")
# lst1.insert(4,"Denver")
# lst1.insert(5,"Hanoi")
# lst1.insert(6,"Nairobi")
# lst1.insert(7,"Professor")
# lst1.insert(8,"Camelia")
# root.mainloop()


## buttonat all side........................................
# import tkinter as tk

# root = tk.Tk()

# tk.Button(root, text="Top").pack(side="top")
# tk.Button(root, text="Bottom").pack(side="bottom")
# tk.Button(root, text="Left").pack(side="left")
# tk.Button(root, text="Right").pack(side="right")

# root.mainloop()








