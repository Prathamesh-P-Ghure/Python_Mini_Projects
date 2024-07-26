#With GUI 
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import webbrowser 
import re
root = Tk() 
root.title('Hari Om ')
root.attributes('-fullscreen',1)
root.config(bg='LavenderBlush1')
z = IntVar()
x = IntVar()
c = IntVar()
q = StringVar()
o = 1
def save():
    frame_3.pack_forget()
    frame_5.pack_forget()
    global o
    a = q.get()
    blank_checking = re.match(r' ',a)
    letter_checking = re.match(r'[\w]',a)
    if blank_checking:
        w2.delete(0,END)
        messagebox.showerror('Error !!','You Cannot Pass Blank Input')
        o -= 1
    elif letter_checking:
        if z.get() == 1 and x.get() == 0 and c.get() == 0:
            file_path = 'C:\Prathamesh\python_txt_files\All_songs\marathi.txt'
            with open (file_path,'a') as file_obj:
                file_obj.write( a+'\n')
            w9.config(text = str(o)+' Song Saved Sucessfully',padx=5,pady=5)
            w9.pack()
            w4.toggle()
        elif x.get() == 1 and z.get() == 0  and c.get() == 0:
            file_path_1 = 'C:\Prathamesh\python_txt_files\All_songs\english.txt'
            with open(file_path_1,'a') as file_obj_1:
                file_obj_1.write(a+'\n')
            w9.config(text =  str(o)+' Song Saved Sucessfully',padx=5,pady=5)
            w9.pack()
            w5.toggle()
        elif c.get() == 1 and x.get() == 0 and z.get() == 0 :
            file_path = 'C:\Prathamesh\python_txt_files\All_songs\hindi.txt'
            with open (file_path,'a') as file_obj_2:
                file_obj_2.write(a+'\n')
            w9.config(text =  str(o)+' Song Saved Sucessfully',padx=5,pady=5)
            w9.pack()
            w6.toggle()
        elif z.get() == 0 and x.get() == 0 and c.get() == 0 :
            messagebox.showwarning('Warning !!!','You Have To Select One Field ')
            o -= 1
        else:
            messagebox.showwarning('Warning','You Cannot Select More Than One Field')
            o -= 1
    else:
        messagebox.showerror('Error !!','You Cannot Pass Blank Input')
        o -= 1
    w2.delete(0,END)
    o += 1
def main():
    frame_3.pack_forget()
    frame_2.pack_forget()
    frame_5.pack_forget()
    w9
    frame_4.config(bg='LavenderBlush1')
    frame_4.pack()
    w1.config(text='Enter A Song Name :- ',font=('cambria',15,'bold'))
    w1.pack()
    w2.config(Entry(frame_4),textvariable=q,font=('cambria',15,'bold'))
    w2.pack()
    w3.config(text='Enter field(Marathi,Hindi,English) of song:- ',font=('cambria',15,'bold'))
    w3.pack()
    w4.config(text='Marathi',variable=z,font=('cambria',15,'bold'))
    w4.pack()
    w5.config(text='English',variable=x,font=('cambria',15,'bold'))
    w5.pack()
    w6.config(text='Hindi',variable=c,font=('cambria',15,'bold'))
    w6.pack()
    w7.config(text='Save',command=save,font=('cambria',15,'bold'),activebackground='Tomato')
    w7.pack()
    w8.config(text='Exit  ',command=root.destroy,font=('cambria',15,'bold'),activebackground='Tomato')
    w8.pack()
def marathi_file_open():
    frame_3.pack_forget()
    frame_4.pack_forget()
    frame_5.pack_forget()
    w9.pack_forget()
    w1_1.delete(0,END)
    file_path = 'C:\Prathamesh\python_txt_files\All_songs\marathi.txt'
    with open (file_path) as file_obj_4:
        content = file_obj_4.readlines()
    for i in content:
        w1_1.insert(END,i)
    w1_1.pack(side=LEFT)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=w1_1.yview)
    frame_2.pack()
