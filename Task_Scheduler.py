#Task Scheduler With GUI
from tkinter import *
from tkinter import ttk
import re
from tkinter import messagebox
from PIL import Image,ImageTk
main_window = Tk() # Base Window
main_window.title('To Do List Application')# Giving title to base window
main_window.attributes('-fullscreen',True) # setting base window size 
tab_ctrl = ttk.Notebook(main_window) # Creating tab 
tab_1_frame = Frame(tab_ctrl) # creating frame for tab 1
tab_1_frame.pack()
tab_1_frame.config(bg='Sky Blue')
tab_2_frame = Frame(tab_ctrl) # creating frame for tab 2
tab_2_frame.pack()
tab_2_frame.config(bg='Sky Blue')
tab_3_frame = Frame(tab_ctrl) # creating frame for tab 3
tab_3_frame.pack()
tab_3_frame.config(bg='Sky Blue')
test_frame = Frame(tab_1_frame) #creating one more frame in tab_1_frame for displaying heading
test_frame.pack()
test_frame.config(bg='Black')
to_do_list_img = Image.open('c:\\Prathamesh\\python_txt_files\\to_do_list_icon.jpg')
update_to_do_img = to_do_list_img.resize((60,60))
final_update_to_do_img = ImageTk.PhotoImage(update_to_do_img)
title = Label(test_frame,text='To-Do List Application',bg='Yellow',font=('cambria',20,'bold'),compound=RIGHT,image=final_update_to_do_img) #Lable with heading
title.pack(ipadx=10,ipady=10,padx=10,pady=10)
all_the_best = Image.open('c:\\Prathamesh\\python_txt_files\\all_the_best.jpg')
update_all_the_best_img = all_the_best.resize((60,60))
final_all_the_best_img = ImageTk.PhotoImage(update_all_the_best_img)
tab_2_head_label = Label(tab_2_frame,text='Follwing Are List Of Tasks That You Have To Complete ,All The Best !!!',bg='Sky Blue',image=final_all_the_best_img,compound=RIGHT,font=('cambria',15,'bold'))
tab_2_head_label.pack(padx=10,pady=10)
z = StringVar() # variable which stores string passed by entry
frame_1 = Frame(tab_2_frame)
frame_1.pack(padx=10,pady=10)
scroll = Scrollbar(frame_1)
scroll.pack(side=RIGHT,fill=Y)
w8 = Listbox(frame_1,yscrollcommand=scroll.set,height=10,width=50,font=('cambria',15,'bold')) # Creating list box in which i will insert tasks later
w8.pack(padx=5,pady=5,side=LEFT)
scroll.config(command=w8.yview)
w15 = Label(tab_3_frame,text='Note :- Please Select Task That You Want To Edit & Then Click On Edit Button and \
At The End Click On Save Edited Task Button To Save Task ',fg='Red',bg='Yellow',font=('cambria',15,'bold')) #Creating label with text colour red 
w15.pack(padx=10,pady=10)
frame_2 = Frame(tab_3_frame)
frame_2.pack(padx=10,pady=10)
scroll_1 = Scrollbar(frame_2)
scroll_1.pack(side=RIGHT,fill=Y)
w10 = Listbox(frame_2,yscrollcommand=scroll_1.set,height=10,width=50,font=('cambria',15,'bold'))# Creating list box in which i will insert tasks later
w10.pack(padx=5,pady=5,side=LEFT)
scroll_1.config(command=w10.yview)
count = 1
def add():# When i will press add this task button add() function will call
    final_entry.pack_forget()
    save_edited_btn.pack_forget()
    w = re.match(' ',w5.get())
    e = re.findall('[0-9]',w5.get())
    t = re.findall('[A-Za-z]',w5.get())
    if w:
        messagebox.showerror('Error !!!','Fist Letter Is Space')
        w5.delete(0,END)
    else:
        if t:
            if e:
                messagebox.showerror('Error!!!','You Cannot Add Numbers As A Task')
                w5.delete(0,END)
            else:
                global count
                w2.config(text=f'{count} tasks added sucessfully !!',fg='Red',font=('cambria',15,'bold'),bg='Sky Blue') #Label with dynamic text
                w2.pack(ipadx=5,ipady=5,padx=5,pady=5)
                w8.insert(0,w5.get()) #inserting task from entries into listbox 
                w10.insert(0,w5.get()) #inserting task from entries into listbox 
                w5.delete(0,END) #Clearing entry       
                count += 1 
                edit_label.pack_forget()
        else:
            messagebox.showerror('Error!!!','You Are Pressing Add This Task Button Without Inserting Task')
            w5.delete(0,END)
