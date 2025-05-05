#Note :- some GUI and other improvement is needed 
from tkinter import *
from tkinter import filedialog,messagebox
from datetime import datetime
from PIL import Image,ImageTk
import time
upto = datetime(2025,5,2)
root = Tk()
root.title('Hari Om')
root.config(bg='Light Blue')
root.geometry('500x500+84+75')
def not_working_assigment_case():
    final_message.config(text='You have already crossed deadline for given assigment now meet in lecture for understanding further process ')
    final_message.pack(padx=10,pady=10)
    add_assignment_btn.pack_forget()
def add_assignment_btn_func():
    current_time = datetime.now()
#extracting_current_month = current_time.strftime('%m')
#extracting_current_year = current_time.strftime('%Y')
    if current_time <= upto:
        path_giver = filedialog.askopenfilename(initialdir='\\',filetypes=(('Pdf files','*.pdf'),('All files','*.*')),title='Select Assignment')
        if path_giver:
            final_message.config(text='Your assignment is sucessfully submitted (You might get 5 marks extra for submitting assignment in time !!)')
            final_message.pack(padx=10,pady=10)
            add_assignment_btn.pack_forget()
        else:
            messagebox.showerror('Warning !!!','Please Select File ')
    else:
        not_working_assigment_case()
main_label_frame = Frame(root)
main_label_frame.config(bg='Black',bd=4)
main_label_frame.pack(padx=10,pady=10)
main_heading = Label(main_label_frame,text='Assignment Taker',bg='Light Blue',font=('Cambria',20,'bold'))
main_heading.pack(padx=10,pady=10,ipadx=5,ipady=5)
add_btn_img = Image.open('c:\\Prathamesh\\python_txt_files\\addition.jpg')
updating_add_btn_img = add_btn_img.resize((40,40))
final_add_btn_img = ImageTk.PhotoImage(updating_add_btn_img)
add_assignment_btn = Button(root,text='Attach Assigment',command=add_assignment_btn_func,image=final_add_btn_img,borderwidth=10,compound='right',font=('cambira',14,'bold'),activebackground='Red')
add_assignment_btn.pack(padx=10,pady=10,ipadx=5,ipady=5)

#Static Widgets
final_message = Label(root,text='Dynamic',bg='Light Blue',font=('Cambria',20,'bold'))
final_message.pack_forget()
root.mainloop()
