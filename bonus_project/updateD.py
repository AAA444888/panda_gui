import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd

def update():
    def submit():
        def up():
            df = pd.read_excel('data.xlsx') 
            gender = onthchoosen.get()
            height = height_text.get()
            weight = weight_text.get()
            age = age_text.get()
            if gender=="男生":
                gender='1'
            else:
                gender='2'
            dict={"name":name,"id":id,"gender":gender,"height":height,"weight":weight,"age":age}
            for k,v in dict.items():
                df.loc[df['name'] ==dict['name'], k] = v
            df.to_excel('data.xlsx',index=False)
            messagebox.showinfo('訊息','更新完畢')
            wnd.destroy()
            
        name = name_text.get()
        id = id_text.get()
        df = pd.read_excel('data.xlsx') 
        mask=((df['name'] ==name)&(df['id'] ==id))
        selected=mask
        print(df[selected==1])
        df= df[selected==1].to_dict('records')
        flag=True
        for people in df:
            if people['name']==name and people['id']==id:
                flag=False
                sext = tk.Label(wnd,text='請選擇欲更新的性別:')
                sext.place(relx=0.3,rely=0.3,anchor='n')
                n = tk.StringVar()
                onthchoosen = ttk.Combobox(wnd, width = 17, textvariable = n)
                onthchoosen['values'] = ('男生', '女生')
                onthchoosen.place(relx=0.7,rely=0.3,anchor='n')

                heightt = tk.Label(wnd,text='請輸入欲更新的身高(單位: 公分):')
                heightt.place(relx=0.3,rely=0.4,anchor='n')
                height_text = tk.Entry(wnd)
                height_text.place(relx=0.7,rely=0.4,anchor='n')

                weightt = tk.Label(wnd,text='請輸入欲更新的體重(單位: 公斤):')
                weightt.place(relx=0.3,rely=0.5,anchor='n')
                weight_text = tk.Entry(wnd)
                weight_text.place(relx=0.7,rely=0.5,anchor='n')
                
                aget = tk.Label(wnd,text='請輸入欲更新的年齡:')
                aget.place(relx=0.3,rely=0.6,anchor='n')
                age_text = tk.Entry(wnd)
                age_text.place(relx=0.7,rely=0.6,anchor='n')
                
                button = tk.Button(wnd,text="update",underline=-1,command=up)
                button.place(relx=0.5,rely=0.7,anchor='n') 
        if flag==True:
            messagebox.showinfo('訊息','查無此人')
        
    wnd = tk.Tk()
    wnd.geometry("400x400")
    wnd.title("Update Data")
    
    namet = tk.Label(wnd,text='請輸入欲更新的名字:')
    namet.place(relx=0.3,rely=0.1,anchor='n')
    name_text = tk.Entry(wnd)
    name_text.place(relx=0.7,rely=0.1,anchor='n')

    idt = tk.Label(wnd,text='請輸入欲更新的身分證字號:')
    idt.place(relx=0.3,rely=0.2,anchor='n')
    id_text = tk.Entry(wnd)
    id_text.place(relx=0.7,rely=0.2,anchor='n')

    button = tk.Button(wnd,text="submit",underline=-1,command=submit)
    button.place(relx=0.3,rely=0.7,anchor='n')            
    button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
    button.place(relx=0.7,rely=0.7,anchor='n')
    
    wnd.mainloop()
    
if __name__=='__main__':
    update()