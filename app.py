from tkinter import *
import tkinter.messagebox
from verify_email import *
from validate_email import *
import threading


class Email:
    def __init__(self,root):
        self.root=root
        self.root.title("Email Verification")
        self.root.geometry("500x250")
        self.root.iconbitmap("logo220.ico")
        self.root.resizable(0,0)

        email=StringVar()
       


#=================================================================================#

        def clear():
            email.set("")
            text.delete("1.0","end")



        
        def verify():
            if email.get()!="":
                text.delete("1.0","end")


                answer=verify_email(email.get())
                if answer:
                    ans="The email is valid"
                    text.insert("end",ans)
                else:
                    ans="The email is invalid"
                    text.insert("end",ans)           
            else:
                tkinter.messagebox.showerror("Error","Please Enter Valid Email")

            
        
        def thread_verfiy():
            t=threading.Thread(target=verify)
            t.start()




        def validate():
            if email.get()!="":
                text.delete("1.0","end")

                answer=validate_email(email.get())
                if answer:
                    ans="The email is valid"
                    text.insert("end",ans)
                else:
                    ans="The email is invalid"
                    text.insert("end",ans)

            else:
                tkinter.messagebox.showerror("Error","Please Enter Valid Email")



  
                
           
                

#==================================================================================#
        def on_enter1(e):
            but_verify['background']="black"
            but_verify['foreground']="cyan"
  
        def on_leave1(e):
            but_verify['background']="SystemButtonFace"
            but_verify['foreground']="SystemButtonText"

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        def on_enter3(e):
            but_validate['background']="black"
            but_validate['foreground']="cyan"
  
        def on_leave3(e):
            but_validate['background']="SystemButtonFace"
            but_validate['foreground']="SystemButtonText"

#==================================================================================#
        mainframe=Frame(self.root,width=500,height=250,bd=3,relief="ridge")
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=494,height=150,bd=3,relief="ridge")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=93,bd=3,relief="ridge")
        secondframe.place(x=0,y=150)

#================================firstframe===================================================#

        lab_frame=LabelFrame(firstframe,width=488,height=145,text="Email Verification",bg="#89b0ae",fg="white")
        lab_frame.place(x=0,y=0)
#==============================================================================================#


        lab=Label(lab_frame,text="Enter Email",font=('times new roman',12),bg="#89b0ae")
        lab.place(x=30,y=5)

        ent_search=Entry(lab_frame,width=37,font=('times new roman',12),bd=3,relief="ridge",textvariable=email)
        ent_search.place(x=130,y=5)


        but_verify=Button(lab_frame,width=13,text="Verify",font=('times new roman',12),cursor="hand2",command=thread_verfiy)
        but_verify.place(x=20,y=80)
        but_verify.bind("<Enter>",on_enter1)
        but_verify.bind("<Leave>",on_leave1)


        but_validate=Button(lab_frame,width=13,text="Validate",font=('times new roman',12),cursor="hand2",command=validate )
        but_validate.place(x=180,y=80)
        but_validate.bind("<Enter>",on_enter3)
        but_validate.bind("<Leave>",on_leave3)

        but_clear=Button(lab_frame,width=13,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=340,y=80)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)

#=============================================================================================================#

        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(secondframe,height=4,width=58,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text.place(x=0,y=0)
        scol.config(command=text.yview)
  


if __name__ == "__main__":
    root=Tk()
    app=Email(root)
    root.mainloop()