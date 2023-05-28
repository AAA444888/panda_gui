import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd

def add():
    def new(dict):
        df = pd.read_excel('data.xlsx') 
        mask=((df['name'] ==dict["name"])&(df['id'] ==dict["id"]))
        selected=mask
        print(df[selected==1])
        df= df[selected==1].to_dict('records')
        f=True
        for people in df:
            if people['name']==dict["name"] and people['id']==dict["id"]:
                f=False
        if f==True:
            df = pd.read_excel('data.xlsx') 
            questions = ['name','id','gender','height','weight','age']
            df2 = pd.DataFrame([dict],columns=questions)
            df= pd.concat([df2,df],ignore_index=True)
            df.to_excel('data.xlsx', index=False)
            messagebox.showinfo('訊息','新增成功')
        else:
            messagebox.showinfo('訊息','資料重複')
    def close():
        wnd.destroy()
    def submit():
        t1 = name_text.get()
        t2 = id_text.get()
        t3 = onthchoosen.get()
        t4 = height_text.get()
        t5 = weight_text.get()
        t6 = age_text.get()
        if t3=="男生":
            t3='1'
        else:
            t3='2'
        if t1!="" and t2!="" and t3!="" and t4!="" and t5!="" and t6!="":
            new({"name":t1,"id":t2,"gender":t3,"height":t4,"weight":t5,"age":t6})
            close()

    wnd = tk.Tk()
    wnd.geometry("400x400")
    wnd.title("Add Data")
    
    namet = tk.Label(wnd,text='請輸入名字:')
    namet.place(relx=0.3,rely=0.1,anchor='n')
    name_text = tk.Entry(wnd)
    name_text.place(relx=0.7,rely=0.1,anchor='n')

    idt = tk.Label(wnd,text='請輸入身分證字號:')
    idt.place(relx=0.3,rely=0.2,anchor='n')
    id_text = tk.Entry(wnd)
    id_text.place(relx=0.7,rely=0.2,anchor='n')

    sext = tk.Label(wnd,text='請選擇性別:')
    sext.place(relx=0.3,rely=0.3,anchor='n')
    n = tk.StringVar()
    onthchoosen = ttk.Combobox(wnd, width = 17, textvariable = n)
    onthchoosen['values'] = ('男生', '女生')
    onthchoosen.place(relx=0.7,rely=0.3,anchor='n')

    heightt = tk.Label(wnd,text='請輸入身高(單位: 公分):')
    heightt.place(relx=0.3,rely=0.4,anchor='n')
    height_text = tk.Entry(wnd)
    height_text.place(relx=0.7,rely=0.4,anchor='n')

    weightt = tk.Label(wnd,text='請輸入體重(單位: 公斤):')
    weightt.place(relx=0.3,rely=0.5,anchor='n')
    weight_text = tk.Entry(wnd)
    weight_text.place(relx=0.7,rely=0.5,anchor='n')
    
    aget = tk.Label(wnd,text='請輸入年齡:')
    aget.place(relx=0.3,rely=0.6,anchor='n')
    age_text = tk.Entry(wnd)
    age_text.place(relx=0.7,rely=0.6,anchor='n')

    button = tk.Button(wnd,text="submit",underline=-1,command=submit)
    button.place(relx=0.4,rely=0.7,anchor='n')
    button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
    button.place(relx=0.6,rely=0.7,anchor='n')
    
    wnd.mainloop()
    
if __name__=='__main__':
    add()