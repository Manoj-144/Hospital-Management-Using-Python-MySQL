from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import pickle
import mysql.connector
from tkinter import ttk
import datetime


def hospital_management():
    global h
    h=Tk()
    ww=1150
    wh=600
    sw=h.winfo_screenwidth()
    sh=h.winfo_screenheight()
    h.geometry("%dx%d" % (sw, sh))
    h.title('MNM HOSPITAL')
    
    #bg image
    bgimg=Image.open("c:/Users/doodle 1.jpg")
    bgimgresize=bgimg.resize((sw,sh))
    bgimg2=ImageTk.PhotoImage(bgimgresize)
    bgimglabel=Label(image=bgimg2,border=0,justify=CENTER).pack()

    #frame
    Frame(h,width=1050,height=550,bg='white').place(x=250,y=100)

    #logo1 image
    limg=Image.open("c:/Users/DAV.jpg")
    limgresize=limg.resize((140,170))
    limg2=ImageTk.PhotoImage(limgresize)
    limglabel=Label(image=limg2,border=0,justify=CENTER)
    limglabel.place(x=350,y=300)

    #logo2 image
    l1img=Image.open("c:/Users/logo.png")
    l1imgresize=l1img.resize((350,350))
    l1img2=ImageTk.PhotoImage(l1imgresize)
    l1imglabel=Label(image=l1img2,border=0,justify=CENTER)
    l1imglabel.place(x=950,y=200)

    #title
    titlelbl=Label(h,text="HOSPITAL MANAGEMENT",bg="white",fg="firebrick3",font=("consolas",50,"bold"))
    titlelbl.place(x=425,y=125)

    #done by
    donelbl=Label(h,text="DONE BY :\n\n   Madhusudhanan.K\n   Nitin.S\n   Manoj.R",bg="white",fg="black",font=("consolas",30))
    donelbl.place(x=540,y=250)

    def hospital():
        h.destroy()
        w=Tk()
        ww=1150
        wh=600
        sw=w.winfo_screenwidth()
        sh=w.winfo_screenheight()
        w.geometry("%dx%d" % (sw, sh))
        w.title('L O G I N')

        #bg image
        bgimg=Image.open("c:/Users/doodle.jpg")
        bgimgresize=bgimg.resize((sw,sh))
        bgimg2=ImageTk.PhotoImage(bgimgresize)
        bgimglabel=Label(image=bgimg2,border=0,justify=CENTER).pack()

        Frame(w,width=850,height=500,bg='white').place(x=350,y=150)

        #title
        titlelbl=Label(w,text="MNM HOSPITAL",bg="white",fg="firebrick3",font=("consolas",50,"bold"))
        titlelbl.place(x=550,y=170)
        
        #label 1
        al1=Label(w,text='Email: ',bg='white')
        al=('consolas',15)
        al1.config(font=al)
        al1.place(x=580,y=310)

        ae1=Entry(w,width=15,border=5)
        ae1.config(font=al)
        ae1.place(x=720,y=310)

        #label 2
        al2=Label(w,text='Password: ',bg='white')
        al=('consolas',15)
        al2.config(font=al)
        al2.place(x=580,y=390)

        ae2=Entry(w,width=15,border=5,show='*')
        ae2.config(font=al)
        ae2.place(x=720,y=390)    

        def login():
            flag=False
            if ae1.get()=="" or ae2.get()=="":
                messagebox.showerror("Error","all fields are required ")
            elif True:
                l,l2=reading()
                for i in l :
                    try:
                        if i['email']==ae1.get() and i['password']==ae2.get():
                            flag=True
                            w.destroy()
                            admin()
                    except:
                        pass
                if not flag:
                    messagebox.showerror("Invalid","Invalid username or password ")
                    ae1.delete(0, END)
                    ae2.delete(0, END)
                    
        Button(w,width=20,height=2,fg='white',bg='#994422',border=0,command=login,text="L O G I N").place(x=680,y=480)

        Button(w,width=30,height=2,fg='black',font=("consolas",10,"bold"),bg='goldenrod1',command=register,border=2,text="R E G I S T E R").place(x=645,y=550)

        w.mainloop()
        

    Button(h,width=20,height=2,fg='black',bg='cyan',command=hospital,border=2,text="C O N T I N U E").place(x=685,y=575)
    
    h.mainloop()