def final_update():# When i will press Save Edited Task button final_update() function will call
    a = re.match(' ',final_entry.get())
    s = re.findall('[0-9]',final_entry.get())
    d = re.findall('[A-Za-z]',final_entry.get())
    if a:
        messagebox.showerror('Error','First Letter Is Space')
        final_entry.delete(0,END)
    else:
        if s:
            messagebox.showerror('Error','Numbers Are Not Allowed')
            final_entry.delete(0,END)
        else:
            if d:
                for i in w10.curselection(): #Implementing for loop on list box with curselection method to get selected entry
                    w10.delete(i)
                    w10.insert(END,z.get())
                    w8.delete(i)
                    w8.insert(END,z.get())
                    final_entry.delete(0,END)
                    frame_4.pack_forget()
                    save_edited_btn.pack_forget()
            else:
                messagebox.showerror('Error','Invalid Input')
                final_entry.delete(0,END)
def tab_3_button():# When i will press Edit button tab_3_button() function will call
    frame_4.pack(padx=10,pady=10)
    edit_label.pack(side=LEFT)  
    final_entry.config(textvariable=z,font=('cambria',15,'bold'))#crating entry with textvariable z which will store task
    final_entry.pack(padx=10,pady=10,ipadx=5,ipady=5,side=LEFT)
    save_edited_btn.config(text='Save Edited Task',command=final_update,font=('cambria',15,'bold'),bg='sandybrown',activebackground='Tomato') #refer line no 24
    save_edited_btn.pack(ipadx=5,ipady=5,padx=5,pady=5)
exit_img = Image.open('c:\\Prathamesh\\python_txt_files\\exit.jpg')
update_exit_img = exit_img.resize((40,40))
final_update_exit_img = ImageTk.PhotoImage(update_exit_img)
tab_ctrl.add(tab_1_frame,text='Add Task')#Adding tab
frame_3 = Frame(tab_1_frame,bg='Sky Blue')
frame_3.pack(padx=10,pady=10)
arrow_img = Image.open('c:\\Prathamesh\\python_txt_files\\next_arrow.jpg')
update_arrow_img = arrow_img.resize((40,40))
final_arrow_img = ImageTk.PhotoImage(update_arrow_img)
w4 = Label(frame_3,text='Please Add Your  Task --->',font=('cambria',15,'bold'),bg='Sky Blue') #Creating Label
w4.pack(padx=5,pady=5,ipadx=5,ipady=5,side=LEFT)
w5 = Entry(frame_3,font=('cambria',15,'bold')) #Creating Entry
w5.pack(side=LEFT)
add_img = Image.open('c:\\Prathamesh\\python_txt_files\\addition.jpg')
update_add_img = add_img.resize((40,40))
final_update_add_img = ImageTk.PhotoImage(update_add_img)
w7 = Button(tab_1_frame,text='Add This Task',command=add,font=('cambria',15,'bold'),bg='sandybrown',activebackground='Tomato',image=final_update_add_img,compound=RIGHT) #Refer line no.29
w7.pack(ipadx=5,ipady=5,padx=10,pady=10)
w6 = Button(tab_1_frame,text='Exit',command=main_window.destroy,font=('cambria',15,'bold'),bg='sandybrown',activebackground='tomato',image=final_update_exit_img,compound=RIGHT) #Button with built in destroy method
w6.pack(ipadx=5,ipady=5,padx=10,pady=10)
w2 = Label(tab_1_frame) #creating label with dynamic text
w2.pack_forget()# Disappering here but it will pack once if i press add task button
tab_ctrl.pack(expand=1,fill=BOTH)#Packing tab
tab_ctrl.add(tab_2_frame,text='View Tasks List') # Adding tab no.2
tab_ctrl.add(tab_3_frame,text='Edit Task') # Adding tab no.3
edit_img = Image.open('c:\\Prathamesh\\python_txt_files\\edit_img.jpg')
update_edit_img = edit_img.resize((40,40))
final_update_edit_img = ImageTk.PhotoImage(update_edit_img)
w1 = Button(tab_3_frame,text='Edit',command=tab_3_button,font=('cambria',15,'bold'),bg='sandybrown',activebackground='tomato',image=final_update_edit_img,compound=RIGHT) # Refer line no. 43
w1.pack(ipadx=5,ipady=5,padx=5,pady=5)
w13 = Button(tab_2_frame,text='Exit',command=main_window.destroy,font=('cambria',15,'bold'),bg='sandybrown',activebackground='tomato',image=final_update_exit_img,compound=RIGHT) #Button with built in destroy method
w13.pack(ipadx=5,ipady=5,padx=10,pady=10)
w14 = Button(tab_3_frame,text='Exit',command=main_window.destroy,font=('cambria',15,'bold'),bg='sandybrown',activebackground='tomato',image=final_update_exit_img,compound=RIGHT) #Button with built in destroy method
w14.pack(ipadx=5,ipady=5,padx=5,pady=5)
frame_4 = Frame(tab_3_frame)
frame_4.config(bg='Sky Blue')
frame_4.pack_forget()
edit_label = Label(frame_4,text='Edit You Task Here ---->',font=('cambria',15,'bold'),bg='SKy Blue')
edit_label.pack_forget()
#Static Widgets :- 
final_entry = Entry(frame_4)
final_entry.pack_forget()
save_edited_btn = Button(tab_3_frame)
save_edited_btn.pack_forget()
main_window.mainloop() #Main Event 
#Thank You !!!!