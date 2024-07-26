#With GUI :- 
from tkinter import *
from tkinter import messagebox
import re
from PIL import Image,ImageTk
from datetime import *
import webbrowser
root = Tk()
root.title('Chant Counter')
root.config(bg='lemonchiffon')
root.attributes('-fullscreen',1)
x = 0
q = StringVar()
def jaap_btn_count():
    frame_2.pack_forget()
    w4.pack_forget()
    save_btn_label.pack_forget()
    final_save.pack_forget()
    list_box.pack_forget()
    sucess.pack_forget()
    about_label.pack_forget()
    gmail_btn.pack_forget()
    insta_btn.pack_forget()
    linkdin_btn.pack_forget()
    global x
    x += 1
    w1.config(text='Your Count :- '+str(x),font=('Cambria',25,'bold'))
    w1.pack(padx=5,pady=5)
    save_btn.pack(padx=5,pady=5)
def decrease_count():
    frame_2.pack_forget()
    w4.pack_forget()
    save_btn_label.pack_forget()
    final_save.pack_forget()
    sucess.pack_forget()
    list_box.pack_forget()
    about_label.pack_forget()
    gmail_btn.pack_forget()
    insta_btn.pack_forget()
    linkdin_btn.pack_forget()
    global x
    x -= 1
    w1.config(text='Your Count = '+str(x),font=('Cambria',25,'bold'))
    w1.pack(padx=5,pady=5)
    save_btn.pack(padx=5,pady=5)
def reset_count():
    frame_2.pack_forget()
    w4.pack_forget()
    save_btn_label.pack_forget()
    final_save.pack_forget()
    sucess.pack_forget()
    list_box.pack_forget()
    save_btn.pack_forget()
    about_label.pack_forget()
    gmail_btn.pack_forget()
    insta_btn.pack_forget()
    linkdin_btn.pack_forget()
    global x
    x = 0
    w1.config(text='Your Count = '+str(x),font=('Cambria',25,'bold'))
    w1.pack(padx=5,pady=5)
def view_jaap_func():
    w1.pack_forget()
    w4.pack_forget()
    sucess.pack_forget()
    save_btn_label.pack_forget()
    final_save.pack_forget()
    save_btn.pack_forget()
    about_label.pack_forget()
    gmail_btn.pack_forget()
    insta_btn.pack_forget()
    linkdin_btn.pack_forget()
    scroll.pack(side=RIGHT,fill=Y)
    list_box.config(height=5,width=50,font=('cambria',15,'bold'))
    list_box.pack(side=LEFT,fill=BOTH)
    scroll.config(command=list_box.yview)
    frame_2.pack()
def save_btn_func():
    frame_2.pack_forget()
    list_box.pack_forget()
    sucess.pack_forget()
    gmail_btn.pack_forget()
    insta_btn.pack_forget()
    linkdin_btn.pack_forget()
    save_btn_label.config(text='Please Insert Name/Note So That My Application Will Store Your Count With Reference To That Name ',font=('cambria',15,'bold'),bg='lemonchiffon')
    save_btn_label.pack()
    w4.config(textvariable=q,font=('cambria',15,'bold'))
    w4.pack(padx=5,pady=5)
    final_save.config(command=final_save_func,font=('cambria',15,'bold'))
    final_save.pack(padx=5,pady=5)
def final_save_func():
    global x
    a = q.get()
    w = re.match(' ',a)
    z = re.findall('[a-zA-Z]',a)
    t = re.findall('[0-9]',a)
    if w:
        w4.delete(0,END)
        messagebox.showwarning('Warning!!!','You Cannot Pass Blank Input !!!')
    else:
        if z:
            if t:
                messagebox.showwarning('Warning!!!','Numbers are not alloowed')
            else:
                file_path = 'c:\Prathamesh\python_txt_files\chant_counter.txt'
                with open (file_path,'a') as file_path_1:
                    file_path_1.write(a+' and your count was :- '+str(x)+'\n')
                    s = a+' and your count was :- '+str(x)
                    list_box.insert(END,s)
                sucess.config(text='Your Chant Count Is Sucessfully Stored With Name !!!\n\
    Please Click On View My Chants Button To See Your All Previous chants List',font=('cambria',15,'bold'),bg='lemonchiffon')
                sucess.pack(padx=5,pady=5)
                w1.pack_forget()
                w4.pack_forget()
                list_box.pack_forget()
                save_btn_label.pack_forget()
                save_btn.pack_forget()
                final_save.pack_forget()
                frame_2.pack_forget()
                gmail_btn.pack_forget()
                insta_btn.pack_forget()
                linkdin_btn.pack_forget()
                x = 0
                w4.delete(0,END)
        else:
            w4.delete(0,END)
            messagebox.showwarning('Warning!!!','Sorry Only Letters Are Allowed ')
