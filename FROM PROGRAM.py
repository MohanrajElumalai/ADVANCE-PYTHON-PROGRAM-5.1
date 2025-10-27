from tkinter import *
root = Tk(); root.title("FROM")

Label(root,text="TAKSHASHILS UNVERSITY").pack()

Label(root,text="Student Information").pack()

for t in ["Enrollment No","Name","DOB","Language","Phone No"]:
    
    Label(root,text=t).pack(); Entry(root).pack()
    
Button(root,text="Save",bg="green",fg="white").pack(side=LEFT,padx=20,pady=10)
Button(root,text="Cancel",bg="red",fg="white",command=root.destroy).pack(side=RIGHT,padx=20,pady=10)

root.mainloop()
