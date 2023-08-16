from tkinter import *
import string
import random




def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_Box.get())

    #password=random.sample(all,password_length)
    #passwordField.insert(0,password)

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))


    if choice.get() == 2:
        passwordField.insert(0, random.sample(small_alphabets+capital_alphabets, password_length))

    if choice.get() == 3:
        passwordField.insert(0, random.sample(all,password_length))








root=Tk()
root.geometry("400x550+400+100")

root.config(bg="dark blue")
choice=IntVar()
Font=('arial',13,'bold')

passwordLabel=Label(root,text="Password Generator",font=("times new roman",20,"bold"),bg="dark blue",fg="white")
passwordLabel.grid(pady=10,padx=50)

weakradioButton=Radiobutton(root,text="Weak",value=1,variable=choice,width=13,height=3)
weakradioButton.grid(pady=5)

mediumadioButton=Radiobutton(root,text="Medium",value=2,variable=choice,width=13,height=3)
mediumadioButton.grid(pady=5)

strongadioButton=Radiobutton(root,text="Strong",value=3,variable=choice,width=13,height=4)
strongadioButton.grid(pady=5)

lengthLabel=Label(root,text="Password Length",font=15,bg="dark blue",fg="white")
lengthLabel.grid(pady=5)

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.grid(pady=5)

generateButton=Button(root,text='Generate',font=Font,command=generator,height=2,width=15)
generateButton.grid(pady=5)


passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid(pady=5)

#copyButton=Button(root,text='Copy',font=Font,command=copy,height=2,width=15)
#copyButton.grid(pady=5)




root.mainloop()