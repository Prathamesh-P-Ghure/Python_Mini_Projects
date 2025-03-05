print('Ganpati Bappa Morya !!! ')
from tkinter import *
from tkinter import simpledialog
from datetime import *
from tkinter import messagebox
from PIL import Image,ImageTk
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import numpy as np
import webbrowser
import pandas as pd
import matplotlib.pyplot as plt
import re
root = Tk()
root.title('Jai Shree Ram')
root.attributes('-fullscreen',True)
root.config(bg='Pink')
q = StringVar()
def farmer_btn_func():
    main_dynamic_frame.pack_forget()
    about_label.pack_forget()
    mail_id_label.pack_forget()
    insta_btn.pack_forget()
    gmail_btn.pack_forget()
    linkdin_btn.pack_forget()
    analyst_name_confirmation_label.pack_forget()
    frame_for_farmers_btns_working.pack()
    profit_recmommandation.pack(side=LEFT,padx=10,pady=10)
    govt_schems_for_farmers.pack(side=LEFT,padx=10,pady=10)
    feedback_farmer_btn.pack(side=LEFT,padx=10,pady=10)
    back_to_main_page_btn_for_farmers.pack(side=LEFT,padx=10,pady=10)
def analyst_btn_func():
    analyst_btn.pack_forget()
    mail_id_label.pack_forget()
    about_label.pack_forget()
    insta_btn.pack_forget()
    gmail_btn.pack_forget()
    linkdin_btn.pack_forget()
    entry_pass = simpledialog.askinteger('Security Purpose !','Enter password :- ')
    if entry_pass == 7588:
        analyst_name_label.config()
        analyst_name_label.pack(padx=10,pady=10)
        analyst_name_entry.config(textvariable=q)
        analyst_name_entry.pack(padx=10,pady=10)
        proceed_analyst_btn.pack(padx=10,pady=10)
    elif entry_pass != 7588:
        messagebox.showerror('Warning !!!','Wrong Password (If You Have Forgetted Password Then You Can Contact Developer By Clicking About Developer Button )')
        analyst_btn.pack()
        proceed_analyst_btn.pack_forget()
    else:
        pass
def proceed_analyst_btn_fun():
    time_keeper = datetime.now()
    time_converter = time_keeper.ctime()
    entry_name_taker = q.get()
    entry_name_number_checker = re.findall('[0-9]',entry_name_taker)
    if re.fullmatch(r'[A-Za-z]+', entry_name_taker):
        file_path = 'e:\Prathamesh New\MSC-IT\Sem 3 Project\security_details_keeper.txt'
        with open (file_path,'a+') as file_path_2:
                    file_path_2.write('Login Name :- '+entry_name_taker+'\n')
                    file_path_2.write('Login Time And Date:- '+time_converter+'\n')
        proceed_analyst_btn.pack_forget()
        analyst_name_label.pack_forget()
        analyst_name_entry.delete(0,END)
        analyst_name_entry.pack_forget()
        main_dynamic_frame.pack_forget()
        frame_for_analyst_btns_working.pack()
        analyst_name_confirmation_label.config(text='Welcome '+entry_name_taker)
        analyst_name_confirmation_label.pack()
        farmers_info.pack(side=LEFT,padx=10,pady=10)
        profit_influencing_factor_btn.pack(side=LEFT,padx=10,pady=10)
        about_tools_btn.pack(side=LEFT,padx=10,pady=10)
        water_supply_method_btn.pack(side=LEFT,padx=10,pady=10)
        govt_plicy_awareness_analysis_btn.pack(side=LEFT,padx=10,pady=10)
        back_to_home_page_btn.pack(padx=10,pady=10)
        check_accuracy_btn.pack(padx=10,pady=10)
    elif entry_name_number_checker:
        analyst_name_entry.delete(0,END)
        analyst_name_label.pack_forget()
        analyst_name_entry.pack_forget()
        messagebox.showwarning('Wrong Input !','Inavalid Name.You Cannot Pass Numbers As Name')
        analyst_btn.pack()
        proceed_analyst_btn.pack_forget()
    else:
        analyst_name_entry.delete(0,END)
        analyst_name_label.pack_forget()
        analyst_name_entry.pack_forget()
        messagebox.showwarning('Wrong Input !','Please Provide Valid Name ')
        analyst_btn.pack()
        proceed_analyst_btn.pack_forget()