def register_user():
    el=[]
    cl=[]
    if e1.get()=="" or e2.get()=="" or e3.get()=="":
        messagebox.showerror("Error","All fields are required")
        r.destroy()

    else:
        try:
            f2=open("Register_details.txt","rb")
            while True:
                try:
                    d=pickle.load(f2)
                    el.append(d['email'])
                    cl.append(d['password'])
                except:
                    break
            f2.close()
        except:
            pass
        
        if e2.get() in  el :
               messagebox.showerror("Error","Already a user ( Email exist ) ")
               r.destroy()
        else:
              f=open("Register_details.txt","ab")
              messagebox.showinfo("Success","Registration Successful")
              d={}
              d["name"]=e1.get()
              d["email"]=e2.get()
              d["password"]=e3.get()
              pickle.dump(d,f)
              f.close()
              e1.delete(0, END)
              e2.delete(0, END)
              e3.delete(0, END)
              r.destroy()
              
    r.mainloop()

def reading():
     f=open("Register_details.txt","rb")
     l,l2=[],[]
     while True:
          try:
               d1={}
               d=pickle.load(f)
               l2.append(d)
               d1['email']=d['email']
               d1['password']=d['password']
               l.append(d1)
          except:
               break
     return l,l2
     f.close()

def register():
    global e1
    global e2
    global e3
    global r
    r=Tk()
    ww=370
    wh=550
    sw=r.winfo_screenwidth()
    sh=r.winfo_screenheight()
    x=(sw/2)-(ww/2)
    y=(sh/2)-(wh/2)
    r.geometry(f'{ww}x{wh}+{int(x)}+{int(y)}')
    r.title('R E G I S T E R')
    r.resizable(0,0)
    
    #Frame
    Frame(r,width=850,height=500,bg='white').place(x=0,y=0)

    #Text
    titlelbl=Label(r,text="MNM HOSPITAL\nREGISTRATION",bg="white",fg="red",font=("consolas",30,"bold"))
    titlelbl.place(x=50,y=20)
    
    #label 1
    l1=Label(r,text='Username',bg='white')
    l=('consolas',15)
    l1.config(font=l)
    l1.place(x=60,y=130)

    e1=Entry(r,width=15,border=2)
    e1.config(font=l)
    e1.place(x=60,y=160)

    #label 2
    l2=Label(r,text='Email',bg='white')
    l=('consolas',15)
    l2.config(font=l)
    l2.place(x=60,y=210)

    e2=Entry(r,width=15,border=2)
    e2.config(font=l)
    e2.place(x=60,y=240)

    #label 3
    l3=Label(r,text='Password',bg='white')
    l=('consolas',15)
    l3.config(font=l)
    l3.place(x=60,y=290)

    e3=Entry(r,width=15,border=2,show='*')
    e3.config(font=l)
    e3.place(x=60,y=320)

    submit_button = Button(r,width=20,height=1,fg='black',font=("consolas",15,"bold"),bg='goldenrod1',command=register_user,border=2,text="S U B M I T").place(x=60,y=460)

