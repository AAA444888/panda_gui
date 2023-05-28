import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import bmi
import bmr
import ideal

def query():
    def gen(gender):
        if gender == '1':
            return "男生"
        else:
            return "女生"
    def submit():
        name = name_text.get()
        id = id_text.get()
        df = pd.read_excel('data.xlsx') 
        mask=((df['name'] ==name)&(df['id'] ==id))
        selected=mask
        print(df[selected==1])
        df= df[selected==1].to_dict('records')
        f=True
        for people in df:
            if people['name']==name and people['id']==id:
                f=False
                height=people['height']
                weight=people['weight']
                gender=people['gender']
                age=people['age']
                BMI=bmi.calculate(height,weight)
                bmitype=bmi.category(BMI)
                idealweight=ideal.weight(height,BMI)
                BMR=bmr.count(age,gender,BMI)
                bmrtype=bmr.category(gender,BMR)
                contacts = []
                columns = ("name","id", "gender",'height','weight','age','bmi','bmitype','idealweight','bmr','bmr_type')
                headers =("name","id", "gender",'height','weight','age','bmi','bmitype','idealweight','bmr','bmr_type')
                widthes = (80,80,80,80,80,80,80,80,90,80,80)
                tv = ttk.Treeview(wnd, show="headings",height=2 ,columns=columns)
                for (column, header, width) in zip(columns, headers, widthes):
                    tv.column(column, width=width, anchor="w")
                    tv.heading(column, text=header, anchor="w")
                def inser_data():
                    """插入数据"""
                    contacts.append(tuple([name,id,gen(gender),height,weight,age,BMI,bmitype,idealweight,BMR,bmrtype]))
                    for i, v in enumerate(contacts):
                        print(i,v)
                        tv.insert('', i,values=v)
                tv.place(relx=0.5,rely=0.35,anchor= 'n')
                inser_data()
                
        if f==True:
            messagebox.showinfo('訊息','查無此人')
        
    wnd = tk.Tk()
    wnd.geometry("900x400")
    wnd.title("Query Data")
    
    namet = tk.Label(wnd,text='請輸入名字:')
    namet.place(relx=0.3,rely=0.1,anchor='n')
    name_text = tk.Entry(wnd)
    name_text.place(relx=0.7,rely=0.1,anchor='n')

    idt = tk.Label(wnd,text='請輸入身分證字號:')
    idt.place(relx=0.3,rely=0.2,anchor='n')
    id_text = tk.Entry(wnd)
    id_text.place(relx=0.7,rely=0.2,anchor='n')

    button = tk.Button(wnd,text="submit",underline=-1,command=submit)
    button.place(relx=0.4,rely=0.7,anchor='n')            
    button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
    button.place(relx=0.6,rely=0.7,anchor='n')

    wnd.mainloop()
    
if __name__=='__main__':
    query()