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
import pygame
import os
from gtts import *
from all_file_path_for_dynamic_images import all_dynamic_images_path
import random
import threading
root = Tk()
root.title('Jai Shree Ram')
root.attributes('-fullscreen',True)
root.config(bg='Pink')
q = StringVar()
#Loading image on remaining buttons
loading_farmer_logo_img = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\farmer_logo.jpg')
resizing_farmer_logo_img = loading_farmer_logo_img.resize((40,40))
final_farmer_logo_img = ImageTk.PhotoImage(resizing_farmer_logo_img)

loading_analyst_logo_img = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\analyst.png')
resizing_analyst_logo_img = loading_analyst_logo_img.resize((40,40))
final_analyst_logo_img = ImageTk.PhotoImage(resizing_analyst_logo_img)

loading_pr_logo_img = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\profit_recommendation.jpg')
resizing_pr_img = loading_pr_logo_img.resize((40,40))
final_pr_img = ImageTk.PhotoImage(resizing_pr_img)

loading_proceed_img = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\proceed_logo.jpg')
resizing_proceed_img = loading_proceed_img.resize((40,40))
final_proceed_img = ImageTk.PhotoImage(resizing_proceed_img)

loading_pause_img = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\pause.jpg')
resizing_pause_img = loading_pause_img.resize((40,40))
final_pause_img = ImageTk.PhotoImage(resizing_pause_img)

loading_play_img = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\play.jpg')
resizing_play_img = loading_play_img.resize((40,40))
final_play_img = ImageTk.PhotoImage(resizing_play_img)

loading_stop_img = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\stop.png')
resizing_stop_img = loading_stop_img.resize((40,40))
final_stop_img = ImageTk.PhotoImage(resizing_stop_img)

loading_audio_img = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\audio.jpg')
resizing_audio_img = loading_audio_img.resize((40,40))
final_audio_img = ImageTk.PhotoImage(resizing_audio_img)

loading_gs_img = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\govt_schemes_logo.png')
resizing_gs_img = loading_gs_img.resize((40,40))
final_gs_img = ImageTk.PhotoImage(resizing_gs_img)

loading_feedback_img = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\feedback_log.png')
resizing_feedback_img = loading_feedback_img.resize((40,40))
final_feedback_img = ImageTk.PhotoImage(resizing_feedback_img)

loading_submit_feedback_img = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\submit.png')
resizing_submit_feedback_img = loading_submit_feedback_img.resize((40,40))
final_submit_feedback_img = ImageTk.PhotoImage(resizing_submit_feedback_img)

loading_profit_influence_img = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\profit_influence.png')
resizing_profit_influence_img = loading_profit_influence_img.resize((40,40))
final_profit_influence_img = ImageTk.PhotoImage(resizing_profit_influence_img)

loading_tools_img = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\tools.jpg')
resizing_tools_img = loading_tools_img.resize((40,40))
final_tools_img = ImageTk.PhotoImage(resizing_tools_img)

loading_method_img = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\method.png')
resizing_method_img = loading_method_img.resize((40,40))
final_method_img = ImageTk.PhotoImage(resizing_method_img)

loading_awarness_img = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\awarness.png')
resizing_awareness_img = loading_awarness_img.resize((40,40))
final_awarness_img = ImageTk.PhotoImage(resizing_awareness_img)

loading_accuracy_img = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\accuracy.jpg')
resizing_accuracy_img = loading_accuracy_img.resize((40,40))
final_accuracy_img = ImageTk.PhotoImage(resizing_accuracy_img)

def farmer_btn_func():
    left_frame_for_img.pack_forget()
    center_frame_for_center_img.pack_forget()
    random_path_taker_2 = random.choice(all_dynamic_images_path)
    loading_img_2 = Image.open(random_path_taker_2)
    resizing_img_2 = loading_img_2.resize((800,450))
    final_resized_img_2 = ImageTk.PhotoImage(resizing_img_2)
    label_for_right_img.config(image=final_resized_img_2)
    label_for_right_img.img = final_resized_img_2
    right_frame_for_img.pack(side='bottom',padx=40)
    main_dynamic_frame.pack_forget()
    analyst_name_confirmation_label.pack_forget()
    frame_for_farmers_btns_working.pack()
    profit_recmommandation.pack(side=LEFT,padx=10,pady=10)
    govt_schems_for_farmers.pack(side=LEFT,padx=10,pady=10)
    feedback_farmer_btn.pack(side=LEFT,padx=10,pady=10)
    back_to_main_page_btn_for_farmers.pack(side=LEFT,padx=10,pady=10)
def analyst_btn_func():
    random_path_taker_1 = random.choice(all_dynamic_images_path)
    random_path_taker_2 = random.choice(all_dynamic_images_path)
    random_path_taker_3 = random.choice(all_dynamic_images_path)
    loading_img_1 = Image.open(random_path_taker_1)
    loading_img_2 = Image.open(random_path_taker_2)
    loading_img_3 = Image.open(random_path_taker_3)
    resizing_img_1 = loading_img_1.resize((425,300))
    resizing_img_2 = loading_img_2.resize((425,300))
    resizing_img_3 = loading_img_3.resize((425,200))
    final_resized_img_1 = ImageTk.PhotoImage(resizing_img_1)
    final_resized_img_2 = ImageTk.PhotoImage(resizing_img_2)
    final_resized_img_3 = ImageTk.PhotoImage(resizing_img_3)
    label_for_left_img.config(image=final_resized_img_1)
    label_for_left_img.img = final_resized_img_1
    label_for_right_img.config(image=final_resized_img_2)
    label_for_right_img.img = final_resized_img_2
    label_for_center_img.config(image=final_resized_img_3)
    label_for_center_img.img = final_resized_img_3
    left_frame_for_img.pack(side='left',padx=50,pady=50)
    right_frame_for_img.pack(side='right',padx=50,pady=50)
    center_frame_for_center_img.pack(padx=15,pady=15)
    analyst_btn.pack_forget()
    entry_pass = simpledialog.askinteger('Security Purpose !','Enter password :- ')
    if entry_pass == 7588:
        analyst_name_label.config()
        analyst_name_label.pack(padx=10,pady=10)
        analyst_name_entry.config(textvariable=q)
        analyst_name_entry.pack(padx=10,pady=10)
        proceed_analyst_btn.pack(padx=10,pady=10)
    elif entry_pass != 7588:
        messagebox.showerror('Warning !!!','Please Insert Correct Password (If You Have Forgetted Password Then You Can Contact Developer By Clicking About Developer Button )')
        analyst_btn.pack()
        proceed_analyst_btn.pack_forget()
    else:
        pass
def play_audio_for_analyst_function():
    if pygame.mixer_music.get_busy():
        root.after(100,play_audio_for_analyst_function)
    else:
        pass
def proceed_analyst_btn_fun():
    time_keeper = datetime.now()
    time_converter = time_keeper.ctime()
    entry_name_taker = q.get()
    entry_name_number_checker = re.findall('[0-9]',entry_name_taker)
    if re.fullmatch(r'[A-Za-z]{2,}[A-Za-z_]*', entry_name_taker):
        left_frame_for_img.pack_forget()
        right_frame_for_img.pack_forget()
        random_path_taker_3 = random.choice(all_dynamic_images_path)
        loading_img_3 = Image.open(random_path_taker_3)
        resizing_img_3 = loading_img_3.resize((800,400))
        final_resized_img_3 = ImageTk.PhotoImage(resizing_img_3)
        label_for_center_img.config(image=final_resized_img_3)
        label_for_center_img.img = final_resized_img_3
        center_frame_for_center_img.pack(side='bottom',padx=30,pady=15)#Make here dynamic
        pygame.init()
        pygame.mixer_music.load('E:\\Prathamesh New\MSC-IT\\Sem 4\\sem 4 Project\\All_Project_Audios\\analyst.mp3')
        pygame.mixer_music.play()
        play_audio_for_analyst_function()
        file_path = 'e:\Prathamesh New\MSC-IT\Sem 3 Project\security_details_keeper.txt'
        with open (file_path,'a+') as file_path_2:
                    file_path_2.write('Login Name :- '+entry_name_taker+'\n')
                    file_path_2.write('Login Time And Date:- '+time_converter+'\n')
        proceed_analyst_btn.pack_forget()
        analyst_name_label.pack_forget()
        analyst_name_entry.delete(0,END)
        analyst_name_entry.pack_forget()
        main_dynamic_frame.pack_forget()
        analyst_name_confirmation_label.config(text='Welcome '+entry_name_taker)
        analyst_name_confirmation_label.pack()
        frame_for_analyst_btns_working.pack()
        farmers_info.pack(side=LEFT,padx=5,pady=10)
        profit_influencing_factor_btn.pack(side=LEFT,padx=5,pady=10)
        about_tools_btn.pack(side=LEFT,padx=5,pady=10)
        water_supply_method_btn.pack(side=LEFT,padx=5,pady=10)
        govt_plicy_awareness_analysis_btn.pack(side=LEFT,padx=5,pady=10)
        back_to_home_page_btn.pack(side='bottom',padx=5,pady=10)
        secondary_data_analysis_btn.pack(padx=10,pady=10)
        check_accuracy_btn.pack(padx=10,pady=10)
        messagebox.showwarning('Attention Here !!!',"Welcome, Analyst. You are now accessing the Agriculture Data Analyzer. Handle all data responsibly. Unauthorized sharing or modification is strictly prohibited.")
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
def back_to_home_page_btn_fun():
    current_time_for_logout = datetime.now()
    converting_current_time_into_human_readable_format = current_time_for_logout.ctime()
    file_path = 'e:\Prathamesh New\MSC-IT\Sem 3 Project\security_details_keeper.txt'
    with open (file_path,'a+') as file_path_2:
        file_path_2.write('Log Out Time And Date:- '+converting_current_time_into_human_readable_format+'\n\n')
    check_accuracy_btn.pack_forget()
    secondary_data_analysis_btn.pack_forget()
    analyst_name_confirmation_label.pack_forget()
    explanation_of_farmers_info_label.pack_forget()
    explaination_label_for_all_analysts_btns_working.pack_forget()
    frame_for_list_box_farmer_names.pack_forget()
    frame_for_analyst_btns_working.pack_forget()
    back_to_home_page_btn.pack_forget()
    random_path_taker_1 = random.choice(all_dynamic_images_path)
    random_path_taker_2 = random.choice(all_dynamic_images_path)
    random_path_taker_3 = random.choice(all_dynamic_images_path)
    loading_img_1 = Image.open(random_path_taker_1)
    loading_img_2 = Image.open(random_path_taker_2)
    loading_img_3 = Image.open(random_path_taker_3)
    resizing_img_1 = loading_img_1.resize((425,300))
    resizing_img_2 = loading_img_2.resize((425,300))
    resizing_img_3 = loading_img_3.resize((425,200))
    final_resized_img_1 = ImageTk.PhotoImage(resizing_img_1)
    final_resized_img_2 = ImageTk.PhotoImage(resizing_img_2)
    final_resized_img_3 = ImageTk.PhotoImage(resizing_img_3)
    label_for_left_img.config(image=final_resized_img_1)
    label_for_left_img.img = final_resized_img_1
    label_for_right_img.config(image=final_resized_img_2)
    label_for_right_img.img = final_resized_img_2
    label_for_center_img.config(image=final_resized_img_3)
    label_for_center_img.img = final_resized_img_3
    left_frame_for_img.pack(side='left',padx=50,pady=50)
    right_frame_for_img.pack(side='right',padx=50,pady=50)
    main_dynamic_frame.pack()
    center_frame_for_center_img.pack(padx=15,pady=15)
    analyst_btn.pack(padx=10,pady=10)