def admin():
    w=Tk()
    ww=1150
    wh=600
    sw=w.winfo_screenwidth()
    sh=w.winfo_screenheight()
    w.geometry("%dx%d" % (sw, sh))
    w.title('H O S P I T A L  M A N A G E M E N T')
    
    #Frames
    Frame(w,width=sw,height=sh,bg='#c8d8e4').place(x=0,y=0)
    Frame(w,width=300,height=sh,bg='#2b6777').place(x=0,y=0)
    Frame(w,width=1400,height=50,bg='CadetBlue3').place(x=300,y=0)

    #Bg image
    hosbg1=Image.open("c:/Users/hosbg.jpeg")
    hosbgresize=hosbg1.resize((900,400))
    hosbg2=ImageTk.PhotoImage(hosbgresize)
    hosbglabel=Label(image=hosbg2,border=0,justify=CENTER)
    hosbglabel.place(x=470,y=350)

    #Admin logo
    adminpic1=Image.open("c:/Users/admin2.png")
    adminpicresize=adminpic1.resize((125,125))
    adminpic2=ImageTk.PhotoImage(adminpicresize)
    adminpiclabel=Label(image=adminpic2,border=0,justify=CENTER)
    adminpiclabel.place(x=80,y=70)
    
    #Logo
    l1img=Image.open("c:/Users/logo.png")
    l1imgresize=l1img.resize((200,200))
    l1img2=ImageTk.PhotoImage(l1imgresize)
    l1imglabel=Label(image=l1img2,border=0,justify=CENTER)
    l1imglabel.place(x=50,y=575)

    #Font
    titlelbl=Label(w,text='A D M I N',bg='#2b6777',fg="black",font=("consolas",20))
    titlelbl.place(x=70,y=220)

    titlelbl=Label(w,text='HOSPITAL MANAGEMENT',bg='CadetBlue3',fg="black",font=("consolas",20))
    titlelbl.place(x=310,y=6)

    titlelbl=Label(w,text='MNM HOSPITAL',bg='CadetBlue3',fg="black",font=("consolas",25))
    titlelbl.place(x=40,y=350)

    titlelbl=Label(w,text='email : mnmhospital@123.com\nphone : 9632147850\naddress : No:10 Broadway,\n\t5th Avenue,\nNew Jersey',bg='#2b6777',fg="black",font=("consolas",13))
    titlelbl.place(x=15,y=410)
    
    #Button image
    aord1=Image.open("c:/Users/aord.png")
    aordr=aord1.resize((380,155))
    aord2=ImageTk.PhotoImage(aordr)

    aorp1=Image.open("c:/Users/aorp.png")
    aorpr=aorp1.resize((380,155))
    aorp2=ImageTk.PhotoImage(aorpr)

    aora1=Image.open("c:/Users/aora.png")
    aorar=aora1.resize((380,155))
    aora2=ImageTk.PhotoImage(aorar)


    def exitt():
        res=messagebox.askquestion('Exit Application', 'Do you really want to exit')
        if res == 'yes':
            w.destroy()
        else:
            pass


    def aord():
        def addd():
            name=de1.get()
            age=de2.get()
            gender=de3.get()
            spec=de4
            email=de5.get()
            phone=de6.get()
            time=de7
            row=(name,age,gender,spec,email,phone,time)

            mc=mysql.connector.connect(host='localhost',user='root',passwd='manoj144',database='project')
            c=mc.cursor()

            c.execute("INSERT INTO DOC VALUES('{}','{}','{}','{}','{}','{}','{}');".format(name,age,gender,spec,email,phone,time))
            mc.commit()
            mc.close()
            dt.insert('',END, values=row)

            de1.delete(0, END)
            de2.delete(0, END)
            de3.delete(0, END)
            de5.delete(0, END)
            de6.delete(0, END)

        def delete():
            global selected_row
            selected_item = dt.selection()[0]
            dt.delete(selected_item)
            
            mc=mysql.connector.connect(host='localhost',user='root',passwd='manoj144',database='project')
            c=mc.cursor()
            c.execute("DELETE FROM DOC WHERE DNAME = '{}';".format(selected_row[0]))
            mc.commit()
            mc.close()

        def get_content(event=""):
            global selected_row
            cursor_row=dt.focus()
            content=dt.item(cursor_row)
            selected_row=content["values"]

        w=Tk()
        ww=1150
        wh=600
        sw=w.winfo_screenwidth()
        sh=w.winfo_screenheight()
        w.geometry("%dx%d" % (sw, sh))
        w.title('D O C T O R S')

        Frame(w,width=500,height=750,bg='#c8d8e4').place(x=20,y=20)
        Frame(w,width=950,height=750,bg='black').place(x=550,y=20)

        addlbl=Label(w,text='ADD OR DELETE',bg='#c8d8e4',fg="black",font=("consolas",20))
        addlbl.place(x=175,y=25)

        detlbl=Label(w,text='DOCTOR DETAILS',bg='black',fg="white",font=("consolas",20))
        detlbl.place(x=925,y=25)
                
        #label 1
        dl1=Label(w,text='Name: ',bg='#c8d8e4')
        dl=('consolas',15)
        dl1.config(font=dl)
        dl1.place(x=50,y=90)

        de1=Entry(w,width=15,border=5)
        de1.config(font=dl)
        de1.place(x=230,y=90)

        #label 2
        dl2=Label(w,text='Age: ',bg='#c8d8e4')
        dl=('consolas',15)
        dl2.config(font=dl)
        dl2.place(x=50,y=150)

        de2=Entry(w,width=15,border=5)
        de2.config(font=dl)
        de2.place(x=230,y=150)

        #Label 3
        dl3=Label(w,text='Gender: ',bg='#c8d8e4')
        dl=('consolas',15)
        dl3.config(font=dl)
        dl3.place(x=50,y=210)

        de3=Entry(w,width=15,border=5)
        de3.config(font=dl)
        de3.place(x=230,y=210)

        #Label 4
        dl4=Label(w,text='Specialization: ',bg='#c8d8e4')
        dl=('consolas',15)
        dl4.config(font=dl)
        dl4.place(x=50,y=270)

        #combo box
        var1 = StringVar(w)
        box1 = ttk.Combobox(w,width=17,height=10,textvariable=var1,font=("consolas",13))

        box1['values'] = ["Dentist","Cardiologist","Allergist","Neurologist","Psychiatrist","Pediatrician","Ophthalmologist","Orthopedic","Gynecologist","Nephrologist"]

        box1['state'] = 'readonly'

        box1.place(x=230,y=270)

        def ok1(event):
            global de4
            de4=str(var1.get())

        box1.bind('<<ComboboxSelected>>', ok1)

        box1.set(var1.get())

        #Label 5
        dl5=Label(w,text='Email: ',bg='#c8d8e4')
        dl=('consolas',15)
        dl5.config(font=dl)
        dl5.place(x=50,y=330)

        de5=Entry(w,width=15,border=5)
        de5.config(font=dl)
        de5.place(x=230,y=330)

        #Label 6
        dl6=Label(w,text='Phone no: ',bg='#c8d8e4')
        dl=('consolas',15)
        dl6.config(font=dl)
        dl6.place(x=50,y=390)

        de6=Entry(w,width=15,border=5)
        de6.config(font=dl)
        de6.place(x=230,y=390)
        
        #Label 7
        dl7=Label(w,text='Time slot: ',bg='#c8d8e4')
        dl=('consolas',15)
        dl7.config(font=dl)
        dl7.place(x=50,y=450)

        var = StringVar(w)
        box = ttk.Combobox(w,width=17,height=10,textvariable=var,font=("consolas",13))

        box['values'] = ["9:00 AM - 11:00 AM","11:00 AM - 01:00 PM","01:00 PM - 03:00 PM","03:00 PM - 05:00 PM","05:00 PM - 07:00 PM","07:00 PM - 09:00 PM","09:00 PM - 11:00 PM"]

        box['state'] = 'readonly'

        box.place(x=230,y=455)

        def ok(event):
            global de7
            de7=str(var.get())

        box.bind('<<ComboboxSelected>>', ok)

        box.set(var.get())
        
        #table
        details_table=Frame(w,bd=4,relief=RIDGE)
        details_table.place(x=550,y=20,width=950,height=750)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        header = ('name','age','gender','spec','email','phone','time')

        dt=ttk.Treeview(details_table,column=header,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=dt.xview)
        scroll_y.config(command=dt.yview)

        dt.heading('name', text='Name')
        dt.heading('age', text= 'Age')
        dt.heading('gender', text='Gender')
        dt.heading('spec', text='Specialization')
        dt.heading('email', text='Email')
        dt.heading('phone', text='Phone')
        dt.heading('time', text='Time Slot')

        dt["show"]="headings"

        dt.column('name',width=100,anchor=CENTER)
        dt.column("age",width=50,anchor=CENTER)
        dt.column("gender",width=50,anchor=CENTER)
        dt.column("spec",width=100,anchor=CENTER)
        dt.column("email",width=100,anchor=CENTER)
        dt.column("phone",width=75,anchor=CENTER)
        dt.column("time",width=100,anchor=CENTER)

        mc = mysql.connector.connect(host = 'localhost',user = 'root',passwd= 'manoj144', database = 'project')
        c = mc.cursor()
        l=[]
        c.execute("select * from doc;")
        t = c.fetchall()
        count=0
        for i in t:
            if count%2==0:
                dt.insert('',END, values=i, tags=('oddrow'))
            else:
                dt.insert('',END, values=i, tags=('evenrow'))
            count+=1

        mc.close()


        dt.pack(fill=BOTH,expand=1)
        dt.bind("<ButtonRelease-1>",get_content)

        dt.tag_configure('oddrow', background = "white")
        dt.tag_configure('evenrow', background = "lightblue")

        style = ttk.Style(w)
        style.theme_use("clam")
        style.configure(".",font=('Helvetica',11))
        style.configure('Treeview', rowheight=40)
        style.configure("Treeview.Heading",foreground='black',font=('Helvetica',11,"bold"))               
  
        Button(w,width=35,height=2,fg='white',bg='#2b6777',command=addd,text=" A D D ").place(x=150,y=550)
        Button(w,width=35,height=2,fg='white',bg='#2b6777',command=delete,text=" D E L E T E ").place(x=150,y=600)

        w.mainloop()

  

    def aorp():
        def addp():
            name=pe1.get()
            age=pe2.get()
            gender=pe3.get()
            phone=pe4.get()
            symptoms=pe5.get()
            dep=pe6
            doa=pe7.get()
            row=(name,age,gender,phone,symptoms,dep,doa)

            today = datetime.date.today()
            todayd = today.strftime('%Y-%m-%d')
            if doa<todayd:
                messagebox.showerror("Error","Date not correct!")
                return

            mc=mysql.connector.connect(host='localhost',user='root',passwd='manoj144',database='project')
            c=mc.cursor()
    
            c.execute("SELECT * FROM DOC WHERE SPECILIZATION = '{}'".format(dep))
            listdoc = c.fetchall()
            mc.close()
            
            mc=mysql.connector.connect(host='localhost',user='root',passwd='manoj144',database='project')
            c=mc.cursor()
            c.execute("SELECT * FROM APP WHERE SPECILIZATION = '{}'".format(dep))
            listapp = c.fetchall()
            mc.close()

            mc=mysql.connector.connect(host='localhost',user='root',passwd='manoj144',database='project')
            c=mc.cursor()
            
            for i in listdoc:
                idoccount = 0
                for j in listapp:
                    pppt = j[5]
                    pppa = pppt.strftime('%Y-%m-%d')
                    if i[0].lower() == j[0].lower() and pppa==doa :
                        idoccount +=1
                if idoccount<2:
                    c.execute("INSERT INTO PAT VALUES('{}','{}','{}','{}','{}','{}','{}');".format(name,age,gender,phone,symptoms,dep,doa))
                    mc.commit()
                    c.execute("INSERT INTO APP VALUES('{}','{}','{}','{}','{}','{}');".format(i[0],name,phone,dep,i[6],doa))
                    dt.insert('',END, values=row)
                    mc.commit()
                    break

            else:
                messagebox.showerror("Error","Doc is busy , select another date!!")
            mc.close()

            pe1.delete(0, END)
            pe2.delete(0, END)
            pe3.delete(0, END)
            pe4.delete(0, END)
            pe5.delete(0, END)
            pe7.delete(0, END)
            
        def delete():
            global selected_row
            selected_item = dt.selection()[0]
            dt.delete(selected_item)
            
            mc=mysql.connector.connect(host='localhost',user='root',passwd='manoj144',database='project')
            c=mc.cursor()
            c.execute("DELETE FROM PAT WHERE PNAME = '{}';".format(selected_row[0]))
            c.execute("DELETE FROM APP WHERE PNAME = '{}';".format(selected_row[0]))
            mc.commit()
            mc.close()

        def get_content(event=""):
            global selected_row
            cursor_row=dt.focus()
            content=dt.item(cursor_row)
            selected_row=content["values"]
            
        w=Tk()
        ww=1150
        wh=600
        sw=w.winfo_screenwidth()
        sh=w.winfo_screenheight()
        w.geometry("%dx%d" % (sw, sh))
        w.title(' P A T I E N T')

        Frame(w,width=500,height=750,bg='#c8d8e4').place(x=20,y=20)
        Frame(w,width=950,height=750,bg='black').place(x=550,y=20)

        addlbl=Label(w,text='ADD OR DELETE',bg='#c8d8e4',fg="black",font=("consolas",20))
        addlbl.place(x=175,y=25)

        detlbl=Label(w,text='PATIENT DETAILS',bg='black',fg="white",font=("consolas",20))
        detlbl.place(x=925,y=25)

        #label 1
        pl1=Label(w,text='Name: ',bg='#c8d8e4')
        pl=('consolas',15)
        pl1.config(font=pl)
        pl1.place(x=50,y=90)

        pe1=Entry(w,width=15,border=5)
        pe1.config(font=pl)
        pe1.place(x=230,y=90)

        #label 2
        pl2=Label(w,text='Age: ',bg='#c8d8e4')
        pl=('consolas',15)
        pl2.config(font=pl)
        pl2.place(x=50,y=150)

        pe2=Entry(w,width=15,border=5)
        pe2.config(font=pl)
        pe2.place(x=230,y=150)

        #Label 3
        pl3=Label(w,text='Gender: ',bg='#c8d8e4')
        pl=('consolas',15)
        pl3.config(font=pl)
        pl3.place(x=50,y=210)

        pe3=Entry(w,width=15,border=5)
        pe3.config(font=pl)
        pe3.place(x=230,y=210)

        #Label 4
        pl4=Label(w,text='Phone no: ',bg='#c8d8e4')
        pl=('consolas',15)
        pl4.config(font=pl)
        pl4.place(x=50,y=270)

        pe4=Entry(w,width=15,border=5)
        pe4.config(font=pl)
        pe4.place(x=230,y=270)

        #Label 5
        pl5=Label(w,text='Symptoms: ',bg='#c8d8e4')
        pl=('consolas',15)
        pl5.config(font=pl)
        pl5.place(x=50,y=330)

        pe5=Entry(w,width=15,border=5)
        pe5.config(font=pl)
        pe5.place(x=230,y=330)

        #Label 6
        pl6=Label(w,text='Department: ',bg='#c8d8e4')
        pl=('consolas',15)
        pl6.config(font=pl)
        pl6.place(x=50,y=390)

        var1 = StringVar(w)
        box1 = ttk.Combobox(w,width=17,height=10,textvariable=var1,font=("consolas",13))

        box1['values'] = ["Dentist","Cardiologist","Allergist","Neurologist","Psychiatrist","Pediatrician","Ophthalmologist","Orthopedic","Gynecologist","Nephrologist"]

        box1['state'] = 'readonly'

        box1.place(x=230,y=390)

        def ok1(event):
            global pe6
            pe6=str(var1.get())

        box1.bind('<<ComboboxSelected>>', ok1)

        box1.set(var1.get())

        #Label 7
        pl7=Label(w,text='DOA: ',bg='#c8d8e4')
        pl=('consolas',15)
        pl7.config(font=pl)
        pl7.place(x=50,y=450)

        pe7=Entry(w,width=15,border=5)
        pe7.config(font=pl)
        pe7.place(x=230,y=450)

        details_table=Frame(w,bd=4,relief=RIDGE)
        details_table.place(x=550,y=20,width=950,height=750)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        header = ('name','age','gender','phone','symptoms','department','doa')

        dt=ttk.Treeview(details_table,column=header,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=dt.xview)
        scroll_y.config(command=dt.yview)

        dt.heading('name', text='Name')
        dt.heading('age', text= 'Age')
        dt.heading('gender', text='Gender')
        dt.heading('phone', text='Phone no')
        dt.heading('symptoms', text='Symptoms')
        dt.heading('department', text='Department')
        dt.heading('doa', text='DOA')

        dt["show"]="headings"

        dt.column('name',width=100,anchor=CENTER)
        dt.column("age",width=50,anchor=CENTER)
        dt.column("gender",width=50,anchor=CENTER)
        dt.column("phone",width=100,anchor=CENTER)
        dt.column("symptoms",width=100,anchor=CENTER)
        dt.column("department",width=100,anchor=CENTER)
        dt.column("doa",width=100,anchor=CENTER)

        mc = mysql.connector.connect(host = 'localhost',user = 'root',passwd= 'manoj144', database = 'project')
        c = mc.cursor()
        l=[]
        c.execute("select * from pat;")
        t = c.fetchall()
        count=0
        for i in t:
            if count%2==0:
                dt.insert('',END, values=i, tags=('oddrow'))
            else:
                dt.insert('',END, values=i, tags=('evenrow'))
            count+=1

        mc.close()


        dt.pack(fill=BOTH,expand=1)
        dt.bind("<ButtonRelease-1>",get_content)

        dt.tag_configure('oddrow', background = "white")
        dt.tag_configure('evenrow', background = "lightblue")

        style = ttk.Style(w)
        style.theme_use("clam")
        style.configure(".",font=('Helvetica',11))
        style.configure('Treeview', rowheight=40)
        style.configure("Treeview.Heading",foreground='black',font=('Helvetica',11,"bold"))               

        Button(w,width=35,height=2,fg='white',bg='#2b6777',command=addp,text=" A D D ").place(x=150,y=550)
        Button(w,width=35,height=2,fg='white',bg='#2b6777',command=delete,text=" D E L E T E ").place(x=150,y=600)
        
        w.mainloop()



    def aora():
        w=Tk()
        ww=1150
        wh=600
        sw=w.winfo_screenwidth()
        sh=w.winfo_screenheight()
        w.geometry("%dx%d" % (sw, sh))
        w.title('A P P O I N T M E N T S')

        Frame(w,width=sw,height=sh,bg='black').place(x=0,y=0)

        detlbl=Label(w,text='APPOINTMENTS:',bg='black',fg="white",font=("consolas",20))
        detlbl.place(x=625,y=70)                

        details_table=Frame(w,bd=4,relief=RIDGE)
        details_table.place(x=250,y=125,width=1000,height=500)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        header = ('dname','pname','phone','categ','time','doa')

        dt=ttk.Treeview(details_table,column=header,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=dt.xview)
        scroll_y.config(command=dt.yview)

        dt.heading('dname', text='Doctor Name')
        dt.heading('pname', text='Patient Name')
        dt.heading('phone', text='Phone')
        dt.heading('categ', text='Category')
        dt.heading('time', text='Time slot')
        dt.heading('doa', text='DOA')
        

        dt["show"]="headings"

        dt.column('dname',width=150,anchor=CENTER)
        dt.column("pname",width=150,anchor=CENTER)
        dt.column('phone',width=150,anchor=CENTER)
        dt.column('categ',width=150,anchor=CENTER)
        dt.column('time',width=150,anchor=CENTER)
        dt.column('doa',width=150,anchor=CENTER)

        today = datetime.date.today()
        todayd = today.strftime('%Y-%m-%d')
        
        mc = mysql.connector.connect(host = 'localhost',user = 'root',passwd= 'manoj144', database = 'project')
        c = mc.cursor()
        c.execute("SELECT DNAME,PNAME,PHONE,SPECILIZATION,TIMESLOT,DOA FROM APP;")
        t = c.fetchall()
        count=0
        for i in range(len(t)):
            doanow = t[i][5].strftime('%Y-%m-%d')
            if doanow<todayd:
                c.execute('DELETE FROM APP WHERE DOA = "{}"'.format(doanow))
                mc.commit()
        mc.close()
        mc = mysql.connector.connect(host = 'localhost',user = 'root',passwd= 'manoj144', database = 'project')
        c = mc.cursor()
        c.execute("SELECT DNAME,PNAME,PHONE,SPECILIZATION,TIMESLOT,DOA FROM APP;")
        t = c.fetchall()
        for i in t:
            if count%2==0:
                dt.insert('',END, values=i, tags=('oddrow'))
            else:
                dt.insert('',END, values=i, tags=('evenrow'))
            count+=1

        mc.close()

        dt.pack(fill=BOTH,expand=1)

        dt.tag_configure('oddrow', background = "white")
        dt.tag_configure('evenrow', background = "lightblue")

        style = ttk.Style(w)
        style.theme_use("clam")
        style.configure(".",font=('Helvetica',11))
        style.configure('Treeview', rowheight=40)
        style.configure("Treeview.Heading",foreground='black',font=('Helvetica',11,"bold"))               

        w.mainloop()

    Button(w,width=10,height=2,fg='white',bg='#2b6777',command=exitt,text="E X I T").place(x=1425,y=5)
    Button(w,width=350,height=155,border=1,command=aord,image=aord2).place(x=335,y=125)
    Button(w,width=350,height=155,border=1,command=aorp,image=aorp2).place(x=735,y=125)
    Button(w,width=350,height=155,border=1,command=aora,image=aora2).place(x=1135,y=125)

    w.mainloop()

hospital_management()