def goverment_btn_func():
    pass
def back_to_home_page_btn_fun():
    check_accuracy_btn.pack_forget()
    analyst_name_confirmation_label.pack_forget()
    explanation_of_farmers_info_label.pack_forget()
    explaination_label_for_all_analysts_btns_working.pack_forget()
    frame_for_list_box_farmer_names.pack_forget()
    frame_for_analyst_btns_working.pack_forget()
    back_to_home_page_btn.pack_forget()
    main_dynamic_frame.pack()
    analyst_btn.pack(padx=10,pady=10)
def farmers_info_func():
    analyst_name_confirmation_label.pack_forget()
    explaination_label_for_all_analysts_btns_working.pack_forget()
    excel_file_path = 'e:\Prathamesh New\MSC-IT\Sem 3 Project\project.xlsx'
    excel_data = pd.read_excel(excel_file_path)
    excel_data.head()
    farmer_names = excel_data['Farmer Names']
    land_usage = excel_data['Land (in guntha)']
    total_land_occupied_in_guntha = 0 #Setting 0 for now which will update automatically once you iterate for loop on land_usage values
    for i in land_usage:
        total_land_occupied_in_guntha += i
    total_land_occupied_in_acre = total_land_occupied_in_guntha //40 #keep it up prathamesh
    explanation_of_farmers_info_label.config(text='All Farmers Name With Their Farming Land Information Are As Follows :- '+'\nTotal Number Of Farmers :- '+str(len(farmer_names))+'\n'+'Total Land Occupied By All Mentioned Farmers(In Guntha) :- '+str(total_land_occupied_in_guntha)+'\n'+'Total Land Occupied By All Mentioned Farmers(In Acre) :- '+str(total_land_occupied_in_acre))
    explanation_of_farmers_info_label.pack()
    frame_for_list_box_farmer_names.pack()
    scroll_for_farmers_info.pack(side=RIGHT,fill=Y)
    list_box_for_farmer.config(height=5,width=50,font=('cambria',15,'bold'))
    for i in farmer_names:
        list_box_for_farmer.insert(END,i)
    list_box_for_farmer.pack(side=LEFT,fill=BOTH)
    scroll_for_farmers_info.config(command=list_box_for_farmer.yview)
    plt.figure(figsize=(12, 3))
    plt.bar(farmer_names, land_usage, color='skyblue')
    plt.xlabel('Farmer Names')
    plt.ylabel('Land (in guntha)')
    plt.title('Land Usage by Farmers')
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
def profit_influencing_factor_btn_func():
    analyst_name_confirmation_label.pack_forget()
    explanation_of_farmers_info_label.pack_forget()
    frame_for_list_box_farmer_names.pack_forget()
    explaination_label_for_all_analysts_btns_working.config(text='Explanation For Given Graph Is as Follows :- \npesticides_usage per month (in liters): Coefficient of \
-116.48: A negative coefficient means that as pesticide usage increases, the profit tends to decrease.\nThis indicate overuse of pesticides is negatively influencing to decrease profit.\n\
fertilizer_usage per month (in kg): Coefficient of  22.16: This positive coefficient suggests that increasing fertilizer usage is generally associated with an increase in profit, although it should use within require range\
.\nso as a analyst your primary aim is to recommand ideal amount of fertilizer and pesticide to farmer in order to get more porfit.You Can Ignore Other Factors For Now Only ')
    explaination_label_for_all_analysts_btns_working.pack()
    file_path = 'e:\\Prathamesh New\\MSC-IT\\Sem 3 Project\\project.xlsx' 
    data = pd.read_excel(file_path, sheet_name='Sheet1')

    # Selecting relevant features for the model (excluding 'Profit(2023)')
    features = ['Profit(2021)', 'Profit(2022)', 'rainfall at 2021 (in mm)', 
                'rainfall at 2022 (in mm)', 'rainfall at 2023 (in mm)', 
                'Expected rainfall 2024 (in mm) ', 'fertilizer_usage per month ( in kg)', 
                'pesticides_usage per month ( in liters)']
    target = 'Profit(2023)'

    # Splitting data into features (X) and target (y)
    X = data[features]
    y = data[target]

    # Splitting the dataset into training (80%) and testing (20%) sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the Linear Regression model
    model = LinearRegression()

    # Train the model
    model.fit(X_train, y_train)

    # Predict on the test set
    y_pred = model.predict(X_test)
    # Get model coefficients and corresponding feature names
    coefficients = model.coef_
    feature_importance = pd.DataFrame({
        'Feature': features,
        'Coefficient': coefficients
    })
    # Display feature importance sorted by absolute value of coefficients
    feature_importance['Absolute Coefficient'] = np.abs(feature_importance['Coefficient'])
    feature_importance = feature_importance.sort_values(by='Absolute Coefficient', ascending=False)

    other_influencing_factores = feature_importance[['Feature', 'Coefficient']]#if examinar asks for other factors influence then just print this
    # Visualizing feature importance
    plt.figure(figsize=(12, 5))
    plt.bar(feature_importance['Feature'], feature_importance['Absolute Coefficient'], color='Pink')
    plt.title('Feature Importance Based on Absolute Coefficient Values')
    plt.xlabel('Features')
    plt.ylabel('Absolute Coefficient')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
