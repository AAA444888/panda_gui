import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd

def delete():
    def submit():
        name = name_text.get()
        id = id_text.get()
        df = pd.read_excel('data.xlsx') 
        mask=((df['name'] ==name)&(df['id'] ==id))
        selected=mask
        df= df[selected==1].to_dict('records')
        flag=True
        for people in df:
            if people['name']==name and people['id']==id:
                flag=False
        if flag==False:
            df = pd.read_excel('data.xlsx') 
            df = df.drop(df[mask].index)
            df.to_excel('data.xlsx',index=False)
            messagebox.showinfo('訊息','已刪除檔案')
            wnd.destroy()
        else:
            messagebox.showinfo('訊息','刪除失敗')
        
    wnd = tk.Tk()
    wnd.geometry("400x400")
    wnd.title("Delete Data")
    
    namet = tk.Label(wnd,text='請輸入欲刪除的名字:')
    namet.place(relx=0.3,rely=0.1,anchor='n')
    name_text = tk.Entry(wnd)
    name_text.place(relx=0.7,rely=0.1,anchor='n')

    idt = tk.Label(wnd,text='請輸入欲刪除的身分證字號:')
    idt.place(relx=0.3,rely=0.2,anchor='n')
    id_text = tk.Entry(wnd)
    id_text.place(relx=0.7,rely=0.2,anchor='n')

    button = tk.Button(wnd,text="submit",underline=-1,command=submit)
    button.place(relx=0.3,rely=0.7,anchor='n')            
    button = tk.Button(wnd,text="close",underline=-1,command=wnd.destroy)
    button.place(relx=0.7,rely=0.7,anchor='n')
    
    wnd.mainloop()
    
if __name__=='__main__':
    delete()