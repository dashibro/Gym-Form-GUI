import tkinter
from PIL import Image,ImageTk
root = tkinter.Tk()
root.title("Gym Classes")
root.geometry("1000000x1000")
root.configure(bg="black")

def resistor():
    def clear_message(label):
        label.destroy()

    if(fname.get() == "" or lname.get() == ""):
      name_message = tkinter.Label(text="You can not leave name empty",bg="black",fg="white",font="none 10 bold")
      name_message.place(x=670,y=740)
      root.after(2000, clear_message, name_message)
    elif(email.get() == "" or "@gmail.com" not in email.get()):
      email_message = tkinter.Label(text="Enter a valid email",bg="black",fg="white",font="none 10 bold")
      email_message.place(x=710,y=740)
      root.after(2000, clear_message, email_message)
    elif(phno.get() == "" or not phno.get().isdigit() or len(phno.get()) < 10):
      phno_message = tkinter.Label(text="Enter a valid phone number",bg="black",fg="white",font="none 10 bold")
      phno_message.place(x=690,y=740)
      root.after(2000, clear_message, phno_message)
    elif(age.get() == "" or not age.get().isdigit()):
       age_message = tkinter.Label(text="Entering age is compulsory",bg="black",fg="white",font="none 10 bold")
       age_message.place(x=690,y=740)
       root.after(2000, clear_message, age_message)
    elif(dob.get() == "" or not dob.get().isdigit()):
       dob_message = tkinter.Label(text="Please enter date of birth",bg="black",fg="white",font="none 10 bold")
       dob_message.place(x=690,y=740)
       root.after(2000, clear_message, dob_message)
    elif(gender.get() == "other"):
       gender_message = tkinter.Label(text="Please select your gender",bg="black",fg="white",font="none 10 bold")
       gender_message.place(x=690,y=740)
       root.after(2000, clear_message, gender_message)
    else:
       file = open("Entries.txt","a")
       file.write(f"First Name: {fname.get()}\n")
       file.write(f"Last Name: {lname.get()}\n")
       file.write(f"Email: {email.get()}\n")
       file.write(f"Phone Number: {phno.get()}\n")
       file.write(f"Age: {age.get()}\n")
       file.write(f"DOB: {dob.get()}\n")
       file.write(f"Gender: {gender.get()}\n")
       file.write("-" * 40 + "\n")
       file.close()
    success_label =tkinter.Label(text="Submitted successfuly",bg="black",fg="white",font="none 10 bold")
    success_label.place(x=690,y=740)
    root.after(2000, clear_message, success_label)
       
      
# Title
tkinter.Label(root,text="Gym Resistration",font="monsterrate 25 bold",bg="black",fg="White",pady=9).pack()

#Image
image = Image.open("gym.jpg")
Photo = image.resize((300,400))
photo = ImageTk.PhotoImage(Photo)
tkinter.Label(image=photo,bg="black").place(x=610,y=50)

# Full Name
tkinter.Label(text="Full Name",bg="black",fg="white",font="bold").place(x=430,y=330)
fname = tkinter.StringVar()
lname = tkinter.StringVar()
tkinter.Entry(root,textvariable=fname,width=50).place(x=430,y=365)
tkinter.Label(text="First Name",bg="black",fg="white",font="None  10 bold").place(x=430,y=392)

tkinter.Entry(root,textvariable=lname,width=50).place(x=800,y=365)
tkinter.Label(text="Last Name",bg="black",fg="white",font="None  10 bold").place(x=800,y=392)

# Email ID
tkinter.Label(text="Email ID",bg="black",fg="white",font="bold").place(x=430,y=440)
email = tkinter.StringVar()
tkinter.Entry(root,textvariable=email,width=50).place(x=430,y=472)

# Phone NO.
tkinter.Label(text="Phone Number",bg="black",fg="white",font="bold").place(x=800,y=440)
phno = tkinter.StringVar()
tkinter.Entry(root,textvariable=phno,width=50).place(x=800,y=472)

# Age
tkinter.Label(text="Age",bg="black",fg="white",font="bold").place(x=430,y=510)
age = tkinter.StringVar()
tkinter.Entry(root,textvariable=age,width=50).place(x=430,y=542)

# DOB
tkinter.Label(text="DOB",bg="black",fg="white",font="bold").place(x=800,y=510)
dob = tkinter.StringVar()
tkinter.Entry(root,textvariable=dob,width=50).place(x=800,y=542)


# Gender
tkinter.Label(text="Gender",bg="black",fg="white",font="bold").place(x=430,y=580)
gender = tkinter.StringVar()
gender.set("other")
tkinter.Radiobutton(root,text="Male",variable=gender,value="M",bg="black",fg="white",font="bold").place(x=500,y=610)
tkinter.Radiobutton(root,text="Female",variable=gender,value="F",bg="black",fg="white",font="bold").place(x=900,y=610)

# Submit Button
tkinter.Button(root,text="Submit",bg="black",fg="white",font="bold",command=resistor).place(x=730,y=690)

root.mainloop()