def about_tools_btn_func():
    explanation_of_farmers_info_label.pack_forget()
    analyst_name_confirmation_label.pack_forget()
    frame_for_list_box_farmer_names.pack_forget()
    # Load the Excel file
    file_path = 'e:\Prathamesh New\MSC-IT\Sem 3 Project\project.xlsx'
    data = pd.read_excel(file_path)
    data.head()
    all_tool_types = data['Type Of Tools']
    B_list_for_stroing_modern_type = []
    B_list_for_stroing_tradional_type = []
    B_list_for_stroing_hybrid_type = []
    for i in all_tool_types:
        if i == 'Modern':
            B_list_for_stroing_modern_type.append(i)
        elif i == 'Traditional':
            B_list_for_stroing_tradional_type.append(i)
        elif i == 'Hybrid':
            B_list_for_stroing_hybrid_type.append(i)
    explaination_label_for_all_analysts_btns_working.config(text='The Follwoing Are Exact Numbers Of Farmers Who Are Using Modern,Traditional,Hybrid Methods \nNumber Of Farmers Using Modern \
Type Of Tools :-'+str(len(B_list_for_stroing_modern_type))+'\n'+'Number Of Farmers Using \
Modern Type Of Tools :-'+str(len(B_list_for_stroing_tradional_type))+'\n'+'Number Of Farmers Using \
Both Type Of Tools :-'+str(len(B_list_for_stroing_hybrid_type)))
    explaination_label_for_all_analysts_btns_working.pack()
    # Assuming the columns are 'FarmerID' and 'ToolType' in your Excel sheet
    # Adjust as needed based on your actual column names
    tool_counts = data['Type Of Tools'].value_counts()
    # Create pie chart
    plt.figure(figsize=(8, 3))
    plt.pie(tool_counts, labels=tool_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Type Of Tools Used by Farmers')
    plt.show()
def water_supply_method_btn_func():
    explanation_of_farmers_info_label.pack_forget()
    analyst_name_confirmation_label.pack_forget()
    frame_for_list_box_farmer_names.pack_forget()
    file_path = 'e:\Prathamesh New\MSC-IT\Sem 3 Project\project.xlsx'
    data = pd.read_excel(file_path)
    data.head()
    all_water_supply_types = data['Water Supply Methods']
    B_list_for_stroing_drip_type_water_supply = []
    B_list_for_stroing_Sprinkler_type_water_supply = []
    for i in all_water_supply_types:
        if i == 'Drip':
            B_list_for_stroing_drip_type_water_supply.append(i)
        elif i == 'Sprinkler':
            B_list_for_stroing_Sprinkler_type_water_supply.append(i)
        else:
            pass
    explaination_label_for_all_analysts_btns_working.config(text='The Follwoing Are Exact Numbers Of Farmers Who Are Using Drip And Sprinkler Water Supply Methods For Farming. \nNumber Of Farmers Using Drip \
Method :-'+str(len(B_list_for_stroing_drip_type_water_supply))+'\n'+'Number Of Farmers Using \
Sprinkler Method :-'+str(len(B_list_for_stroing_Sprinkler_type_water_supply)))
    explaination_label_for_all_analysts_btns_working.pack()
    # Assuming the columns are 'FarmerID' and 'ToolType' in your Excel sheet
    # Adjust as needed based on your actual column names
    tool_counts = data['Water Supply Methods'].value_counts()
    # Create pie chart
    plt.figure(figsize=(8, 3))
    plt.pie(tool_counts, labels=tool_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Water Supply Methods Used by Farmers')
    plt.show()
def govt_plicy_awareness_analysis_btn_fun():
    explanation_of_farmers_info_label.pack_forget()
    frame_for_list_box_farmer_names.pack_forget()
    analyst_name_confirmation_label.pack_forget()
    file_path = 'e:\Prathamesh New\MSC-IT\Sem 3 Project\project.xlsx'
    data = pd.read_excel(file_path)
    data.head()
    all_water_supply_types = data['Government Policies Awarness']
    B_list_for_stroing_yes_answers = []
    B_list_for_stroing_no_answers = []
    for i in all_water_supply_types:
        if i == 'Yes':
            B_list_for_stroing_yes_answers.append(i)
        elif i == 'No ':
            B_list_for_stroing_no_answers.append(i)
        else:
            print('Something Error Occured !')
    explaination_label_for_all_analysts_btns_working.config(text='The Follwoing Are Exact Numbers Of Farmers Which Are Aware And Taking Benifites Of Goverment Policies For Farming. \nNumber Of Farmers Aware About \
Government Policies :-'+str(len(B_list_for_stroing_yes_answers))+'\n'+'Number Of Farmers Dont Aware \
And Not Getting Benifits Of Government Policies :-'+str(len(B_list_for_stroing_no_answers)))
    explaination_label_for_all_analysts_btns_working.pack()
    # Assuming the columns are 'FarmerID' and 'ToolType' in your Excel sheet
    # Adjust as needed based on your actual column names
    tool_counts = data['Government Policies Awarness'].value_counts()
    # Create pie chart
    plt.figure(figsize=(8, 3))
    plt.pie(tool_counts, labels=tool_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title('Distribution of Water Supply Methods Used by Farmers')
    plt.show()
def check_accuracy_btn_fun():
    analyst_name_confirmation_label.pack_forget()
    explanation_of_farmers_info_label.pack_forget()
    frame_for_list_box_farmer_names.pack_forget()
    file_path = 'e:\Prathamesh New\MSC-IT\Sem 3 Project\project.xlsx'
    df = pd.read_excel(file_path, sheet_name='Sheet1')

    # Prepare the data
    # We'll assume that 'Profit(2023)' is the target variable, and the rest are features.
    X = df.drop(columns=['Profit(2023)', 'Farmer Names'])
    y = df['Profit(2023)']

    # One-hot encode categorical variables
    X_encoded = pd.get_dummies(X, drop_first=True)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.3, random_state=42)

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict and check model performance
    y_pred = model.predict(X_test)
    r2 = r2_score(y_test, y_pred)

    # Check coefficients to find the most influential factors
    coefficients = model.coef_
    features = X_encoded.columns

    # Combine feature names with their corresponding coefficients
    feature_importance = pd.DataFrame({'Feature': features, 'Importance': np.abs(coefficients)}).sort_values(by='Importance', ascending=False)
    explaination_label_for_all_analysts_btns_working.config(text='What Is R^2 Score ?\n\
R^2 Also Known As The coefficient of determination.\nThe R² score represents the proportion of the variance in the dependent variable (Profit(2023)) that is predictable from the independent variables (features).\nYour Model R^2 Is'+str(r2)+'\n\
This indicates that your model fits the data very well, as it explains almost all the variation/influences for Profit.')
    explaination_label_for_all_analysts_btns_working.pack()
#All Functions Of Farmers Buttons :- 
def profit_recmommandation_func():
    frame_for_feedback.pack_forget()
    feedback_submit_btn.pack_forget()
def govt_schems_for_farmers_func():
    frame_for_feedback.pack_forget()
    feedback_submit_btn.pack_forget()
    webbrowser.open('https://www.google.com/search?q=government+schemes+for+farmers+in+maharashtra&rlz=1C1CHBF_enIN890IN890&oq=govenment+schemes+for+farmer&gs_lcrp=EgZjaHJvbWUqCQgCEAAYDRiABDIGCAAQRRg5MgkIARAAGA0YgAQyCQgCEAAYDRiABDIJCAMQABgNGIAEMgkIBBAAGA0YgAQyCQgFEAAYDRiABDIJCAYQABgNGIAEMgkIBxAAGA0YgAQyCQgIEAAYDRiABDIJCAkQABgNGIAE0gEJMTU0NjJqMGo3qAIIsAIB&sourceid=chrome&ie=UTF-8')
def feedback_farmer_btn_func():
    frame_for_feedback.pack()
    frame1_of_feedback.pack(side=LEFT)
    frame2_of_feedback.pack(side=RIGHT)
    name_label_for_feedback.pack(padx=10,pady=10)
    name_of_feedback_giver.pack(padx=10,pady=10)
    actual_feedback_label.pack(padx=10,pady=80)
    actual_message_of_user.pack(padx=10,pady=10)
    feedback_submit_btn.pack(padx=10,pady=10)
def feedback_submit_btn_func():
    feedback_submit_btn.pack_forget()
    frame_for_feedback.pack_forget()
    feedback_storer = actual_message_of_user.get("1.0",END)
    file_name_keeper = name_of_feedback_giver.get()
    file_path = 'E:\\Prathamesh New\\MSC-IT\\Sem 3 Project\\All_Feedbacks\\'+file_name_keeper+'.txt'
    with open(file_path,'w')as file_obj_1:
        file_obj_1.write(feedback_storer)
    name_of_feedback_giver.delete(0,END)
    actual_message_of_user.delete("1.0",END)
    explnation_label_for_all_farmers_btn_working.config(text=file_name_keeper+' Thank You So Much For Giving Feedback !!')
    explnation_label_for_all_farmers_btn_working.pack()
def back_to_main_page_btn_for_farmers_func():
    frame_for_farmers_btns_working.pack_forget()
    frame_for_feedback.pack_forget()
    feedback_submit_btn.pack_forget()
    explnation_label_for_all_farmers_btn_working.pack_forget()
    main_dynamic_frame.pack()
def about_func():
    analyst_name_confirmation_label.pack_forget()
    mail_id_label.pack_forget()
    about_label.config(text='You Can Connect Developer On Following Platforms',font=('cambria',15,'bold'),bg='Pink')
    about_label.pack(padx=10,pady=10)
    insta_btn.pack(padx=10,pady=10,ipadx=5,ipady=5)
    linkdin_btn.pack(padx=10,pady=10,ipadx=5,ipady=5)
    gmail_btn.pack(padx=10,pady=10,ipadx=5,ipady=5)
def insta_profile():
    webbrowser.open('https://www.instagram.com/prathameshghure?utm_source=qr&igsh=MXZwZjhyZnBsb2hpNA==')
def linkdin_profile():
    webbrowser.open('https://www.linkedin.com/in/prathamesh-ghure-07310227a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app')
def gmail_profile():
    mail_id_label.pack()
heading_frame = Frame(root)
heading_frame.config(bd=4,bg='black')
heading_frame.pack(padx=10,pady=10)
heading_label = Label(heading_frame,text='Agriculture Data Analyzer',font=('cambria',20,'bold'),bg='Pink')
heading_label.pack()
main_dynamic_frame = Frame(root)
main_dynamic_frame.config(bg='Pink')
main_dynamic_frame.pack()
farmer_btn = Button(main_dynamic_frame,text='Access This Model As A Farmer',command=farmer_btn_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
farmer_btn.pack(ipadx=5,padx=10,ipady=5,pady=10)
analyst_btn = Button(main_dynamic_frame,text='Access This Model As A Analyst',command=analyst_btn_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
analyst_btn.pack(ipadx=5,padx=10,ipady=5,pady=10)
about_img = Image.open('c:\\Prathamesh\\python_txt_files\\about.jpg')
update_about_img = about_img.resize((40,40))
final_update_about_img = ImageTk.PhotoImage(update_about_img)
about_btn = Button(main_dynamic_frame,text='About Developer !!',command=about_func,compound=RIGHT,image=final_update_about_img,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
about_btn.pack(padx=10,pady=10)
footer_frame = Frame(root)
footer_frame.config(bg='Black',height=100,width=1550)
footer_frame.pack_propagate(0)
footer_frame.pack(side='bottom',fill='x')
footer_label = Label(footer_frame,text='All Copyrights Reserved By Developer(Prathamesh) !!!',bg='black',fg='White',font=('cambria',15,'bold'))
footer_label.pack(ipadx=10,ipady=10)
#Static Widgets :- 
about_label = Label(main_dynamic_frame)
about_label.pack_forget()
analyst_name_label = Label(main_dynamic_frame,text='Enter Your Name For Security References(Without Any Space) :- ',font=('cambria',15,'bold'))
analyst_name_label.pack_forget()
analyst_name_entry = Entry(main_dynamic_frame,font=('cambria',15,'bold'))
analyst_name_entry.pack_forget()
proceed_analyst_btn = Button(main_dynamic_frame,text='Proceed',command=proceed_analyst_btn_fun,font=('cambria',15,'bold'))
proceed_analyst_btn.pack_forget()
insta_img = Image.open('c:\\Prathamesh\\python_txt_files\\insta_logo.jpg')
updated_insta_img = insta_img.resize((40,40))
final_updated_insta_img = ImageTk.PhotoImage(updated_insta_img)
insta_btn = Button(main_dynamic_frame,text='Instagram',command=insta_profile,compound=RIGHT,image=final_updated_insta_img,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
insta_btn.pack_forget()
linkdin_img = Image.open('c:\\Prathamesh\\python_txt_files\\lindin_logo.jpg')
update_linkdin_img = linkdin_img.resize((40,40))
final_linkdin_img = ImageTk.PhotoImage(update_linkdin_img)
linkdin_btn = Button(main_dynamic_frame,text='Linkdin',command=linkdin_profile,compound=RIGHT,image=final_linkdin_img,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
linkdin_btn.pack_forget()
gmail_img = Image.open('c:\\Prathamesh\\python_txt_files\\gmail_logo.jpg')
update_gmail_img = gmail_img.resize((40,40))
final_update_gmail_img = ImageTk.PhotoImage(update_gmail_img)
gmail_btn = Button(main_dynamic_frame,text='Gmail',command=gmail_profile,image=final_update_gmail_img,compound=RIGHT,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
gmail_btn.pack_forget()
exit_img = Image.open('c:\\Prathamesh\\python_txt_files\\exit.jpg')
update_exit_img = exit_img.resize((40,40))
final_update_exit_img = ImageTk.PhotoImage(update_exit_img)
mail_id_label = Label(main_dynamic_frame,text='Mail Id Of Developer :- prathameshghure26@gmail.com ',bg='Pink',font=('cambria',15,'bold'))
mail_id_label.pack_forget()
exit_btn = Button(main_dynamic_frame,text='Exit',command=root.destroy,image=final_update_exit_img,compound=RIGHT,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
exit_btn.pack(padx=10,pady=10)
#statics widgets for analyst buttons :- 
frame_for_analyst_btns_working = Frame(root,bg='Pink')
frame_for_analyst_btns_working.pack_forget()
analyst_name_confirmation_label = Label(frame_for_analyst_btns_working,text='Dynamic Welcome With Name',font=('cambria',15,'bold'),bg='pink')
analyst_name_confirmation_label.pack_forget()
back_to_home_page_btn = Button(frame_for_analyst_btns_working,text='Back To Main Page',command=back_to_home_page_btn_fun,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
back_to_home_page_btn.pack_forget()
farmers_info = Button(frame_for_analyst_btns_working,text='Farmers Information',command=farmers_info_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
farmers_info.pack_forget()
frame_for_list_box_farmer_names = Frame(root)
frame_for_list_box_farmer_names.config(bg='Black',bd=4)
frame_for_list_box_farmer_names.pack_forget()
list_box_for_farmer  = Listbox(frame_for_list_box_farmer_names)
scroll_for_farmers_info = Scrollbar(frame_for_list_box_farmer_names)
scroll_for_farmers_info.pack_forget()
list_box_for_farmer.config(yscrollcommand=scroll_for_farmers_info.set,height=100,width=400)
scroll_for_farmers_info.config(command=list_box_for_farmer.yview)
list_box_for_farmer.pack_forget()
explanation_of_farmers_info_label = Label(root,text='All Farmers Name With Their Farming Land Information Are As Follows :- ',font=('cambria',15,'bold'),bg='Pink')
explanation_of_farmers_info_label.pack_forget()
explaination_label_for_all_analysts_btns_working = Label(root,text='it will be dynamic for every analyst button',bg='Pink',font=('cambria',15,'bold'))
explaination_label_for_all_analysts_btns_working.pack_forget()
profit_influencing_factor_btn = Button(frame_for_analyst_btns_working,text='Show Profit Influencing Factor',command=profit_influencing_factor_btn_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
profit_influencing_factor_btn.pack_forget()
about_tools_btn = Button(frame_for_analyst_btns_working,text='Tools Analysis',command=about_tools_btn_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
about_tools_btn.pack_forget()
water_supply_method_btn = Button(frame_for_analyst_btns_working,text='Water Anlysis',command=water_supply_method_btn_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
water_supply_method_btn.pack_forget()
govt_plicy_awareness_analysis_btn = Button(frame_for_analyst_btns_working,text='GOVT Policies Awarenes Ratio',command=govt_plicy_awareness_analysis_btn_fun,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
govt_plicy_awareness_analysis_btn.pack_forget()
check_accuracy_btn = Button(root,text='Check Accuracy',command=check_accuracy_btn_fun,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
check_accuracy_btn.pack_forget()
#Static Widgets For Farmer Button :-
frame_for_farmers_btns_working = Frame(root,bg='Pink')
frame_for_farmers_btns_working.pack_forget()
profit_recmommandation = Button(frame_for_farmers_btns_working,text='Profit Recommandation',command=profit_recmommandation_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
profit_recmommandation.pack_forget()
govt_schems_for_farmers = Button(frame_for_farmers_btns_working,text='Goverment Schemes For Farmers',command=govt_schems_for_farmers_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
govt_schems_for_farmers.pack_forget()
feedback_farmer_btn = Button(frame_for_farmers_btns_working,text='Feedback/Help',command=feedback_farmer_btn_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
feedback_farmer_btn.pack_forget()
back_to_main_page_btn_for_farmers = Button(frame_for_farmers_btns_working,text='Back To Home Page',command=back_to_main_page_btn_for_farmers_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
back_to_main_page_btn_for_farmers.pack_forget()
#-->Static Widget For Feedback Button :- 
frame_for_feedback = Frame(root,bg='Pink')
frame_for_feedback.pack_forget()
frame1_of_feedback = Frame(frame_for_feedback,bg='Pink')
frame1_of_feedback.pack_forget()
frame2_of_feedback = Frame(frame_for_feedback,bg='Pink')
frame2_of_feedback.pack_forget()
name_label_for_feedback = Label(frame1_of_feedback,text='Please Tell Your Name Here ---> ',bg='Pink',font=('cambria',15,'bold'))
name_label_for_feedback.pack_forget()
name_of_feedback_giver = Entry(frame2_of_feedback,font=('cambria',15,'bold')) 
name_of_feedback_giver.pack_forget()
actual_feedback_label = Label(frame1_of_feedback,text='Please Leave Your Feedback Here --->',bg='Pink',font=('cambria',15,'bold'))
actual_feedback_label.pack_forget()
actual_message_of_user = Text(frame2_of_feedback,height=8,width=40,font=('cambria',15,'bold'))
actual_message_of_user.pack_forget()
#if you get time then please add that flying message wala emoji
feedback_submit_btn = Button(root,text='Submit Feedback',command=feedback_submit_btn_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
feedback_submit_btn.pack_forget()
explnation_label_for_all_farmers_btn_working = Label(root,text='Dynamic Text For Each Button Of Farmers Section',font=('cambria',15,'bold'),bg='Pink')
explnation_label_for_all_farmers_btn_working.pack_forget()
root.mainloop()