def about_func():
    frame_2.pack_forget()
    save_btn.pack_forget()
    w1.pack_forget()
    sucess.pack_forget()
    w4.pack_forget()
    final_save.pack_forget()
    save_btn_label.pack_forget()
    about_label.config(text='You Can Connect Developer On Following Platforms',font=('cambria',15,'bold'),bg='lemonchiffon')
    about_label.pack(padx=10,pady=10)
    insta_btn.pack(padx=10,pady=10)
    linkdin_btn.pack(padx=10,pady=10)
    gmail_btn.pack(padx=10,pady=10)
def insta_profile():
    webbrowser.open('https://www.instagram.com/prathameshghure?utm_source=qr&igsh=MXZwZjhyZnBsb2hpNA==')
def linkdin_profile():
    webbrowser.open('https://www.linkedin.com/in/prathamesh-ghure-07310227a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app')
def gmail_profile():
    sucess.config(text='Mail Id Of Developer :- prathameshghure26@gmail.com ',font=('cambria',15,'bold'))
    sucess.pack(padx=5,pady=5)
frame_1 = Frame(root)
frame_1.config(bg='lemonchiffon')
frame_1.pack(padx=10,pady=10)
frame_4 = Frame(frame_1)
frame_4.config(bg='lemonchiffon')
frame_4.pack(side=RIGHT)
frame_5 = Frame(frame_1)
frame_5.config(bg='lemonchiffon')
frame_5.pack(side=LEFT)
frame_3 = Frame(frame_1)
frame_3.config(bd=4,bg='Black')
frame_3.pack(padx=10,pady=10,anchor=NW,side=RIGHT)
w2 = Canvas(frame_3,height=500,width=400)
w2.pack(side=RIGHT)
w3 =Image.open('e:\\Prathamesh New\\bappa_photo.jpg')
img_resize = w3.resize((400,500))
new_img = ImageTk.PhotoImage(img_resize)
w2.create_image(0,0,anchor = NW,image = new_img)
add_count_image= Image.open('c:\\Prathamesh\\python_txt_files\\addition.jpg')
upadted_add_cnt_img = add_count_image.resize((40,40))
final_add_cnt_img = ImageTk.PhotoImage(upadted_add_cnt_img)
jaap_btn = Button(frame_5,text='Add Count',image=final_add_cnt_img,command=jaap_btn_count,compound=LEFT,font=('cambria',15,'bold'),activebackground='tomato')
jaap_btn.pack(pady=25)
japp_decrease_img = Image.open('c:\\Prathamesh\\python_txt_files\\substraction.jpg')
updated_jaap_decrease_img = japp_decrease_img.resize((40,40))
final_jaap_decrease_img = ImageTk.PhotoImage(updated_jaap_decrease_img)
jaap_decrase = Button(frame_5,text='Reduce Count',image=final_jaap_decrease_img,command=decrease_count,compound=LEFT,font=('cambria',15,'bold'),activebackground='tomato')
jaap_decrase.pack(pady=25)
restart_img = Image.open('c:\\Prathamesh\\python_txt_files\\restart.jpg')
updated_restart_img = restart_img.resize((40,40))
final_restart_img = ImageTk.PhotoImage(updated_restart_img)
jaap_reset = Button(frame_5,text='Restart My Count',command=reset_count,image=final_restart_img,compound=LEFT,font=('cambria',15,'bold'),activebackground='tomato')
jaap_reset.pack(pady=25)
save_btn = Button(root,text='Save My Count ',command=save_btn_func,font=('cambria',15,'bold'),activebackground='tomato')
save_btn.pack_forget()
view_img = Image.open('c:\\Prathamesh\\python_txt_files\\view.jpg')
updated_view_img = view_img.resize((40,40))
final_updated_view_img = ImageTk.PhotoImage(updated_view_img)
view_jaap = Button(frame_4,text='View My Chants',command=view_jaap_func,image=final_updated_view_img,compound=LEFT,font=('cambria',15,'bold'),activebackground='tomato')
view_jaap.pack(pady=25)
exit_img = Image.open('c:\\Prathamesh\\python_txt_files\\exit.jpg')
update_exit_img = exit_img.resize((40,40))
final_update_exit_img = ImageTk.PhotoImage(update_exit_img)
exit_btn = Button(frame_4,text='Exit',command=root.destroy,image=final_update_exit_img,compound=LEFT,font=('cambria',15,'bold'),activebackground='tomato')
exit_btn.pack(pady=25)
about_img = Image.open('c:\\Prathamesh\\python_txt_files\\about.jpg')
update_about_img = about_img.resize((40,40))
final_update_about_img = ImageTk.PhotoImage(update_about_img)
about_btn = Button(frame_4,text='About Developer !!',command=about_func,compound=LEFT,image=final_update_about_img,font=('cambria',15,'bold'),activebackground='tomato')
about_btn.pack(pady=25)
#Static Widgets :- 
w1 = Label(root,bg='lemonchiffon')
w1.pack_forget()
save_btn_label = Label(root)
save_btn_label.pack_forget()
w4 = Entry(root)
w4.pack_forget()
final_save = Button(root,text='Final Save !!',activebackground='tomato')
final_save.pack_forget()
frame_2 = Frame(root)
frame_2.config(bg='Black',bd=4)
frame_2.pack_forget()
list_box = Listbox(frame_2)
scroll = Scrollbar(frame_2)
scroll.pack_forget()
list_box.config(yscrollcommand=scroll.set,height=100,width=400)
scroll.config(command=list_box.yview)
file_path = 'c:\Prathamesh\python_txt_files\chant_counter.txt'
with open (file_path,'r+') as file_path_2:
    content = file_path_2.readlines()