def english_file_open():
    frame_3.pack_forget()
    frame_4.pack_forget()
    frame_5.pack_forget()
    w9.pack_forget()
    w1_1.delete(0,END)
    file_path = 'C:\Prathamesh\python_txt_files\All_songs\english.txt'
    with open (file_path) as file_obj_4:
        content = file_obj_4.readlines()
    for i in content:
        w1_1.insert(END,i)
    w1_1.pack(side=LEFT)
    scroll.pack(side=LEFT,fill=Y)
    scroll.config(command=w1_1.yview)
    frame_2.pack()
def hindi_file_open():
    frame_3.pack_forget()
    frame_4.pack_forget()
    frame_5.pack_forget()
    w9.pack_forget()
    w1_1.delete(0,END)
    file_path = 'C:\Prathamesh\python_txt_files\All_songs\hindi.txt'
    with open (file_path) as file_obj_4:
        content = file_obj_4.readlines()
    for i in content:
        w1_1.insert(END,i)
    w1_1.pack(side=LEFT)
    scroll.pack(side=RIGHT,fill=Y)
    scroll.config(command=w1_1.yview)
    frame_2.pack()
def about_func():
    frame_2.pack_forget()
    frame_3.pack_forget()
    frame_4.pack_forget()
    w10.pack_forget()
    frame_5.pack()
    insta_btn.pack(pady=10)
    linkdin_btn.pack(pady=10)
    gmail_btn.pack(pady=10)
def insta_profile():
    webbrowser.open('https://www.instagram.com/prathameshghure?utm_source=qr&igsh=MXZwZjhyZnBsb2hpNA==')
def linkdin_profile():
    webbrowser.open('https://www.linkedin.com/in/prathamesh-ghure-07310227a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app')
def gmail_profile():
    w10.config(text='Mail Id Of Developer :- prathameshghure26@gmail.com ',font=('cambria',15,'bold'),bg='LavenderBlush1')
    w10.pack(padx=5,pady=5)
