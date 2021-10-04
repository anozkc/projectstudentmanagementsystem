

def exportall():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id, name, mobile, email, address, gender, dob, addeddate, addedtime = [], [], [], [], [], [], [], [], []
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]), name.append(pp[1]), mobile.append(pp[2]), email.append(pp[3]), address.append(pp[4]),
        gender.append(pp[5]), dob.append(pp[6]), addeddate.append(pp[7]), addedtime.append(pp[8])
    dd = ['Id', 'Name', 'Mobile', 'Email', 'Address', 'Gender', 'D.O.B', 'Addeddate', 'Addedtime']
    df = pandas.DataFrame(list(zip( id, name, mobile, email, address, gender, dob, addeddate, addedtime)), columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths, index=False)
    messagebox.showinfo('Notifications', 'Student data is saved{}'.format(paths))



def exit():
    print('student exit')
    res = messagebox.askyesnocancel('Notification', 'Do you want to exit?')
    if(res == True):
        root.destroy()
        print(res)


######################################################## CONNECT TO DATABASE   ###########################
def connectdb():
    print('Welcome to database')

    def submitdb():
        print('submitted')
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()

        global con, mycursor

        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications', 'Data is incorrect please try again')
            return
        try:
            strr = "create database studentmanagementsystem"
            mycursor.execute(strr)
            strr = "use studentmanagementsystem"
            mycursor.execute(strr)
            mycursor.execute(
                "create table studentdata(id int,name varchar(20),mobile varchar(30),email varchar(50),address varchar(100)" 
                ",gender varchar(50),dob varchar(50),time varchar(40),date varchar(50))")
            messagebox.showinfo('Notification', 'database created and now you are connected to the database', parent=dbroot)


            mycursor.execute('alter table studentdata modify column id int not null')
            mycursor.execute('alter table studentdata modify column id int primary key')

        except:
            strr = "use studentmanagementsystem"
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'now you are connected to the database', parent=dbroot)

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('500x250+800+230')
    dbroot.iconbitmap('student.ico')
    dbroot.resizable(False, False)
    dbroot.config(bg='cornflower blue')
    #####--------------------------- CONNECT LABLES ---------------------#
    hostlable = Label(dbroot, text='Enter Host :', bg='gold2', font=('Big Caslon', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=13, anchor='w')
    hostlable.place(x=10, y=10)

    userlable = Label(dbroot, text='Enter User :', bg='gold2', font=('Big Caslon', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=13, anchor='w')
    userlable.place(x=10, y=70)

    passwordlable = Label(dbroot, text='Enter Password :', bg='gold2', font=('Big Caslon', 20, 'bold'), relief=GROOVE,
                          borderwidth=3, width=13, anchor='w')
    passwordlable.place(x=10, y=130)

    # -----------------------------------------Connect db entry-------------------------------------------#

    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot, font=('Big Caslon', 15, 'bold'), bd=5, textvariable=hostval)
    hostentry.place(x=250, y=10)

    userentry = Entry(dbroot, font=('Big Caslon', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('Big Caslon', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)

    # ------------------------------------------connect db button ------------------------------------#

    submitbutton = Button(dbroot, text='Submit', font=('Big Caslon', 15, 'bold'), bd=5, bg='sky blue'
                          , activebackground='tomato', activeforeground='white', relief=GROOVE, width=10,
                          command=submitdb)
    submitbutton.place(x=180, y=200)

    dbroot.mainloop()



############################################################################################

def tick():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")
    am_pm = time.strftime("%p")
    din = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%Y")


    clock.config(text='TIME:' + hour + ":" + minute + ":" + second + " " + am_pm + "\n" + "DATE:" + din + "/" + month +
                 "/" + year, anchor='w')


    clock.after(1000, tick)
    weekday.config(text='DAY=' + day)



################################################### INTRO SLIDER
colors = ['black', 'orange', 'orchid1', 'DarkSlateGray2', 'cadet blue']
def IntroLabelColorTick():
    fg = random.choice(colors)
    #print(fg)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2, IntroLabelColorTick)


def IntroLabelTick():
    global count, text
    if(count>=len(ss)):
        count = -1
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text + ss[count]
        SliderLabel.config(text=text)
    count += 1
    SliderLabel.after(100, IntroLabelTick)


##################################################################################################################
from tkinter import *
import time
import random
from tkinter import Toplevel, messagebox, filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import pandas



root = Tk()
root.title('student management system')
root.config(bg="cyan")
root.geometry('1174x700+200+40')
root.iconbitmap("student.ico")
root.resizable(False, False)

######################################################################################################### FRAMES ###
#-----------------------------dataentryframe---------------------------------------#


DataEntryFrame = Frame(root, bg='lavender', relief=GROOVE, borderwidth=10)
DataEntryFrame.place(x=10, y=80, width=500, height=600)



frontlabel = Label(DataEntryFrame, text='---------------WELCOME------------------', font=("Big Caslon", 20, ' bold'),
                   width=30, bg='olive')
frontlabel.pack(side=TOP, expand=True)

addbtn = Button(DataEntryFrame, text='1) Add students',width=20,  font=("Big Caslon", 22, ' bold'), bd=6, bg='gold',
                activeforeground='tomato', activebackground='aquamarine2', relief=GROOVE, command=addstudent)
addbtn.pack(side=TOP, expand=True)

searchbtn = Button(DataEntryFrame, text='2) Search students', width=20,  font=("Big Caslon", 22, ' bold'), bd=6, bg='gold',
                activeforeground='tomato', activebackground='aquamarine2', relief=GROOVE, command=searchstudent)
searchbtn.pack(side=TOP, expand=True)


deletebtn = Button(DataEntryFrame, text='3) Delete students', width=20,  font=("Big Caslon", 22, ' bold'), bd=6, bg='gold',
                activeforeground='tomato', activebackground='aquamarine2', relief=GROOVE, command=deletestudent)
deletebtn.pack(side=TOP, expand=True)


updatebtn = Button(DataEntryFrame, text='4) Update students', width=20,  font=("Big Caslon", 22, ' bold'), bd=6, bg='gold',
                activeforeground='tomato', activebackground='aquamarine2', relief=GROOVE, command=updatestudent)
updatebtn.pack(side=TOP, expand=True)

showbtn = Button(DataEntryFrame, text='5) Show all', width=20,  font=("Big Caslon", 22, ' bold'), bd=6, bg='gold',
                activeforeground='tomato', activebackground='aquamarine2', relief=GROOVE, command=showall)
showbtn.pack(side=TOP, expand=True)


exportbtn = Button(DataEntryFrame, text='6) Export data', width=20,  font=("Big Caslon", 22, ' bold'), bd=6, bg='gold',
                activeforeground='tomato', activebackground='aquamarine2', relief=GROOVE, command=exportall)
exportbtn.pack(side=TOP, expand=True)


exitbtn = Button(DataEntryFrame, text='7) Exit', width=20,  font=("Big Caslon", 22, ' bold'), bd=6, bg='gold',
                activeforeground='tomato', activebackground='aquamarine2', relief=GROOVE, command=exit)
exitbtn.pack(side=TOP, expand=True)








#----------------------------------------------- Show data frame ------------------------------------------#



ShowDataFrame = Frame(root, bg='antique white', relief=GROOVE, borderwidth=10)
ShowDataFrame.place(x=570, y=80, width=600, height=600)


#----------------------------------------------------------- Show data frame----------------------------#
style = ttk.Style()
style.configure('Treeview.Heading', font=("Big Caslon", 17, ' bold'), foreground='RoyalBlue2')
style.configure('Treeview', font=("times", 13, ' bold'), foreground='tomato', background='cyan')
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)





studenttable = Treeview(ShowDataFrame, columns=('ID', 'Name', 'Mobile no', 'Email', 'Address',  'Gender', 'D.O.B',
                         'Added Date', 'Added Time'), yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('ID', text='ID')
studenttable.heading('Name', text='Name')
studenttable.heading('Mobile no', text='Mobile no')
studenttable.heading('Email', text='Email')
studenttable.heading('Address', text='Address')
studenttable.heading('Gender', text='Gender')
studenttable.heading('D.O.B', text='D.O.B')
studenttable.heading('Added Date', text='Added Date')
studenttable.heading('Added Time', text='Added Time')
studenttable['show'] = 'headings'



















studenttable.pack(fill=BOTH, expand=1)




############################################################################################# SLIDER  ############
ss = 'welcome to student management system'
count = 0
text = ''
#################################################################

SliderLabel = Label(root, font=("Big Caslon", 22, ' bold'), text=ss, relief=RIDGE, borderwidth=5,
                    bg='LightCyan2', width=35, fg='orange3')
SliderLabel.place(x=300, y=0)
IntroLabelTick()
IntroLabelColorTick()

########################################################################################################## clock########

clock = Label(root, font=("Big Caslon", 20, ' bold'), borderwidth=5, bg='black', fg='green',anchor='w')
clock.place(x=0, y=0)
weekday = Label(root, font=("Big Caslon", 15, ' bold'), borderwidth=2, bg='tomato', anchor='w')
weekday.place(x=250, y=45)
tick()

#################################################### CONNECT TO DATABASE ##################################

ConnectButton = Button(root, text='Connect to \nDatabase', width=13,  font=("Big Caslon", 15, ' bold'), borderwidth=4,
                       bg='green yellow', relief=GROOVE, activebackground='gold',
                       activeforeground='white', command=connectdb)
ConnectButton.place(x=1000, y=0)




root.mainloop()