def farmers_info_func():
    random_path_taker_3 = random.choice(all_dynamic_images_path)
    loading_img_3 = Image.open(random_path_taker_3)
    resizing_img_3 = loading_img_3.resize((500,300))
    final_resized_img_3 = ImageTk.PhotoImage(resizing_img_3)
    label_for_center_img.config(image=final_resized_img_3)
    label_for_center_img.img = final_resized_img_3
    center_frame_for_center_img.pack(side='bottom',padx=15,pady=15)
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
    random_path_taker_3 = random.choice(all_dynamic_images_path)
    loading_img_3 = Image.open(random_path_taker_3)
    resizing_img_3 = loading_img_3.resize((500,300))
    final_resized_img_3 = ImageTk.PhotoImage(resizing_img_3)
    label_for_center_img.config(image=final_resized_img_3)
    label_for_center_img.img = final_resized_img_3
    center_frame_for_center_img.pack(side='bottom',padx=15,pady=15)
    analyst_name_confirmation_label.pack_forget()
    explanation_of_farmers_info_label.pack_forget()
    frame_for_list_box_farmer_names.pack_forget()
    explaination_label_for_all_analysts_btns_working.config(text='Explanation For Given Graph Is as Follows :- \npesticides_usage per month (in liters): Coefficient of \
-116.48: A negative coefficient means that as pesticide usage increases, the profit tends to decrease.\nThis indicate overuse of pesticides is negatively influencing to decrease profit.\n\
fertilizer_usage per month (in kg): Coefficient of  22.16: This positive coefficient suggests that increasing fertilizer usage is generally associated with an increase in profit, \nalthough it should use within require range\
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
    random_path_taker_3 = random.choice(all_dynamic_images_path)
    loading_img_3 = Image.open(random_path_taker_3)
    resizing_img_3 = loading_img_3.resize((500,300))
    final_resized_img_3 = ImageTk.PhotoImage(resizing_img_3)
    label_for_center_img.config(image=final_resized_img_3)
    label_for_center_img.img = final_resized_img_3
    center_frame_for_center_img.pack(side='bottom',padx=15,pady=15)
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
    random_path_taker_3 = random.choice(all_dynamic_images_path)
    loading_img_3 = Image.open(random_path_taker_3)
    resizing_img_3 = loading_img_3.resize((500,300))
    final_resized_img_3 = ImageTk.PhotoImage(resizing_img_3)
    label_for_center_img.config(image=final_resized_img_3)
    label_for_center_img.img = final_resized_img_3
    center_frame_for_center_img.pack(side='bottom',padx=15,pady=15)
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
    random_path_taker_3 = random.choice(all_dynamic_images_path)
    loading_img_3 = Image.open(random_path_taker_3)
    resizing_img_3 = loading_img_3.resize((500,300))
    final_resized_img_3 = ImageTk.PhotoImage(resizing_img_3)
    label_for_center_img.config(image=final_resized_img_3)
    label_for_center_img.img = final_resized_img_3
    center_frame_for_center_img.pack(side='bottom',padx=15,pady=15)
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
    plt.title('Distribution of Government Policies Awarness Ratio')
    plt.show()
def check_accuracy_btn_fun():
    random_path_taker_3 = random.choice(all_dynamic_images_path)
    loading_img_3 = Image.open(random_path_taker_3)
    resizing_img_3 = loading_img_3.resize((500,300))
    final_resized_img_3 = ImageTk.PhotoImage(resizing_img_3)
    label_for_center_img.config(image=final_resized_img_3)
    label_for_center_img.img = final_resized_img_3
    center_frame_for_center_img.pack(side='bottom',padx=15,pady=15)
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
R^2 Also Known As The coefficient of determination.\nThe R² score represents the proportion of the variance in the dependent variable (Profit(2023)) that is predictable from the independent variables (features).\nYour Model R^2 Is '+str(r2)+'\n\
This indicates that your model fits the data very well, as it explains almost all the variation/influences for Profit.')
    explaination_label_for_all_analysts_btns_working.pack()
#All Functions Of Farmers Buttons :- 
def profit_recmommandation_func():
    frame_for_feedback.pack_forget()
    explnation_label_for_all_farmers_btn_working.pack_forget()
    feedback_submit_btn.pack_forget()
    final_frame.pack_forget()
    frame_for_profit_recommandation_btn.pack()
    frame1_of_profit_recmommandation_btn.pack(side=LEFT)
    frame2_of_profit_recmommandation_btn.pack(side=RIGHT)
    label_for_farmer_name.pack(padx=5,pady=5)
    entry_for_farmer_name.pack(padx=5,pady=5)
    land_input_label.pack(padx=5,pady=5)
    entry_for_land_input.pack(padx=5,pady=5)
    label_for_type_of_tool.pack(padx=5,pady=5)
    input_for_agriculture_type_tool.pack(padx=5,pady=5)
    label_for_irrigation_method.pack(padx=5,pady=5)
    input_for_irrigation_method.pack(padx=5,pady=5)
    label_for_fertilizer_use.pack(padx=5,pady=5)
    entry_forfertilizer_use.pack(padx=5,pady=5)
    label_for_pesticide_use.pack(padx=5,pady=5)
    entry_for_pesticide_use.pack(padx=5,pady=5)
    label_for_profit_2021.pack(padx=5,pady=5)
    entry_for_profit_2021.pack(padx=5,pady=5)
    label_for_profit_2022.pack(padx=5,pady=5)
    entry_for_profit_2022.pack(padx=5,pady=5)
    label_for_profit_2023.pack(padx=5,pady=5)
    entry_for_profit_2023.pack(padx=5,pady=5)
    govt_policy_label.pack(padx=5,pady=5)
    input_for_policy_awareness.pack(padx=5,pady=5)
    proceed_for_profit_recommandation_btn.pack(padx=5,pady=5)
    random_path_taker_2 = random.choice(all_dynamic_images_path)
    loading_img_2 = Image.open(random_path_taker_2)
    resizing_img_2 = loading_img_2.resize((600,150))
    final_resized_img_2 = ImageTk.PhotoImage(resizing_img_2)
    label_for_right_img.config(image=final_resized_img_2)
    label_for_right_img.img = final_resized_img_2
    right_frame_for_img.pack(side='bottom')
    try:
        pygame.mixer_music.stop()
    except pygame.error:
        pass
def proceed_for_profit_recommandation_btn_func():
    global farmer_name_keeper
    global land_value_keeper
    global agriculture_tool_type_keeper
    global irrigation_method_holder
    global fetilizer_use_keeper
    global pesticide_use_keeper
    global profit_2021_keeper
    global profit_2022_keeper
    global profit_2023_keeper
    global policy_awareness_answer_keeper
    final_farmer_name_keeper = farmer_name_keeper.get()
    final_land_value_kepper = land_value_keeper.get()
    final_agriculture_tool_type_keeper = agriculture_tool_type_keeper.get()
    final_irrigation_method_holder = irrigation_method_holder.get()
    final_fetilizer_use_keeper = fetilizer_use_keeper.get()
    final_pesticide_use_keeper = pesticide_use_keeper.get()
    final_profit_2021_keeper= profit_2021_keeper.get()
    final_profit_2022_keeper = profit_2022_keeper.get()
    final_profit_2023_keeper= profit_2023_keeper.get()
    final_policy_awareness_answer_keeper = policy_awareness_answer_keeper.get()
    pattern_for_name_checking = r"^[A-Za-z]+(?: [A-Za-z]+)*$"
    final_pattern_for_name_checking = re.match(pattern_for_name_checking, final_farmer_name_keeper)
    pattern_for_land_checking = r"^[1-9]\d*$"
    final_pattern_for_land_checking = re.match(pattern_for_land_checking, final_land_value_kepper)
    pattern_for_fertilizer_cheking = r"^[1-9]\d*(?:\.\d+)?$"
    final_pattern_checking_for_fertilizer = re.match(pattern_for_fertilizer_cheking, final_fetilizer_use_keeper)
    final_pattern_checking_for_pesticide = re.match(pattern_for_fertilizer_cheking, final_pesticide_use_keeper)
    final_pattern_checking_for_profit_2021 = re.match(pattern_for_fertilizer_cheking, final_profit_2021_keeper)
    final_pattern_checking_for_profit_2022 = re.match(pattern_for_fertilizer_cheking, final_profit_2022_keeper)
    final_pattern_checking_for_profit_2023 = re.match(pattern_for_fertilizer_cheking, final_profit_2023_keeper)
    if final_pattern_for_name_checking and len(final_farmer_name_keeper)>= 3:
        if final_pattern_for_land_checking:
            if final_agriculture_tool_type_keeper == 'Options' or final_irrigation_method_holder == 'Options' or final_policy_awareness_answer_keeper == 'Options':
                messagebox.showerror('Warnning !!!','You Have Not Selected Options !!!')
            else:
                if final_pattern_checking_for_fertilizer:
                    if final_pattern_checking_for_pesticide:
                        if final_pattern_checking_for_profit_2021:
                            if final_pattern_checking_for_profit_2022:
                                if final_pattern_checking_for_profit_2023:
                                    frame_for_profit_recommandation_btn.pack_forget()
                                    proceed_for_profit_recommandation_btn.pack_forget()
                                    recommndation_saver_for_implementing_nlp.delete(0,END)
                                    final_frame_working()
                                else:
                                    messagebox.showerror('Warnning !!!','Please Give Valid Profit For 2023 ')
                            else:
                                messagebox.showerror('Warnning !!!','Please Give Valid Profit For 2022 ')
                        else:
                            messagebox.showerror('Warnning !!!','Please Give Valid Profit For 2021 ')
                        #Now use the same pattern for profits entry
                    else:
                        messagebox.showerror('Warnning !!!','You Are Giving Wrong Input For Pesticide Use .Please Check It ')
                else:
                    messagebox.showerror('Warnning !!!','You Are Giving Wrong Input For Fertilizer Use .Please Check It ')
        else:
            messagebox.showerror('Warnning !!!','Please Give Valid Input For Land Using For Farmming ')
    else:
        messagebox.showerror('Warning !!!','Please Give Valid Name')
#I am goint to make text conainer for my reference which will be pack forgeted 
recommndation_saver_for_implementing_nlp = Entry(root)
def func_to_not_freeze_window_while_playing_audio():
    if pygame.mixer_music.get_busy():
        root.after(100,func_to_not_freeze_window_while_playing_audio)
    else:
        pass
patience_img_loading = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\final_audio_loading.jpg')
resizing_patience_img_loading = patience_img_loading.resize((800,150))
final_patience_img = ImageTk.PhotoImage(resizing_patience_img_loading)
def volume_btn_working():
    volume_btn.pack_forget()
    label_for_right_img.config(image=final_patience_img)
    right_frame_for_img.pack(side='bottom',padx=40)
    final_all_content_for_audio = recommndation_saver_for_implementing_nlp.get()
    destination_for_audio = r'E:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Audios\dynamic_audio.mp3'
    if pygame.mixer.get_init():
        pygame.mixer_music.stop()
        pygame.mixer.quit()
    gtts_obj = gTTS(text=final_all_content_for_audio,lang='en',slow=False)
    gtts_obj.save(destination_for_audio)
    pygame.mixer.init()
    pygame.mixer_music.load(destination_for_audio)
    pygame.mixer_music.play()
    func_to_not_freeze_window_while_playing_audio()
    random_path_taker_2 = random.choice(all_dynamic_images_path)
    loading_img_2 = Image.open(random_path_taker_2)
    resizing_img_2 = loading_img_2.resize((800,150))
    final_resized_img_2 = ImageTk.PhotoImage(resizing_img_2)
    label_for_right_img.config(image=final_resized_img_2)
    label_for_right_img.img = final_resized_img_2
def pause_btn_working():
    try:
        pygame.mixer_music.pause()
    except pygame.error:
        pass
    random_path_taker_2 = random.choice(all_dynamic_images_path)
    loading_img_2 = Image.open(random_path_taker_2)
    resizing_img_2 = loading_img_2.resize((800,150))
    final_resized_img_2 = ImageTk.PhotoImage(resizing_img_2)
    label_for_right_img.config(image=final_resized_img_2)
    label_for_right_img.img = final_resized_img_2
    right_frame_for_img.pack(side='bottom',padx=40)
def resume_btn_working():
    try:
        pygame.mixer_music.unpause()
    except pygame.error:
        pass
    random_path_taker_2 = random.choice(all_dynamic_images_path)
    loading_img_2 = Image.open(random_path_taker_2)
    resizing_img_2 = loading_img_2.resize((800,150))
    final_resized_img_2 = ImageTk.PhotoImage(resizing_img_2)
    label_for_right_img.config(image=final_resized_img_2)
    label_for_right_img.img = final_resized_img_2
    right_frame_for_img.pack(side='bottom',padx=40)
def stop_btn_working():
    try:
        pygame.mixer_music.stop()
        random_path_taker_2 = random.choice(all_dynamic_images_path)
        loading_img_2 = Image.open(random_path_taker_2)
        resizing_img_2 = loading_img_2.resize((800,150))
        final_resized_img_2 = ImageTk.PhotoImage(resizing_img_2)
        label_for_right_img.config(image=final_resized_img_2)
        label_for_right_img.img = final_resized_img_2
        right_frame_for_img.pack(side='bottom',padx=40)
    except pygame.error:#in case if any person pressed stop button wiothout stating audio 
        pass
    volume_btn.pack(padx=10,pady=10,ipadx=5,ipady=5,side='left')
def final_frame_working():
    final_farmer_name_keeper = farmer_name_keeper.get()
    final_land_value_kepper = land_value_keeper.get()
    final_agriculture_tool_type_keeper = agriculture_tool_type_keeper.get()
    final_policy_awareness_answer_keeper = policy_awareness_answer_keeper.get()
    final_irrigation_method_holder = irrigation_method_holder.get()
    final_fetilizer_use_keeper = fetilizer_use_keeper.get()
    final_pesticide_use_keeper = pesticide_use_keeper.get()
    final_profit_2021_keeper = int(profit_2021_keeper.get())
    final_profit_2022_keeper = int(profit_2022_keeper.get())
    final_profit_2023_keeper = int(profit_2023_keeper.get())
    explnation_label_for_all_farmers_btn_working.config(text='Hello '+final_farmer_name_keeper+', Profit Recommendation Report Generated By Model Is As Follows .')
    explnation_label_for_all_farmers_btn_working.pack(padx=10,pady=10)
    recommndation_saver_for_implementing_nlp.insert(END,'Hello '+final_farmer_name_keeper+', Profit Recommendation Report Generated By Model Is As Follows. ')
    final_frame.pack()
    if final_agriculture_tool_type_keeper == 'Traditional':
        ideal_text_for_traditional_tool = 'Currently you are using traditional tools for farming , But model is recommending to use modern agriculture tools. \
\nmodern agriculture tools can improve efficiency , productivity & sustainability.'
        recommndation_saver_for_implementing_nlp.insert(END,ideal_text_for_traditional_tool)
        tool_explanation_label.config(text=ideal_text_for_traditional_tool)
        tool_explanation_label.pack(padx=10,pady=10)
    elif final_agriculture_tool_type_keeper == 'Modern':
        ideal_text_for_Modern_tool = 'Currently you are using modern agriculture tools which haves several advantages like efficiency , productivity & sustainability.\
\n Model is giving suggestion that keep regular maintaince of your all modern tools in order to avoide adverse effects on our environment.'
        recommndation_saver_for_implementing_nlp.insert(END,ideal_text_for_Modern_tool)
        tool_explanation_label.config(text=ideal_text_for_Modern_tool)
        tool_explanation_label.pack(padx=10,pady=10)
    else:
        ideal_text_for_hybird_tool = 'Currently you are using hybrid agriculture tools for farmming,But model is recommending to fully merge with modern agriculture tools. \
\nmodern agriculture tools can improve efficiency , productivity & sustainability.'
        recommndation_saver_for_implementing_nlp.insert(END,ideal_text_for_hybird_tool)
        tool_explanation_label.config(text=ideal_text_for_hybird_tool)
        tool_explanation_label.pack(padx=10,pady=10)
    if final_irrigation_method_holder == 'Drip':
        ideal_text_for_Drip_irrigation_method = 'You are using drip irrigation method in farmming.Keep usage of drip irrigation method because,it gives benifits like Water Conservation & soil erosion redection .'
        recommndation_saver_for_implementing_nlp.insert(END,ideal_text_for_Drip_irrigation_method)
        irrigation_explanation_label.config(text=ideal_text_for_Drip_irrigation_method)
        irrigation_explanation_label.pack()
    elif final_irrigation_method_holder == 'Sprinkler':
        ideal_text_for_Sprinkler_irrigation_method = 'Currently you are using sprinkler irrigation method which has several disadvantages like water wastage , high cost. \
\nBecause of all such reasons, Model is recommending to implement drip irrigation method for farmming.'
        recommndation_saver_for_implementing_nlp.insert(END,ideal_text_for_Sprinkler_irrigation_method)
        irrigation_explanation_label.config(text=ideal_text_for_Sprinkler_irrigation_method)
        irrigation_explanation_label.pack()
    else:
        pass
    try:
        current_fertilizer_range_1 = int(final_land_value_kepper ) * 2
        current_fertilizer_range_2 = int(final_land_value_kepper) * 3
    except ValueError:
        current_fertilizer_range_1 = float(final_land_value_kepper ) * 2
        current_fertilizer_range_2 = float(final_land_value_kepper) * 3
    ideal_text_for_fertilizer_explanation_label = 'Currently you are using '+ final_fetilizer_use_keeper+' kg fertilizer per month. \
\n An ideal range for fertilizer recommended by model is '+str(current_fertilizer_range_1)+' to '+str(current_fertilizer_range_2) + ' kg fertilizer per month. '
    recommndation_saver_for_implementing_nlp.insert(END,ideal_text_for_fertilizer_explanation_label)
    fertilizer_expalnation_label.config(text=ideal_text_for_fertilizer_explanation_label)
    fertilizer_expalnation_label.pack(padx=10,pady=10)
    try:
        current_pesticide_range_1 = int(final_land_value_kepper ) / 2 + 5
        current_pesticide_range_2 = int(final_land_value_kepper ) / 2 - 5
    except ValueError:
        current_pesticide_range_1 = float(final_land_value_kepper ) / 2 + 5
        current_pesticide_range_2 = float(final_land_value_kepper ) / 2 - 5
    ideal_text_for_pesticide_explanation_label = 'Currently you are using '+ final_pesticide_use_keeper+' liter pesticide per month.\
\n An ideal range for pesticide recommended by model is '+str(current_pesticide_range_2)+' to '+str(current_pesticide_range_1) + ' liter pesticide per month.'
    recommndation_saver_for_implementing_nlp.insert(END,ideal_text_for_pesticide_explanation_label)
    pesticide_explanation_label.config(text=ideal_text_for_pesticide_explanation_label)
    pesticide_explanation_label.pack(padx=10,pady=10)
    if final_profit_2021_keeper > final_profit_2022_keeper > final_profit_2023_keeper:
        ideal_text_for_profit_explanation_label = "Model has observed that your profit is constantly decreasing. Implement all recommendations given by the model."
        recommndation_saver_for_implementing_nlp.insert(END,ideal_text_for_profit_explanation_label)
        profit_explanation_label.config(text=ideal_text_for_profit_explanation_label)
        profit_explanation_label.pack(padx=10,pady=10)
    elif final_profit_2023_keeper > final_profit_2022_keeper > final_profit_2021_keeper:
        ideal_text_for_profit_explanation_label = "Model has observed that your profit is constantly increasing. Implement all recommendations to achieve more profit."
        recommndation_saver_for_implementing_nlp.insert(END,ideal_text_for_profit_explanation_label)
        profit_explanation_label.config(text=ideal_text_for_profit_explanation_label)
        profit_explanation_label.pack(padx=10,pady=10)
    elif final_profit_2021_keeper == final_profit_2022_keeper == final_profit_2023_keeper:
        ideal_text_for_profit_explanation_label = "Model has observed that your profit is stable but not increasing. Implement all recommendations for growth."
        recommndation_saver_for_implementing_nlp.insert(END,ideal_text_for_profit_explanation_label)
        profit_explanation_label.config(text=ideal_text_for_profit_explanation_label)
        profit_explanation_label.pack(padx=10,pady=10)
    elif final_profit_2021_keeper > final_profit_2022_keeper < final_profit_2023_keeper:
        ideal_text_for_profit_explanation_label = "Model has observed that your profit dropped in 2022 but recovered in 2023. Implement all recommendations to maintain growth."
        recommndation_saver_for_implementing_nlp.insert(END,ideal_text_for_profit_explanation_label)
        profit_explanation_label.config(text=ideal_text_for_profit_explanation_label)
        profit_explanation_label.pack(padx=10,pady=10)
    elif final_profit_2021_keeper < final_profit_2022_keeper > final_profit_2023_keeper:
        ideal_text_for_profit_explanation_label = "Model has observed that your profit increased in 2022 but dropped in 2023. Implement all recommendations to prevent future losses."
        recommndation_saver_for_implementing_nlp.insert(END,ideal_text_for_profit_explanation_label)
        profit_explanation_label.config(text=ideal_text_for_profit_explanation_label)
        profit_explanation_label.pack(padx=10,pady=10)
    elif final_profit_2021_keeper > final_profit_2022_keeper == final_profit_2023_keeper:
        ideal_text_for_profit_explanation_label = "Model has observed that you have not gained profit since 2022. Implement all recommendations given by the model."
        recommndation_saver_for_implementing_nlp.insert(END,ideal_text_for_profit_explanation_label)
        profit_explanation_label.config(text=ideal_text_for_profit_explanation_label)
        profit_explanation_label.pack()
    elif final_profit_2021_keeper < final_profit_2022_keeper == final_profit_2023_keeper:
        ideal_text_for_profit_explanation_label = "Model has observed that you gained profit in 2022, but it is now stagnant. Implement all recommendations for further growth."
        recommndation_saver_for_implementing_nlp.insert(END,ideal_text_for_profit_explanation_label)
        profit_explanation_label.config(text=ideal_text_for_profit_explanation_label)
        profit_explanation_label.pack()
    elif final_profit_2021_keeper == final_profit_2022_keeper and final_profit_2023_keeper > final_profit_2022_keeper:
        ideal_text_for_profit_explanation_label = "Model has observed that profit was neutral in 2021 & 2022, but increased in 2023. Implement recommendations to maintain consistency."
        recommndation_saver_for_implementing_nlp.insert(END,ideal_text_for_profit_explanation_label)
        profit_explanation_label.config(text=ideal_text_for_profit_explanation_label)
        profit_explanation_label.pack()
    elif final_profit_2021_keeper == final_profit_2022_keeper and final_profit_2023_keeper < final_profit_2022_keeper:
        ideal_text_for_profit_explanation_label = "Model has observed that profit was stable in 2021 & 2022, but dropped in 2023. Implement all recommendations to recover losses."
        recommndation_saver_for_implementing_nlp.insert(END,ideal_text_for_profit_explanation_label)
        profit_explanation_label.config(text=ideal_text_for_profit_explanation_label)
        profit_explanation_label.pack()
    else:
        ideal_text_for_profit_explanation_label = "Model has observed that your profit is fluctuating. Implement all recommendations for stability."
        recommndation_saver_for_implementing_nlp.insert(END,ideal_text_for_profit_explanation_label)
        profit_explanation_label.config(text=ideal_text_for_profit_explanation_label)
        profit_explanation_label.pack()
    if final_policy_awareness_answer_keeper == 'Yes':
        ideal_text_for_govt_polcies_explanation_label = 'As you are aware of Goverment Policies , But to get all latest policies updates model is recommending you to check goverment schems section. '
        recommndation_saver_for_implementing_nlp.insert(END,ideal_text_for_govt_polcies_explanation_label)
        govt_polcies_explanation_label.config(text=ideal_text_for_govt_polcies_explanation_label)
        govt_polcies_explanation_label.pack()
    else:
        ideal_text_for_govt_polcies_explanation_label = 'As you are not aware about goverment policies , Model is recommending you to check goverment schemes section to get all latest update about goverment policies made for Farmers.'
        recommndation_saver_for_implementing_nlp.insert(END,ideal_text_for_govt_polcies_explanation_label)
        govt_polcies_explanation_label.config(text=ideal_text_for_govt_polcies_explanation_label)
        govt_polcies_explanation_label.pack()
    label_for_volume_btn.pack(side='left',padx=60)
    volume_btn.config(command=lambda: threading.Thread(target=volume_btn_working).start())
    volume_btn.pack(padx=15,pady=7,ipadx=5,ipady=5,side='left')
    pause_btn_for_recommendation.pack(padx=15,pady=7,ipadx=5,ipady=5,side='left')
    resume_btn_for_recommendation.pack(padx=15,pady=7,ipadx=5,ipady=5,side='left')
    stop_btn_for_recommendation.pack(padx=15,pady=7,ipadx=5,ipady=5,side='left')
    random_path_taker_2 = random.choice(all_dynamic_images_path)
    loading_img_2 = Image.open(random_path_taker_2)
    resizing_img_2 = loading_img_2.resize((800,150))
    final_resized_img_2 = ImageTk.PhotoImage(resizing_img_2)
    label_for_right_img.config(image=final_resized_img_2)
    label_for_right_img.img = final_resized_img_2
    right_frame_for_img.pack(side='bottom',padx=10)
    entry_for_farmer_name.delete(0,END)
    entry_for_land_input.delete(0,END)
    agriculture_tool_type_keeper.set('Options')
    irrigation_method_holder.set('Options')
    policy_awareness_answer_keeper.set('Options')
    entry_forfertilizer_use.delete(0,END)
    entry_for_pesticide_use.delete(0,END)
    entry_for_profit_2021.delete(0,END)
    entry_for_profit_2022.delete(0,END)
    entry_for_profit_2023.delete(0,END)
def govt_schems_for_farmers_func():
    try:
        pygame.mixer_music.stop()
    except pygame.error:
        pass
    random_path_taker_2 = random.choice(all_dynamic_images_path)
    loading_img_2 = Image.open(random_path_taker_2)
    resizing_img_2 = loading_img_2.resize((800,450))
    final_resized_img_2 = ImageTk.PhotoImage(resizing_img_2)
    label_for_right_img.config(image=final_resized_img_2)
    label_for_right_img.img = final_resized_img_2
    right_frame_for_img.pack(side='bottom',padx=40)
    frame_for_feedback.pack_forget()
    feedback_submit_btn.pack_forget()
    final_frame.pack_forget()
    frame_for_profit_recommandation_btn.pack_forget()
    proceed_for_profit_recommandation_btn.pack_forget()
    explnation_label_for_all_farmers_btn_working.pack_forget()
    webbrowser.open('https://agriwelfare.gov.in/en/Major')
def feedback_farmer_btn_func():
    try:
        pygame.mixer_music.stop()
    except pygame.error:
        pass
    explnation_label_for_all_farmers_btn_working.pack_forget()
    frame_for_profit_recommandation_btn.pack_forget()
    proceed_for_profit_recommandation_btn.pack_forget()
    final_frame.pack_forget()
    frame_for_feedback.pack()
    frame1_of_feedback.pack(side=LEFT)
    frame2_of_feedback.pack(side=RIGHT)
    name_label_for_feedback.pack(padx=10,pady=10)
    name_of_feedback_giver.pack(padx=10,pady=10)
    actual_feedback_label.pack(padx=10,pady=80)
    actual_message_of_user.pack(padx=10,pady=10)
    feedback_submit_btn.pack(padx=10,pady=10)
    random_path_taker_2 = random.choice(all_dynamic_images_path)
    loading_img_2 = Image.open(random_path_taker_2)
    resizing_img_2 = loading_img_2.resize((800,250))
    final_resized_img_2 = ImageTk.PhotoImage(resizing_img_2)
    label_for_right_img.config(image=final_resized_img_2)
    label_for_right_img.img = final_resized_img_2
    right_frame_for_img.pack(side='bottom',padx=40)
def feedback_submit_btn_func():
    feedback_submit_btn.pack_forget()
    frame_for_feedback.pack_forget()
    feedback_storer = actual_message_of_user.get("1.0",END)
    file_name_keeper = name_of_feedback_giver.get()
    #pattern_1 = r'^[A-Za-z][A-Za-z\s]*$'#for checking file name
    pattern_2 = r'^[^\s].*$'#for checking actual message 
    file_name_cheker = re.fullmatch(r'[A-Za-z]{2,}[A-Za-z_ ]*', file_name_keeper)
    feedback_checker = re.match(pattern_2, feedback_storer)
    if file_name_cheker and feedback_checker:
        file_path = 'E:\\Prathamesh New\\MSC-IT\\Sem 3 Project\\All_Feedbacks\\'+file_name_keeper+'.txt'
        directory = 'E:\\Prathamesh New\\MSC-IT\\Sem 3 Project\\All_Feedbacks\\'
        duplicate_file_count = 1
        while os.path.exists(file_path):
            file_path = os.path.join(directory,f"{file_name_keeper}{duplicate_file_count}.txt")
            duplicate_file_count += 1
        with open(file_path,'w')as file_obj_1:
            file_obj_1.write(feedback_storer)
        explnation_label_for_all_farmers_btn_working.config(text='Thank You So Much '+file_name_keeper+' For Giving Feedback !!')
        explnation_label_for_all_farmers_btn_working.pack()
        random_path_taker_2 = random.choice(all_dynamic_images_path)
        loading_img_2 = Image.open(random_path_taker_2)
        resizing_img_2 = loading_img_2.resize((800,450))
        final_resized_img_2 = ImageTk.PhotoImage(resizing_img_2)
        label_for_right_img.config(image=final_resized_img_2)
        label_for_right_img.img = final_resized_img_2
        right_frame_for_img.pack(side='bottom',padx=40)
    else:
        messagebox.showwarning('Error','Please Give Valid Name(Without Any Numbers and Special Characters) And Message')
    name_of_feedback_giver.delete(0,END)
    actual_message_of_user.delete("1.0",END)
def back_to_main_page_btn_for_farmers_func():
    try:
        pygame.mixer_music.stop()
    except pygame.error:
        pass
    random_path_taker_1 = random.choice(all_dynamic_images_path)
    random_path_taker_2 = random.choice(all_dynamic_images_path)
    random_path_taker_3 = random.choice(all_dynamic_images_path)
    loading_img_1 = Image.open(random_path_taker_1)
    loading_img_2 = Image.open(random_path_taker_2)
    loading_img_3 = Image.open(random_path_taker_3)
    resizing_img_1 = loading_img_1.resize((425,300))
    resizing_img_2 = loading_img_2.resize((425,300))
    resizing_img_3 = loading_img_3.resize((425,200))
    final_resized_img_1 = ImageTk.PhotoImage(resizing_img_1)
    final_resized_img_2 = ImageTk.PhotoImage(resizing_img_2)
    final_resized_img_3 = ImageTk.PhotoImage(resizing_img_3)
    label_for_left_img.config(image=final_resized_img_1)
    label_for_left_img.img = final_resized_img_1
    label_for_right_img.config(image=final_resized_img_2)
    label_for_right_img.img = final_resized_img_2
    label_for_center_img.config(image=final_resized_img_3)
    label_for_center_img.img = final_resized_img_3
    left_frame_for_img.pack(side='left',padx=50,pady=50)
    right_frame_for_img.pack(side='right',padx=50,pady=50)
    frame_for_farmers_btns_working.pack_forget()
    frame_for_feedback.pack_forget()
    feedback_submit_btn.pack_forget()
    explnation_label_for_all_farmers_btn_working.pack_forget()
    frame_for_profit_recommandation_btn.pack_forget()
    proceed_for_profit_recommandation_btn.pack_forget()
    final_frame.pack_forget()
    main_dynamic_frame.pack()
    center_frame_for_center_img.pack(padx=10,pady=10)
#will give insta image to insta button 
insta_img = Image.open('c:\\Prathamesh\\python_txt_files\\insta_logo.jpg')
updated_insta_img = insta_img.resize((35,35))
final_updated_insta_img = ImageTk.PhotoImage(updated_insta_img)
#will give linkdin image to linkdin button 
linkdin_img = Image.open('c:\\Prathamesh\\python_txt_files\\lindin_logo.jpg')
update_linkdin_img = linkdin_img.resize((40,40))
final_linkdin_img = ImageTk.PhotoImage(update_linkdin_img)
#will give gmail image to gmail button
gmail_img = Image.open('c:\\Prathamesh\\python_txt_files\\gmail_logo.jpg')
update_gmail_img = gmail_img.resize((40,40))
final_update_gmail_img = ImageTk.PhotoImage(update_gmail_img)
#will give github image to github button 
github_img_loader = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\git_hub_logo.jpg')
updating_github_img_loader = github_img_loader.resize((40,40))
final_img_for_github_btn = ImageTk.PhotoImage(updating_github_img_loader)
#will give home image to some button 
home_img_loader = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\home_img_updated.jpg')
updating_home_img = home_img_loader.resize((40,40))
final_img_for_home_btn = ImageTk.PhotoImage(updating_home_img)
#loading left image of developer for about developer button 
developer_image = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\Prathu_blezer_photo.jpg')
updating_developer_img = developer_image.resize((200,450))
final_developer_img = ImageTk.PhotoImage(updating_developer_img)
#loading right image of developer for about developer button 
developer_right_image = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\prathamesh_saptshrungi.jpg')
updating_developer_right_img = developer_right_image.resize((250,450))
final_developer_right_img = ImageTk.PhotoImage(updating_developer_right_img)
def insta_profile():
    webbrowser.open('https://www.instagram.com/prathameshghure?utm_source=qr&igsh=MXZwZjhyZnBsb2hpNA==')
def linkdin_profile():
    webbrowser.open('https://www.linkedin.com/in/prathamesh-ghure-07310227a?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app')
def gmail_profile():
    mail_id_label = Label(window_for_about_developer_btn,text='Mail Id Of Developer :- prathameshghure26@gmail.com ',bg='Light Yellow',font=('cambria',15,'bold'))
    mail_id_label.pack()
def git_hub_btn_working():
    webbrowser.open('https://github.com/Prathamesh-P-Ghure')
def back_to_home_from_about_window_working():
    window_for_about_developer_btn.destroy()
window_for_about_developer_btn = None
def about_func():
    random_path_taker_1 = random.choice(all_dynamic_images_path)
    random_path_taker_2 = random.choice(all_dynamic_images_path)
    random_path_taker_3 = random.choice(all_dynamic_images_path)
    loading_img_1 = Image.open(random_path_taker_1)
    loading_img_2 = Image.open(random_path_taker_2)
    loading_img_3 = Image.open(random_path_taker_3)
    resizing_img_1 = loading_img_1.resize((425,300))
    resizing_img_2 = loading_img_2.resize((425,300))
    resizing_img_3 = loading_img_3.resize((425,200))
    final_resized_img_1 = ImageTk.PhotoImage(resizing_img_1)
    final_resized_img_2 = ImageTk.PhotoImage(resizing_img_2)
    final_resized_img_3 = ImageTk.PhotoImage(resizing_img_3)
    label_for_left_img.config(image=final_resized_img_1)
    label_for_left_img.img = final_resized_img_1
    label_for_right_img.config(image=final_resized_img_2)
    label_for_right_img.img = final_resized_img_2
    label_for_center_img.config(image=final_resized_img_3)
    label_for_center_img.img = final_resized_img_3
    global window_for_about_developer_btn
    if window_for_about_developer_btn and window_for_about_developer_btn.winfo_exists():
        messagebox.showerror('Attention Here','Already About Developer Windoe Tab Is Openned !!!')
    else:
        analyst_name_confirmation_label.pack_forget()
        window_for_about_developer_btn = Toplevel()
        window_for_about_developer_btn.geometry('1000x600+250+175')
        window_for_about_developer_btn.config(bg='Light Yellow')
        frame_for_about_developer_btn_woriking = Frame(window_for_about_developer_btn,bg='Light Yellow')
        left_frame_in_frame_for_about_developer_btn_woriking = Frame(frame_for_about_developer_btn_woriking,bg='Black',bd=2)
        right_frame_in_frame_for_about_developer_btn_working = Frame(frame_for_about_developer_btn_woriking,bg='Black',bd=2)
        frame_for_about_developer_btn_woriking.pack(padx=10,pady=10,ipadx=10,ipady=10)
        left_frame_in_frame_for_about_developer_btn_woriking.pack(side=LEFT)
        right_frame_in_frame_for_about_developer_btn_working.pack(side=RIGHT)
        label_to_display_developer_left_img = Label(left_frame_in_frame_for_about_developer_btn_woriking,image=final_developer_img,compound='bottom')
        label_to_display_developer_left_img.pack()
        about_label = Label(frame_for_about_developer_btn_woriking,text='You Can Connect Developer On Following Platforms',font=('cambria',15,'bold'),bg='Light Yellow')
        about_label.pack(padx=10,pady=10)
        insta_btn = Button(frame_for_about_developer_btn_woriking,text='Instagram',command=insta_profile,compound=RIGHT,image=final_updated_insta_img,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
        insta_btn.pack(padx=10,pady=10,ipadx=5,ipady=5)
        linkdin_btn = Button(frame_for_about_developer_btn_woriking,text='Linkdin',command=linkdin_profile,compound=RIGHT,image=final_linkdin_img,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
        linkdin_btn.pack(padx=10,pady=10,ipadx=5,ipady=5)
        gmail_btn = Button(frame_for_about_developer_btn_woriking,text='Gmail ',command=gmail_profile,image=final_update_gmail_img,compound=RIGHT,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
        gmail_btn.pack(padx=10,pady=10,ipadx=5,ipady=5)
        git_hub_btn = Button(frame_for_about_developer_btn_woriking,text='GitHub ',image=final_img_for_github_btn,command=git_hub_btn_working,compound='right',font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
        git_hub_btn.pack(padx=10,pady=10,ipadx=5,ipady=5)
        back_to_home_from_about_window = Button(frame_for_about_developer_btn_woriking,text='Home ',command=back_to_home_from_about_window_working,compound=RIGHT,image=final_img_for_home_btn,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
        back_to_home_from_about_window.pack(padx=10,pady=10,ipadx=5,ipady=5)
        label_to_display_developer_right_img = Label(right_frame_in_frame_for_about_developer_btn_working,image=final_developer_right_img)
        label_to_display_developer_right_img.pack()
heading_frame = Frame(root)
heading_frame.config(bd=4,bg='black')
heading_frame.pack(padx=10,pady=10)
heading_label = Label(heading_frame,text='Agriculture Data Analyzer',font=('cambria',20,'bold'),bg='Pink')
heading_label.pack()
left_frame_for_img = Frame(root,bg='black',bd=4)
left_frame_for_img.pack(side='left',padx=50,pady=50)
first_static_img_for_left = Image.open('e:\\Prathamesh New\\MSC-IT\\Sem 4\\sem 4 Project\\All_Project_Images\\di22.jpeg')
updating_first_static_widget_for_left = first_static_img_for_left.resize((425,300))
final_updating_first_static_widget_for_left = ImageTk.PhotoImage(updating_first_static_widget_for_left)
label_for_left_img = Label(left_frame_for_img,image=final_updating_first_static_widget_for_left)
label_for_left_img.pack()
right_frame_for_img = Frame(root,bg='black',bd=4)
right_frame_for_img.pack(side='right',padx=50,pady=50)
first_static_img_for_right = Image.open('e:\\Prathamesh New\\MSC-IT\\Sem 4\\sem 4 Project\\All_Project_Images\\di_1.jpg')
updating_first_static_widget_for_right = first_static_img_for_right.resize((425,300))#width,height
final_updating_first_static_widget_for_right = ImageTk.PhotoImage(updating_first_static_widget_for_right)
label_for_right_img = Label(right_frame_for_img,image=final_updating_first_static_widget_for_right)
label_for_right_img.pack()
main_dynamic_frame = Frame(root)
main_dynamic_frame.config(bg='Pink')
main_dynamic_frame.pack()
center_frame_for_center_img = Frame(root,bg='black',bd=4)
center_frame_for_center_img.pack()
first_static_img_for_center = Image.open('e:\\Prathamesh New\\MSC-IT\\Sem 4\\sem 4 Project\\All_Project_Images\\di28.jpg')
updating_first_static_widget_for_center = first_static_img_for_center.resize((425,200))#width,height
final_updating_first_static_widget_for_center = ImageTk.PhotoImage(updating_first_static_widget_for_center)
label_for_center_img = Label(center_frame_for_center_img,image=final_updating_first_static_widget_for_center)
label_for_center_img.pack()
farmer_btn = Button(main_dynamic_frame,text='Access This Model As A Farmer',command=farmer_btn_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10,image=final_farmer_logo_img,compound='right')
farmer_btn.pack(ipadx=5,padx=10,ipady=5,pady=10)
analyst_btn = Button(main_dynamic_frame,text='Access This Model As A Analyst',command=analyst_btn_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10,image=final_analyst_logo_img,compound='right')
analyst_btn.pack(ipadx=5,padx=10,ipady=5,pady=10)
about_img = Image.open('c:\\Prathamesh\\python_txt_files\\about.jpg')
update_about_img = about_img.resize((40,40))
final_update_about_img = ImageTk.PhotoImage(update_about_img)
about_btn = Button(main_dynamic_frame,text='About Developer !!',command=about_func,compound=RIGHT,image=final_update_about_img,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
about_btn.pack(padx=10,pady=10)
#Static Widgets :- 
analyst_name_label = Label(main_dynamic_frame,text='Enter Your Name Below For Security References\n(Without Any Space) :- ',font=('cambria',15,'bold'),bg='Pink')
analyst_name_label.pack_forget()
analyst_name_entry = Entry(main_dynamic_frame,font=('cambria',15,'bold'))
analyst_name_entry.pack_forget()
proceed_analyst_btn = Button(main_dynamic_frame,text='Proceed',command=proceed_analyst_btn_fun,font=('cambria',15,'bold'),image=final_proceed_img,compound='right',activebackground='tomato',borderwidth=10)
proceed_analyst_btn.pack_forget()
exit_yes_no_window = None
def exit_btn_func():
    random_path_taker_1 = random.choice(all_dynamic_images_path)
    random_path_taker_2 = random.choice(all_dynamic_images_path)
    random_path_taker_3 = random.choice(all_dynamic_images_path)
    loading_img_1 = Image.open(random_path_taker_1)
    loading_img_2 = Image.open(random_path_taker_2)
    loading_img_3 = Image.open(random_path_taker_3)
    resizing_img_1 = loading_img_1.resize((425,300))
    resizing_img_2 = loading_img_2.resize((425,300))
    resizing_img_3 = loading_img_3.resize((425,200))
    final_resized_img_1 = ImageTk.PhotoImage(resizing_img_1)
    final_resized_img_2 = ImageTk.PhotoImage(resizing_img_2)
    final_resized_img_3 = ImageTk.PhotoImage(resizing_img_3)
    label_for_left_img.config(image=final_resized_img_1)
    label_for_left_img.img = final_resized_img_1
    label_for_right_img.config(image=final_resized_img_2)
    label_for_right_img.img = final_resized_img_2
    label_for_center_img.config(image=final_resized_img_3)
    label_for_center_img.img = final_resized_img_3
    global exit_yes_no_window
    if exit_yes_no_window and exit_yes_no_window.winfo_exists():
        messagebox.showwarning('Tab Openned','Exit Button Tab Is Already Open ...I guess you have minimized that window check it !!!')
    else:
        exit_yes_no_window = Toplevel()
        exit_yes_no_window.title('Exit ?')
        exit_yes_no_window.geometry('1000x500+250+175')
        exit_yes_no_window.config(bg='Light Green')
        label_for_yes_no_exit = Label(exit_yes_no_window,text='Are You Sure Want To Take Exit ?',bg='Light Green',font=('cambria',25,'bold'))
        yes_btn_for_exit = Button(exit_yes_no_window,text='Yes',command=yes_btn_for_exit_working,font=('cambria',25,'bold'),activebackground='tomato',borderwidth=10,image=final_yes_img,compound='right')
        no_btn_for_exit = Button(exit_yes_no_window,text='No',command=no_btn_for_exit_working,font=('cambria',25,'bold'),activebackground='tomato',borderwidth=10,image=final_no_img,compound='right')
        label_for_yes_no_exit.pack(padx=10,pady=10)
        yes_btn_for_exit.pack(padx=10,pady=10,ipadx=10,ipady=10)
        no_btn_for_exit.pack(padx=10,pady=10,ipadx=10,ipady=10)
        frame_to_display_thank_u_img = Frame(exit_yes_no_window,bg='black',bd=4)
        frame_to_display_thank_u_img.pack(padx=10,pady=10)
        label_to_display_thank_you_img = Label(frame_to_display_thank_u_img,image=final_thank_u_img)
        label_to_display_thank_you_img.pack()
exit_img = Image.open('c:\\Prathamesh\\python_txt_files\\exit.jpg')
update_exit_img = exit_img.resize((40,40))
final_update_exit_img = ImageTk.PhotoImage(update_exit_img)
exit_btn = Button(main_dynamic_frame,text='Exit',command=exit_btn_func,image=final_update_exit_img,compound=RIGHT,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
exit_btn.pack(padx=10,pady=10)
#loading_yes_img for exit
loading_yes_image = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\yes.jpg')
resizing_yes_img = loading_yes_image.resize((50,50))
final_yes_img = ImageTk.PhotoImage(resizing_yes_img)
#loading_no_img for exit
loading_no_image = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\no.jpg')
resizing_no_img = loading_no_image.resize((50,50))
final_no_img = ImageTk.PhotoImage(resizing_no_img)
#loading thank you image at end in exit yes no window
loading_thank_u_image = Image.open(r'e:\Prathamesh New\MSC-IT\Sem 4\sem 4 Project\All_Project_Images\thank_you.jpg')
resizing_thank_u_img = loading_thank_u_image.resize((500,300))
final_thank_u_img = ImageTk.PhotoImage(resizing_thank_u_img)
#statics widgets for analyst buttons :- 
frame_for_analyst_btns_working = Frame(root,bg='Pink')
frame_for_analyst_btns_working.pack_forget()
analyst_name_confirmation_label = Label(frame_for_analyst_btns_working,text='Dynamic Welcome With Name',font=('cambria',15,'bold'),bg='pink')
analyst_name_confirmation_label.pack_forget()
back_to_home_page_btn = Button(frame_for_analyst_btns_working,text='Home',command=back_to_home_page_btn_fun,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10,image=final_img_for_home_btn,compound='right')
back_to_home_page_btn.pack_forget()
farmers_info = Button(frame_for_analyst_btns_working,text='Farmers Info',command=farmers_info_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10,image=final_update_about_img,compound='right')
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
profit_influencing_factor_btn = Button(frame_for_analyst_btns_working,text='Show Profit Influencing Factor',command=profit_influencing_factor_btn_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10,image=final_profit_influence_img,compound='right')
profit_influencing_factor_btn.pack_forget()
about_tools_btn = Button(frame_for_analyst_btns_working,text='Tools Analysis',command=about_tools_btn_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10,image=final_tools_img,compound='right')
about_tools_btn.pack_forget()
water_supply_method_btn = Button(frame_for_analyst_btns_working,text='Methods Analysis',command=water_supply_method_btn_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10,image=final_method_img,compound='right')
water_supply_method_btn.pack_forget()
govt_plicy_awareness_analysis_btn = Button(frame_for_analyst_btns_working,text='Policies Awareness Ratio',command=govt_plicy_awareness_analysis_btn_fun,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10,image=final_awarness_img,compound='right')
govt_plicy_awareness_analysis_btn.pack_forget()
check_accuracy_btn = Button(root,text='Check Accuracy',command=check_accuracy_btn_fun,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10,image=final_accuracy_img,compound='right')
check_accuracy_btn.pack_forget()
#Static Widgets For Farmer Button :-
frame_for_farmers_btns_working = Frame(root,bg='Pink')
frame_for_farmers_btns_working.pack_forget()
profit_recmommandation = Button(frame_for_farmers_btns_working,text='Profit Recommendation',command=profit_recmommandation_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10,image=final_pr_img,compound='right')
profit_recmommandation.pack_forget()
govt_schems_for_farmers = Button(frame_for_farmers_btns_working,text='Goverment Schemes For Farmers',command=govt_schems_for_farmers_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10,image=final_gs_img,compound='right')
govt_schems_for_farmers.pack_forget()
feedback_farmer_btn = Button(frame_for_farmers_btns_working,text='Feedback/Help',command=feedback_farmer_btn_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10,image=final_feedback_img,compound='right')
feedback_farmer_btn.pack_forget()
back_to_main_page_btn_for_farmers = Button(frame_for_farmers_btns_working,text='Home',command=back_to_main_page_btn_for_farmers_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10,image=final_img_for_home_btn,compound='right')
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
actual_message_of_user = Text(frame2_of_feedback,height=8,width=40,font=('cambria',15,'bold'),borderwidth=10)
actual_message_of_user.pack_forget()
feedback_submit_btn = Button(root,text='Submit Feedback',command=feedback_submit_btn_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10,image=final_submit_feedback_img,compound='right')
feedback_submit_btn.pack_forget()
explnation_label_for_all_farmers_btn_working = Label(root,text='Dynamic Text For Each Button Of Farmers Section',font=('cambria',15,'bold'),bg='Pink')
explnation_label_for_all_farmers_btn_working.pack_forget()
#Stactic widgets for profit recommandation button :-
frame_for_profit_recommandation_btn = Frame(root,bg='Pink')
frame_for_profit_recommandation_btn.pack_forget()
frame1_of_profit_recmommandation_btn = Frame(frame_for_profit_recommandation_btn,bg='Pink')
frame1_of_profit_recmommandation_btn.pack_forget()
frame2_of_profit_recmommandation_btn = Frame(frame_for_profit_recommandation_btn,bg='Pink')
frame2_of_profit_recmommandation_btn.pack_forget()
label_for_farmer_name = Label(frame1_of_profit_recmommandation_btn,text='Enter your name :- ',font=('cambria',15,'bold'),bg='Pink')
label_for_farmer_name.pack_forget()
farmer_name_keeper = StringVar()
entry_for_farmer_name = Entry(frame2_of_profit_recmommandation_btn,textvariable=farmer_name_keeper,font=('cambria',15,'bold'))
entry_for_farmer_name.pack_forget()
land_input_label = Label(frame1_of_profit_recmommandation_btn,text='How Much Land(In Guntha Only) You Are Using For Farming ?',font=('cambria',15,'bold'),bg='Pink')
land_input_label.pack_forget()
land_value_keeper = StringVar()
entry_for_land_input = Entry(frame2_of_profit_recmommandation_btn,font=('cambria',15,'bold'),textvariable=land_value_keeper)
entry_for_land_input.pack_forget()
label_for_type_of_tool = Label(frame1_of_profit_recmommandation_btn,text='Please Select Type Of Agriculture Tools That You Are Using For Farming :- ',font=('cambria',15,'bold'),bg='Pink')
label_for_type_of_tool.pack_forget()
all_agriculture_tool_type = ['Modern','Traditional','Hybrid']
agriculture_tool_type_keeper = StringVar()
agriculture_tool_type_keeper.set('Options')
input_for_agriculture_type_tool = OptionMenu(frame2_of_profit_recmommandation_btn,agriculture_tool_type_keeper,*all_agriculture_tool_type)
input_for_agriculture_type_tool.config(font=('cambria',15,'bold'))
input_for_agriculture_type_tool.pack_forget()
label_for_irrigation_method = Label(frame1_of_profit_recmommandation_btn,text='Please Select Irrigation Method That You Are Using For Farming',font=('cambria',15,'bold'),bg='Pink')
label_for_irrigation_method.pack_forget()
all_irrigation_methods = ['Drip','Sprinkler']
irrigation_method_holder = StringVar()
irrigation_method_holder.set('Options')
input_for_irrigation_method = OptionMenu(frame2_of_profit_recmommandation_btn,irrigation_method_holder,*all_irrigation_methods)
input_for_irrigation_method.config(font=('cambria',15,'bold'))
input_for_irrigation_method.pack_forget()
label_for_fertilizer_use = Label(frame1_of_profit_recmommandation_btn,text='How Much Fertilizer(in kg) You Use For Farming ?',font=('cambria',15,'bold'),bg='Pink')
label_for_fertilizer_use.pack_forget()
fetilizer_use_keeper = StringVar()
entry_forfertilizer_use = Entry(frame2_of_profit_recmommandation_btn,font=('cambria',15,'bold'),textvariable=fetilizer_use_keeper)
entry_forfertilizer_use.pack_forget()

label_for_pesticide_use = Label(frame1_of_profit_recmommandation_btn,text='How much Pesticides(in liters) you use for farming ?',font=('cambria',15,'bold'),bg='Pink')
label_for_pesticide_use.pack_forget()
pesticide_use_keeper = StringVar()
entry_for_pesticide_use = Entry(frame2_of_profit_recmommandation_btn,font=('cambria',15,'bold'),textvariable=pesticide_use_keeper)
entry_for_pesticide_use.pack_forget()

label_for_profit_2021 = Label(frame1_of_profit_recmommandation_btn,text='Please Enter Your Profit Of Year 2021',font=('cambria',15,'bold'),bg='Pink')
label_for_profit_2021.pack_forget()
profit_2021_keeper = StringVar()
entry_for_profit_2021 = Entry(frame2_of_profit_recmommandation_btn,font=('cambria',15,'bold'),textvariable=profit_2021_keeper)
entry_for_profit_2021.pack_forget()

label_for_profit_2022 = Label(frame1_of_profit_recmommandation_btn,text='Please Enter Your Profit Of Year 2022',font=('cambria',15,'bold'),bg='Pink')
label_for_profit_2022.pack_forget()
profit_2022_keeper = StringVar()
entry_for_profit_2022 = Entry(frame2_of_profit_recmommandation_btn,font=('cambria',15,'bold'),textvariable=profit_2022_keeper)
entry_for_profit_2022.pack_forget()

label_for_profit_2023 = Label(frame1_of_profit_recmommandation_btn,text='Please Enter Your Profit Of Year 2023',font=('cambria',15,'bold'),bg='Pink')
label_for_profit_2023.pack_forget()
profit_2023_keeper = StringVar()
entry_for_profit_2023 = Entry(frame2_of_profit_recmommandation_btn,font=('cambria',15,'bold'),textvariable=profit_2023_keeper)
entry_for_profit_2023.pack_forget()
govt_policy_label = Label(frame1_of_profit_recmommandation_btn,text='Have You Aware About All Goverment Policies Made For Farmers --> ?',font=('cambria',15,'bold'),bg='Pink')
govt_policy_label.pack_forget()
policy_awareness_answer_keeper = StringVar()
policy_awareness_answer_keeper.set('Options')
yes_no_for_policy_awareness = ['Yes','No']
input_for_policy_awareness = OptionMenu(frame2_of_profit_recmommandation_btn,policy_awareness_answer_keeper,*yes_no_for_policy_awareness)
input_for_policy_awareness.config(font=('cambria',15,'bold'))
input_for_policy_awareness.pack_forget()
proceed_for_profit_recommandation_btn = Button(root,text='Proceed For Anlysis',command=proceed_for_profit_recommandation_btn_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10,image=final_proceed_img,compound='right')
proceed_for_profit_recommandation_btn.pack_forget()
final_recommndation_frame = Frame(root,bg='Pink')
final_recommndation_frame.pack_forget()
welcome_label_for_farmer =Label(final_recommndation_frame,bg='Pink',font=('cambria',15,'bold'))
welcome_label_for_farmer.pack_forget()
#final frame for final out
final_frame = Frame(root,bg='Pink')
final_frame.pack_forget()
tool_explanation_label = Label(final_frame,text='Dynamic Text According To Methods ',bg='Pink',font=('cambria',15,'bold'))
tool_explanation_label.pack_forget()
irrigation_explanation_label = Label(final_frame,text='Dynamic Text According To irrigation Methods ',bg='Pink',font=('cambria',15,'bold'))
irrigation_explanation_label.pack_forget()
fertilizer_expalnation_label = Label(final_frame,text='it depends on user input',bg='Pink',font=('cambria',15,'bold'))
fertilizer_expalnation_label.pack_forget()
pesticide_explanation_label = Label(final_frame,text='it depends upon the user inputs ',bg='Pink',font=('cambria',15,'bold'))
pesticide_explanation_label.pack_forget()
profit_explanation_label = Label(final_frame,text='ACcording to conditions ',bg='Pink',font=('cambria',15,'bold'))
profit_explanation_label.pack_forget()
govt_polcies_explanation_label = Label(final_frame,text='it depends on the users response ',bg='Pink',font=('cambria',15,'bold'))
govt_polcies_explanation_label.pack_forget()
label_for_volume_btn = Label(final_frame,text='Audio Features Are Availabel here ',bg='tomato',font=('cambria',15,'bold'),image=final_proceed_img,compound='right')
label_for_volume_btn.pack_forget()
volume_btn = Button(final_frame,text='Audio',command=volume_btn_working,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10,image=final_audio_img,compound='right')
volume_btn.pack_forget()
pause_btn_for_recommendation = Button(final_frame,text='Pause',command=pause_btn_working,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10,image=final_pause_img,compound='right')
pause_btn_for_recommendation.pack_forget()
resume_btn_for_recommendation = Button(final_frame,text='Resume',command=resume_btn_working,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10,image=final_play_img,compound='right')
resume_btn_for_recommendation.pack_forget()
stop_btn_for_recommendation = Button(final_frame,text='Stop',command=stop_btn_working,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10,image=final_stop_img,compound='right')
stop_btn_for_recommendation.pack_forget()
#top level window for exit & static widgets for that panned window 
def yes_btn_for_exit_working():
    root.destroy()
    try:
        exit_yes_no_window.destroy()
    except TclError:
        pass
def no_btn_for_exit_working():
    exit_yes_no_window.destroy()
window_for_secondary_data_analysis_btn = None
weather_df = pd.read_csv(r"c:\Users\PANDURANG\Downloads\weather.csv")
fertilizer_df = pd.read_csv(r"c:\Users\PANDURANG\Downloads\Fertilizer Prediction.csv")
# Function to plot temperature analysis
def plot_temperature():
    dynamic_label_for_explanation_of_secondary_data_analysis.config(text='Temperature plays a critical role in agriculture, affecting crop growth, water requirements, and overall productivity. \
\nThis graph tracks the minimum and maximum temperatures over time, providing insights into temperature variations that can impact farming decisions.')
    dynamic_label_for_explanation_of_secondary_data_analysis.pack()
    plt.figure(figsize=(8, 5))
    plt.plot(weather_df.index, weather_df["MinTemp"], label="Min Temp", marker="o", linestyle="-")
    plt.plot(weather_df.index, weather_df["MaxTemp"], label="Max Temp", marker="o", linestyle="-")
    plt.xlabel("Index")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Analysis Over Time")
    plt.legend()
    plt.grid()
    plt.show()

# Function to plot rainfall analysis
def plot_rainfall():
    dynamic_label_for_explanation_of_secondary_data_analysis.config(text="Rainfall is a primary source of water for crops, and its distribution affects irrigation planning, soil moisture levels, and overall crop health. \
\nThis histogram visualizes how frequently different levels of rainfall occur in a specific region.")
    dynamic_label_for_explanation_of_secondary_data_analysis.pack()
    plt.figure(figsize=(8, 5))
    plt.hist(weather_df["Rainfall"], bins=10, color="blue", edgecolor="black", alpha=0.7)
    plt.xlabel("Rainfall (mm)")
    plt.ylabel("Frequency")
    plt.title("Rainfall Distribution")
    plt.grid()
    plt.show()

# Function to plot humidity analysis
def plot_humidity():
    dynamic_label_for_explanation_of_secondary_data_analysis.config(text="Humidity affects evaporation rates, plant transpiration, and disease occurrence in crops.\
 \nThis graph compares humidity levels at two key times of the day: 9 AM (morning) and 3 PM (afternoon).")
    dynamic_label_for_explanation_of_secondary_data_analysis.pack()
    plt.figure(figsize=(8, 5))
    plt.plot(weather_df.index, weather_df["Humidity9am"], label="Humidity at 9AM", marker="o")
    plt.plot(weather_df.index, weather_df["Humidity3pm"], label="Humidity at 3PM", marker="o")
    plt.xlabel("Index")
    plt.ylabel("Humidity (%)")
    plt.title("Humidity Analysis Over Time")
    plt.legend()
    plt.grid()
    plt.show()

# Function to plot soil type distribution
def plot_soil_type():
    dynamic_label_for_explanation_of_secondary_data_analysis.config(text="Different crops grow best in specific soil types, so understanding soil distribution helps in crop selection and fertilizer application.\
\nThis graph shows the distribution of soil types in the surveyed area.")
    dynamic_label_for_explanation_of_secondary_data_analysis.pack()
    plt.figure(figsize=(8, 5))
    soil_counts = fertilizer_df["Soil Type"].value_counts()
    soil_counts.plot(kind="bar", color="brown", alpha=0.7)
    plt.xlabel("Soil Type")
    plt.ylabel("Count")
    plt.title("Soil Type Distribution")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

# Function to plot crop type distribution
def plot_crop_type():
    dynamic_label_for_explanation_of_secondary_data_analysis.config(text="This graph helps identify which crops are grown most frequently, assisting in market planning, government subsidies, and agricultural policy-making.")
    dynamic_label_for_explanation_of_secondary_data_analysis.pack()
    plt.figure(figsize=(8, 5))
    crop_counts = fertilizer_df["Crop Type"].value_counts()
    crop_counts.plot(kind="bar", color="green", alpha=0.7)
    plt.xlabel("Crop Type")
    plt.ylabel("Count")
    plt.title("Crop Type Distribution")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

# Function to plot fertilizer recommendation
def plot_fertilizer():
    dynamic_label_for_explanation_of_secondary_data_analysis.config(text="Fertilizers are crucial for enhancing soil fertility and boosting crop yields. \nThis graph helps farmers choose the most suitable fertilizer based on soil conditions.")
    dynamic_label_for_explanation_of_secondary_data_analysis.pack()
    plt.figure(figsize=(8, 5))
    fert_counts = fertilizer_df["Fertilizer Name"].value_counts()
    fert_counts.plot(kind="bar", color="purple", alpha=0.7)
    plt.xlabel("Fertilizer")
    plt.ylabel("Count")
    plt.title("Fertilizer Recommendations Distribution")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()
def secondary_data_analysis_btn_func():
    global window_for_secondary_data_analysis_btn
    global dynamic_label_for_explanation_of_secondary_data_analysis
    if window_for_secondary_data_analysis_btn and window_for_secondary_data_analysis_btn.winfo_exists():
        messagebox.showerror('Attention Here','Secondary Data Analysis Button Window Is Already Open')
    else:
        window_for_secondary_data_analysis_btn = Toplevel()
        window_for_secondary_data_analysis_btn.title('Exit ?')
        window_for_secondary_data_analysis_btn.geometry('1000x500+250+175')
        window_for_secondary_data_analysis_btn.config(bg='Light Green')
        btn_temp = Button(window_for_secondary_data_analysis_btn, text="Temperature Analysis", command=plot_temperature,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
        btn_rain = Button(window_for_secondary_data_analysis_btn, text="Rainfall Analysis", command=plot_rainfall,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
        btn_humidity = Button(window_for_secondary_data_analysis_btn, text="Humidity Analysis", command=plot_humidity,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
        btn_soil = Button(window_for_secondary_data_analysis_btn, text="Soil Type Distribution", command=plot_soil_type,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
        btn_crop = Button(window_for_secondary_data_analysis_btn, text="Crop Type Distribution", command=plot_crop_type,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
        btn_fertilizer = Button(window_for_secondary_data_analysis_btn, text="Fertilizer Recommendation", command=plot_fertilizer,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
        # Place buttons on the window
        btn_temp.pack(pady=5)
        btn_rain.pack(pady=5)
        btn_humidity.pack(pady=5)
        btn_soil.pack(pady=5)
        btn_crop.pack(pady=5)
        btn_fertilizer.pack(pady=5)
        dynamic_label_for_explanation_of_secondary_data_analysis = Label(window_for_secondary_data_analysis_btn,text='Welcome To Secondary Data Analysis Report ',font=('cambria',14,'bold'),bg='Light Green')
        dynamic_label_for_explanation_of_secondary_data_analysis.pack(padx=10,pady=10)
secondary_data_analysis_btn = Button(root,text='Secondary Data Analysis',command=secondary_data_analysis_btn_func,font=('cambria',15,'bold'),activebackground='tomato',borderwidth=10)
root.mainloop()