for i in content:
    list_box.insert(END,i)
list_box.pack_forget()
sucess = Label(root,font=('Cambria',15,'bold'),bg='lemonchiffon')
sucess.pack_forget()
about_label = Label(root,bg='lemonchiffon')
about_label.pack_forget()
insta_img = Image.open('c:\\Prathamesh\\python_txt_files\\insta_logo.jpg')
updated_insta_img = insta_img.resize((40,40))
final_updated_insta_img = ImageTk.PhotoImage(updated_insta_img)
insta_btn = Button(root,text='Instagram',command=insta_profile,compound=LEFT,image=final_updated_insta_img,font=('cambria',15,'bold'),activebackground='tomato')
insta_btn.pack_forget()
linkdin_img = Image.open('c:\\Prathamesh\\python_txt_files\\lindin_logo.jpg')
update_linkdin_img = linkdin_img.resize((40,40))
final_linkdin_img = ImageTk.PhotoImage(update_linkdin_img)
linkdin_btn = Button(root,text='Linkdin',command=linkdin_profile,compound=LEFT,image=final_linkdin_img,font=('cambria',15,'bold'),activebackground='tomato')
linkdin_btn.pack_forget()
gmail_img = Image.open('c:\\Prathamesh\\python_txt_files\\gmail_logo.jpg')
update_gmail_img = gmail_img.resize((40,40))
final_update_gmail_img = ImageTk.PhotoImage(update_gmail_img)
gmail_btn = Button(root,text='Gmail',command=gmail_profile,image=final_update_gmail_img,compound=LEFT,font=('cambria',15,'bold'),activebackground='tomato')
gmail_btn.pack_forget()
root.mainloop()

#Without GUI 
'''file_path = 'C:\Prathamesh\python_txt_files\mini_project8.txt'
c = 0
flag = True
while flag:
    a = input('start jaap OR enter exit :- ')
    if a.lower() == 'exit':
        z = input('are you want to save this jaap count with name  ?:- ')
        if z.lower() == 'yes':
            with open(file_path,'a') as file_obj:
                w = input('Enter jaap name :- ')
                file_obj.write(w + str(c)+'\n')
            print('Your data is sucessfully stored')
            break
        elif z.lower()=='no':
            print('you had lost your jaap counts ')
            break
        else:
            break
    else:
        c += 1
        print(c)
x = input('are you want to check your old jaap count with jaap name ?:- ')
if x.lower() == 'yes':
    with open(file_path) as file_obj_1:
        x = file_obj_1.read()
        print(x)
else:
    print("Okay thank you ")'''