frame_1 = Frame(root)
frame_1.pack()
frame_1.config(bd=4,background='Black')
frame_2 = Frame(root)
frame_2.config(height=20,width=45,bg='LavenderBlush1')
frame_2.pack_forget()
w1 = Label(frame_1,text='Welcome To Prathamesh Song Saver Website !!!',font=('cambria',15,'bold'),bg='Yellow')
w1.pack(padx=5,pady=10,ipadx=5,ipady=5)
w2 = Label(root,text='Note :- Click On File Menu For Various Options ',font=('cambria',15,'bold'),bg='LavenderBlush1')
w2.pack(padx=5,pady=10,ipadx=5,ipady=5)
main_menu_bar = Menu(root)
opt_1 = Menu(main_menu_bar)
opt_1.add_command(label='Add Songs',command=main,font=('cambria',15,'bold'))
opt_1.add_separator()
new_opt = Menu(opt_1)
new_opt.add_command(label='Marathi',command=marathi_file_open,font=('cambria',15,'bold'))
new_opt.add_separator()
new_opt.add_command(label='English',command=english_file_open,font=('cambria',15,'bold'))
new_opt.add_separator()
new_opt.add_command(label='Hindi',command=hindi_file_open,font=('cambria',15,'bold'))
new_opt.add_separator()
opt_1.add_cascade(label='Show Saved Song List',menu=new_opt,font=('cambria',15,'bold'))
opt_1.add_separator()
opt_1.add_command(label='About Developer',command=about_func,font=('cambria',15,'bold'))
opt_1.add_separator()
opt_1.add_command(label='Exit',command=root.destroy,font=('cambria',15,'bold'))
opt_1.add_separator()
main_menu_bar.add_cascade(menu=opt_1,label='File',font=('cambria',15,'bold'))
root.config(menu=main_menu_bar)
frame_3 = Frame(root,bd=4,bg='Black')
frame_3.pack()
main_img = Canvas(frame_3,height=400,width=700)
main_img.pack()
img_file= Image.open('c:\Prathamesh\python_txt_files\prathu_piano.jpg')
update_img = img_file.resize((700,400))
final_update = ImageTk.PhotoImage(update_img)
main_img.create_image(0,0,anchor = NW,image = final_update)
#Static Layout :- 
frame_4 = Frame(root)
frame_4.pack()
w1 = Label(frame_4)
w1.pack_forget()
w2 = Entry(frame_4,textvariable=q)
w2.pack_forget()
w3 = Label(frame_4)
w3.pack_forget()
w4 = Checkbutton(frame_4,variable=z)
w4.pack_forget()
w5 = Checkbutton(frame_4,variable=x)
w5.pack_forget()
w6 = Checkbutton(frame_4,variable=c)
w6.pack_forget()
w7 = Button(frame_4,command=save)
w7.pack_forget()
exit_img = Image.open('c:\Prathamesh\python_txt_files\exit.jpg')
update_exit_img = exit_img.resize((40,40))
final_update_exit_img = ImageTk.PhotoImage(update_exit_img)
w8 = Button(frame_4,command=root.destroy,compound=RIGHT,image=final_update_exit_img)
w8.pack_forget()
w9 = Label(root,font=('cambria',15,'bold'))
w9.pack_forget()
frame_5 = Frame(root,bg='LavenderBlush1')
frame_5.pack_forget()
w10 = Label(frame_5)
w10.pack_forget()
scroll= Scrollbar(frame_2)
scroll.pack_forget()
w1_1 = Listbox(frame_2,yscrollcommand=scroll.set)
w1_1.config(height=10,width=30,font=('cambria',15,'bold'))
w1_1.pack_forget()
insta_img = Image.open('c:\\Prathamesh\\python_txt_files\\insta_logo.jpg')
updated_insta_img = insta_img.resize((40,40))
final_updated_insta_img = ImageTk.PhotoImage(updated_insta_img)
insta_btn = Button(frame_5,text='Instagram',command=insta_profile,compound=LEFT,image=final_updated_insta_img,font=('cambria',15,'bold'),activebackground='tomato')
insta_btn.pack_forget()
linkdin_img = Image.open('c:\\Prathamesh\\python_txt_files\\lindin_logo.jpg')
update_linkdin_img = linkdin_img.resize((40,40))
final_linkdin_img = ImageTk.PhotoImage(update_linkdin_img)
linkdin_btn = Button(frame_5,text='Linkdin',command=linkdin_profile,compound=LEFT,image=final_linkdin_img,font=('cambria',15,'bold'),activebackground='tomato')
linkdin_btn.pack_forget()
gmail_img = Image.open('c:\\Prathamesh\\python_txt_files\\gmail_logo.jpg')
update_gmail_img = gmail_img.resize((40,40))
final_update_gmail_img = ImageTk.PhotoImage(update_gmail_img)
gmail_btn = Button(frame_5,text='Gmail',command=gmail_profile,image=final_update_gmail_img,compound=LEFT,font=('cambria',15,'bold'),activebackground='tomato')
gmail_btn.pack_forget()
root.mainloop()
#Without GUI 
'''flag = True
while flag:
    x = input('Enter Song name or exit:-')
    if x.lower() == 'exit':
        flag = False
    else:
        y = input('Enter field(Marathi,Hindi,English) of song:- ')
        if y.lower() == 'marathi':
            file_path = 'C:\Prathamesh\python_txt_files\All_songs\marathi.txt'
            with open (file_path,'a') as file_obj:
                file_obj.write(x +'\n')
        elif y.lower() == 'hindi':
            file_path = 'C:\Prathamesh\python_txt_files\All_songs\hindi.txt'
            with open (file_path,'a') as file_obj:
                file_obj.write(x+'\n')
        elif y.lower() == 'english':
            file_path = 'C:\Prathamesh\python_txt_files\All_songs\english.txt'
            with open(file_path,'a') as file_obj:
                file_obj.write(x+'\n')
        else:
            print('Our senior prathamesh sir will solve error ')'''